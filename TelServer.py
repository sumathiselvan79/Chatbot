
import telepot
import time
import urllib3
from config import *
import json
import Bot
import tflearn
import tensorflow as tf
import subprocess
import Main
import sys
import _thread



proxy_url = "http://proxy.server:3128"
# telepot.api._pools = {
#     'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3, maxsize=10, retries=3, timeout=30),
# }
telepot.api._onetime_pool_spec = (urllib3.ProxyManager, dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False, timeout=30))

bot = telepot.Bot(BOT_TOKEN)
prevText = {}
prevReply = {}
permAdmin = [395906775]
people = []
admin = [395906775]


def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    print(content_type, chat_type, chat_id)

    if content_type == 'text':

        if chat_id not in people:
            bot.sendMessage(chat_id, "Hello! I'm the BOSSBot. How can i help you?")
            people.append(chat_id)
        if chat_id:
            reply = Bot.response(msg["text"], chat_id)
            prevText[chat_id] = msg["text"]
            prevReply[chat_id] = reply
            if not reply == None:
                bot.sendMessage(chat_id, reply)
            else:
                bot.sendMessage(chat_id, "I'm sorry, I didn't understand you. Could you rephrase it please?")
            print(prevReply, prevText)

bot.message_loop(handle)

print('Listening ...')
while 1:
    time.sleep(10)
