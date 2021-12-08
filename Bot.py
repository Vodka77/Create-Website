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
vodka(X+'__     _  ____  _      _    ')
vodka(Z+'\ \   / / _ \|  _ \| |/ /   / \   ')
vodka(X+' \ \ / / | | | | | |   /   / _ \  ')
vodka(Z+'  \ V /| |_| | |_| | . \  / _ \ ')
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
    bot.send_photo(message.chat.id, 'https://t.me/mbttt/7',f'<b>Hi VODKA #1st - python☬\n- - - - - - - - - - - - - -\nWebSite Maker Bot\nSend Your Data Like The Photo\n- - - - - - - - - - - - - -\nBy  : @Vodka_tk</b>', parse_mode="html",reply_to_message_id=message.message_id, reply_markup=maac)
@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
    if call.data == "vodka":
        bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="- VERSION 0.0.1")
@bot.message.handler(func=lambda m:True)
def web_maker(message):
    try: 
        msg = message.text 
        data = str(msg).split('|') 
        main = data[1]
        name = data[2]     
        discription = data[3] 
        instagram = data[4]             
        snapchat = data[5] 
        telegram = data[6] 
        twitter = data[7] 
        locashion = data[8] 
        bot.send_message(message.chat.id, text="*- Wait Website Is Creating*",parse_mode="markdown") 
        url = f'https://apis.red/apiV2/make-me/?main={main}&name={name}&discription={discription}&instagram={instagram}&snapchat={snapchat}&telegram={telegram}&twitter={twitter}&locashion={locashion}&url1=https://t.me/VODKA_Tk&url2=https://t.me/Vodka_Tools' 
        req = requests.get(url).json() 
        your_page = req['url']
        bot.send_message(message.chat.id, text=f"*Your Page Url*: {your_page}", parse_mode="markdown",disable_web_page_preview=True)
    except:
        pass
bot.polling(True)
