#!/usr/bin/env python
# -*- coding: utf-8 -*-

import telebot
import time
from telebot import types


TOKEN = "TOKEN"


bot = telebot.TeleBot(TOKEN)

# HANDLERS #################################################

@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, """\
------- Bot de prova -------

/help : Ajuda de commandes.

--------------------------
\
""")



# FUNCIONS ############################################

def listener(messages):
	try:
		for msg in messages:
			cid = msg.chat.id
			print str(cid)+" -->"+msg.text
	except:
		print 'error'



target=bot.set_update_listener(listener)






######################################################################

while(1):
    try:
            bot.polling(none_stop=True)
    except Exception as err:
            logging.error(err)
            time.sleep(5)
            print "Internet error!"

########################################################################


