# 2020-07-19 07:44:37
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import random
import _corpus
import _if_sleep
import authority
import random
# import record_mes
import _api_mes

def get_hash_key(text):
    l = len(text)
    for i in range(l):
        if text[i] == '#':
            return i
    return -1

def get_file(_file_name):
    with open(_file_name, 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def get_todo_list():
    with open('todo_list.txt', 'r', encoding='utf-8', errors='ignore') as f:
        return f.read()

def send_mes(data, text, api_url, _if_record = False):
    data['message'] = text
    r = requests.post(api_url, data)
    print(r.text)

def output(data, text, api_url, _if_record = False):
    i = 0
    j = 0
    text = text.replace('#$@$#', '\n')
    l = len(text)
    while i < l:
        j = text.find('$%$', i, l)
        if j == -1:
            break
        send_mes(data, text[i:j], api_url, _if_record)
        i = j + 3
    if i < l:
        send_mes(data, text[i:l], api_url, _if_record)
    return

def solve_command(text, data, api_url, usid):
    #system call:
    l = len(text)
    au = authority.get_authority(usid)

    if (text == '#system call:wake up'):
        if (au == 'root') or (au == 'admin') :
            _if_sleep.wake_up()
            output(data, 'bot 已唤醒', api_url)
        else:
            output(data, '权限不足', api_url)
        return

    if _if_sleep.flag:
        return

    if text == '#历史上的今天':
        output(data, _api_mes.history_of_today(), api_url)
        return

    if text == '#二次元':
        output(data, _api_mes.random_acg_pic(), api_url)
        return

    # if text == '#精神小伙':
    #     output(data, _api_mes.spirit_guy(), api_url)
    #     return

    if text == '#一言':
        output(data, _api_mes.random_hitokoto(), api_url)
        return

    if text == '#system call:sleep':
        if (au == 'root') or (au == 'admin') :
            _if_sleep.sleep()
            output(data, 'bot 已休眠', api_url)
        else:
            output(data, '权限不足', api_url)
        return

    if text == '#system call:refresh corpus':
        _corpus.refresh_corpus()
        output(data, '语料库已刷新', api_url)
        return

    if text == '#system call:clear corpus':
        if au == 'root':
            _corpus.clear()
            output(data, '语料库已清除', api_url)
        else:
            output(data, '权限不足', api_url)
        return

    if text == '#system call:inspect entire command list' or text == '#help':
        output(data, get_file('command_list.txt'), api_url)
        return

    if text == '#system call:inspect corpus size':
        output(data, '当前语料总数%d' % _corpus.get_corpus_size(), api_url)
        return

    if text == '#更新日志':
        output(data, get_file('update.log'), api_url)
        return

    if text == '#system call:inspect todo list':
        output(data, get_file('todo_list.txt'), api_url)
        return

    l1 = get_hash_key(text[1:l])
    if l1 == -1:
        output(data, 'COMMAND ERROR', api_url)
        return
    l1 += 1
    command = text[1:l1]

    if command == 'add':
        if (au == 'banned'):
            output(data, '权限不足', api_url)
            return
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        l2 = get_hash_key(text[l1 + 1:l])
        if l2 == -1:
            output(data, 'COMMAND ERROR', api_url)
            return
        l2 += l1 + 1
        if l == l2:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l2]
        text2 = text[l2 + 1:l]
        output(data, _corpus.set_value(text1, text2), api_url)
        return

    if command == 'delete':
        if (au != 'root') and (au != 'admin'):
            output(data, '权限不足', api_url)
            return
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        l2 = get_hash_key(text[l1 + 1:l])
        if l2 == -1:
            output(data, 'COMMAND ERROR', api_url)
            return
        l2 += l1 + 1
        if l == l2:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l2]
        text2 = text[l2 + 1:l]
        output(data, _corpus.del_value(text1, text2), api_url)
        return

    if command == 'delete all':
        if (au != 'root') and (au != 'admin'):
            output(data, '权限不足', api_url)
            return
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l]
        output(data, _corpus.del_all(text1), api_url)
        return

    if command == 'ban':
        if au != 'root':
            output(data, '权限不足', api_url)
            return
        print('ban')
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l]
        toid = int(text1, 10)
        output(data, authority.ban(toid), api_url)
        return

    if command == 'unban':
        if au != 'root':
            output(data, '权限不足', api_url)
            return
        print('ban')
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l]
        toid = int(text1, 10)
        output(data, authority.unban(toid), api_url)
        return

    if command == 'give admin to':
        if au != 'root':
            output(data, '权限不足', api_url)
            return
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l]
        toid = int(text1, 10)
        output(data, authority.give_admin(toid), api_url)
        return

    if command == 'cancel admin':
        if au != 'root':
            output(data, '权限不足', api_url)
            return
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        text1 = text[l1 + 1:l]
        toid = int(text1, 10)
        output(data, authority.cancel_admin(toid), api_url)
        return

    if command == 'roll':
        if l == l1:
            output(data, 'COMMAND ERROR', api_url)
            return
        _roll_pool_  = []
        l2 = 0
        print(text)
        while l2 != -1:
            l2 = get_hash_key(text[l1 + 1:l])
            print(l1, l2, l)
            if l2 == -1:
                break
            l2 += l1 + 1
            _roll_pool_.append(text[l1 + 1:l2])
            l1 = l2
        _roll_pool_.append(text[l1 + 1:l])
        _l = len(_roll_pool_)
        output(data, _roll_pool_[random.randint(0,_l - 1)], api_url)
        return

    output(data, 'COMMAND ERROR', api_url)
    return

def solve(text, data, api_url, usid):
    # print(text)
    text = text.replace('\r\n', '#$@$#')
    text = text.replace('\n', '#$@$#')
    # print(text)
    l = len(text)
    # print(l)
    if text[0] == '#':
        solve_command(text, data, api_url, usid)
        return
    if _if_sleep.flag:
        return
    if text == 'test':
        output(data, '测试成功', api_url)
        return
    _tax_dict = []
    for i in range(l):
        for j in range(i, l):
            s = text[i:j + 1]
            if s in _tax_dict:
                continue
            _tax_dict.append(s)
            _mes = _corpus.get_value(s)
            if _mes != '#@$':
                output(data, _mes, api_url)
    if random.random() >= 0.95:
        output(data, text, api_url)
    return
