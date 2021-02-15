# 2020-07-18 22:16:15
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask,request
from json import loads
import requests
import mes_answer
import _if_sleep

private_api_url = 'http://127.0.0.1:6700/send_private_msg'
group_api_url = 'http://127.0.0.1:6700/send_group_msg'

bot_server = Flask(__name__)
Cnt = 0
Last_id = 0

@bot_server.route('/api/message',methods=['POST'])

def run_group_message(mes):
    print('get!')
    global Cnt
    global Last_id
    grid = mes.get('group_id')
    usid = mes.get('user_id')
    print(usid)
    text = mes['raw_message']
    data = { 'group_id': grid, 'message' : '测试成功', 'auto_escape' : False }
    if Last_id == usid:
        Cnt += 1
    else:
        Last_id = usid
        Cnt = 1
    if (Cnt > 27) and (_if_sleep.flag == False):
        data['message'] = '[CQ:at,qq=%d] 刷屏的sb给爷爬' % usid
        r = requests.post(group_api_url, data)
        print(r.text)
        return ''
    mes_answer.solve(text, data, group_api_url, usid)
    return ''

def run_private_message(mes):
    usid = mes.get('user_id')
    text = mes['raw_message']
    print(text)
    data = { 'user_id': usid, 'message' : '测试成功', 'auto_escape' : False }
    mes_answer.solve(text, data, private_api_url, usid)
    return ''
