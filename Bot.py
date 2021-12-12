#Bot Help With Plugin Codes
import telebot 
import requests
import random 
import vodka
from telebot import types
from time import sleep
import time
import os,sys
def vodka(s):
 for ASU in s + '\n':
  sys.stdout.write(ASU)
  sys.stdout.flush()
  sleep(2./600)
Z = '\x1b[1;31m'#احمر
X = '\x1b[1;32m'#اخضر
C = '\x1b[1;33m'#yellow
V = '\x1b[1;34m'#blue	
B = '\x1b[1;35m'#pink
N = '\x1b[1;36m'#لبني
M = '\x1b[1;37m'#ابيض	 
t = time.localtime()
current_time = time.strftime('%H:%M:%S', t)
current_date =  time.strftime('%D', t)
vodka(X+'__     _____  ____  _  __    _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / ___ \ ')
vodka(X+'   \_/  \___/|____/|_|\_\/_/   \_\ ')
vodka(N+'Time Now : '+M+current_time)
vodka(N+'Date Now : '+M+current_date)
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Telegram : '+M+'@Vodka_tk')
vodka(Z+'('+X+'⌯'+Z+')'+N+'GitHub : '+M+'https://github.com/Vodkahunter.com')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program Code : '+M+'python3')
vodka(Z+'('+X+'⌯'+Z+')'+N+'Program App : '+M+'pycharm')
vodka(M+'- - - - - - - - - - - - - - - - - - - - ')
Token = input(N+'('+B+'⌯'+N+')'+B+'Enter Token : '+M)
bot = telebot.TeleBot(Token)
co = types.InlineKeyboardButton(text ="- VODKA_Tools </>",url='https://t.me/Vodka_Tools')
by = types.InlineKeyboardButton(text ="- Version",callback_data = 'vodka')
@bot.message_handler(commands=['start'])
def first(message):
    maac = types.InlineKeyboardMarkup()
    maac.row_width = 2
    maac.add(co,by)    
    bot.send_message(message.chat.id,f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWelcome To WebSite Maker!\nSend Your Information Like /example\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "vodka":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="- VERSION 0.0.1")   
@bot.message_handler(commands=['example'])
def ex(message):   
    ex = '''
    name = Vodka
    description = Python Programmer
    locashion = Egypt
    instagram = vodka.ks
    snapchat = joo_2277
    telegram = Vodka_Tools
    twitter = elonmusk
    url1 = vodka-apis.rf.gd
    url2 = blagram.live
    '''
    bot.send_message(message.chat.id,ex)
         
@bot.message_handler(func=lambda m: True)
def Get(message):
    try:
        msg = message.text
        data = str(msg).split('\n')
        name = data[0].split('=')[1].strip()
        discription = data[1].split('=')[1].strip()
        locashion = data[2].split('=')[1].strip()
        instagram = data[3].split('=')[1].strip()
        snapchat = data[4].split('=')[1].strip()
        telegram = data[5].split('=')[1].strip()
        twitter = data[6].split('=')[1].strip()
        url1 = data[7].split('=')[1].strip()
        url2 = data[8].split('=')[1].strip()

        bot.send_message(message.chat.id, text="*Making your website* ⌛\nPlease wait!",parse_mode='markdown')

        url = f'https://apis.red/apiV2/make-me/?main={name}&name={name}&discription={discription}&instagram={instagram}&snapchat={snapchat}&telegram={telegram}&twitter={twitter}&locashion={locashion}&url1={url1}&url2={url2}'
        req = requests.get(url).json()
        if req['stats'] == 'taken':
            bot.send_message(message.chat.id, text=f"*Taken Main Name* 🔒\n Try another!", parse_mode="markdown",
                             disable_web_page_preview=True)
        else:
            your_page = req['url']
            bot.send_message(message.chat.id, text=f"*Done Make The WebSite*: {your_page}", parse_mode="markdown",disable_web_page_preview=True)
    except:
        bot.send_message(message.chat.id, text=f"Error", parse_mode="markdown")

bot.polling(True)
