# 2020-07-20 11:14:50
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

aut_dict = {}
aut_file_name = 'aut_list'

def get_authority(id):
    global aut_dict
#   return 'bot_admin'
    print(id)
    if (id in aut_dict) == False:
        return 'NONE'
    return aut_dict[id]

def ban(id):
    global aut_dict
    aut_dict[id] = 'banned'
    f = open(aut_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
    f.write('%d\n' % id)
    f.write('banned' + '\n')
    f.close()
    return '[CQ:at,qq=%d] 您已被 ban' % id

def unban(id):
    global aut_dict
    aut_dict[id] = 'NONE'
    f = open(aut_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
    f.write('%d\n' % id)
    f.write('NONE' + '\n')
    f.close()
    return '[CQ:at,qq=%d] 您可以正常使用 bot 了' % id

def give_admin(id):
    global aut_dict
    aut_dict[id] = 'admin'
    f = open(aut_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
    f.write('%d\n' % id)
    f.write('admin' + '\n')
    f.close()
    return '[CQ:at,qq=%d] 您已被授予 admin 权限' % id

def cancel_admin(id):
    global aut_dict
    aut_dict[id] = 'NONE'
    f = open(aut_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
    f.write('%d\n' % id)
    f.write('NONE' + '\n')
    f.close()
    return '[CQ:at,qq=%d] 您的 admin 权限已被取消' % id

def _init():
    global aut_dict
    f = open(aut_file_name, 'r', encoding = 'utf-8', errors = 'ignore')
    s = f.readlines()
    f.close()
    l = len(s)
    for i in range(0, l, 2):
        id = int(s[i][:-1], 10)
        print(id, s[i + 1][:-1])
        aut_dict[id] = s[i + 1][:-1]
