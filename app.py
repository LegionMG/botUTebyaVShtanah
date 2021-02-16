# -*- coding: utf-8 -*-
import telebot
import time
from datetime import date, datetime
from telebot import types
import requests
import random
import re
from pymystem3 import Mystem

token = 'enter_your_token'

bot = telebot.TeleBot(token)
STEMMER = Mystem()
SHIT_PERCENT = 0.01

@bot.message_handler(commands=["rp"])
def rare_parrot(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'http://i.imgur.com/2czseQm.gif')


@bot.message_handler(content_types=['text'])
def send_text(message):
    try:
        words = STEMMER.lemmatize(message.text)
        words = [x.strip() for x in words if len(x.strip()) > 1]
        chosen_one = random.choice(words).strip()
        if random.random() > SHIT_PERCENT and len(chosen_one) > 0 and chosen_one != " ":
            print(' '.join(words), f"'{chosen_one}'")
            bot.reply_to(message, f"{chosen_one} у тебя в штанах")
    except:
        pass

   

if __name__ == '__main__':
    bot.polling(none_stop=True, timeout=123)