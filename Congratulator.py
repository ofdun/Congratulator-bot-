import telebot
import requests
from bs4 import BeautifulSoup
from telebot import types
#import time

info = requests.get('https://my-calend.ru/holidays')
soup = BeautifulSoup(info.content, 'html.parser')
congratulation = soup.find('ul',class_='holidays-items')
congratulation = congratulation.find('li')
congratulation = congratulation.find('a')
congratulation = congratulation.text

#local_time = time.ctime()
#local_time = local_time[11:16]
#print(local_time)
bot = telebot.TeleBot('5249857314:AAH-LY-pF2njWoUOx9MkqVaEm3Q_C3a_isc')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Поздравь меня🥳")
    btn2 = types.KeyboardButton("Что это за праздник?")
    btn3 = types.KeyboardButton("Ура!🎉")
    markup.add(btn1, btn3)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я поздравлю тебя с праздником!".format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
        if message.text == 'Поздравь меня🥳':
                markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = "Что это за праздник?"
                btn2 = 'Ура!🎉'
                markup.add(btn1,btn2)
                bot.send_message(message.from_user.id, congratulation + '!' + ' Ура!', reply_markup=markup)
        elif message.text == 'Что это за праздник?':
                markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
                btn1 = types.KeyboardButton("Поздравь меня🥳")
                btn3 = types.KeyboardButton("Ура!🎉")
                markup.add(btn1,btn3)
                bot.send_message(message.from_user.id, WhatIsThat, reply_markup=markup)
        elif message.text == 'Ура!🎉':
                bot.send_message(message.from_user.id, 'Ура!')
        elif message.text != '1':
                bot.send_message(message.from_user.id, 'напиши /start')

site = 'https://www.google.com/search?q=что+такое'
solved_site = site + congratulation
info = requests.get(solved_site)
soup = BeautifulSoup(info.content, 'html.parser')
WhatIsThat = soup.find('div', class_='BNeawe s3v9rd AP7Wnd')
WhatIsThat = WhatIsThat.find('div', class_='BNeawe s3v9rd AP7Wnd')
WhatIsThat = WhatIsThat.text.replace('<0xa0>','').replace('...','')
for i in range(len(WhatIsThat)):
        if WhatIsThat[i]=='.':
                WhatIsThat=WhatIsThat[:i+1]
                break
        i+=1


#print(WhatIsThat)

bot.polling(none_stop=True, interval=0)