# 2020-07-18 22:16:15
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request
from json import loads
import message
import requests
import _corpus
import mes_answer
import _if_sleep
import authority

private_api_url = 'http://127.0.0.1:6700/send_private_msg'
group_api_url = 'http://127.0.0.1:6700/send_group_msg'

bot_server = Flask(__name__)

@bot_server.route('/api/message',methods=['POST'])

def server():
    data = request.get_data().decode('utf-8')
    data = loads(data)
    mes_type = data.get('message_type')
    if _if_sleep.flag == False:
        print(data)
    if mes_type == 'group':
        message.run_group_message(data)
    else:
        message.run_private_message(data)
    return ''
if __name__=='__main__':
    _corpus._init()
    authority._init()
    bot_server.run(port=5701)
