# 2020-07-29 23:09:26
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

import random

_global_dict = {}
_dict_Cnt = 0
_corpus_file_name = 'corpus'

def set_value(text1, text2, flag = False):
    global _global_dict
    global _dict_Cnt
    if flag == False and len(text2) > 30:
        return '语料添加失败。当前语料过长'
    if (text1 in _global_dict) == False:
        _global_dict[text1] = []
    if (text2 in _global_dict[text1]) == False:
        if len(_global_dict[text1]) >= 7:
            return '语料添加失败。当前语料已达上限'
        _global_dict[text1].append(text2)
        _dict_Cnt += 1
        if flag == False:
            f = open(_corpus_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
            f.write('add' + '\n')
            f.write(text1 + '\n')
            f.write(text2 + '\n')
            f.close()
        return '语料添加成功！当前语料总数 %d' % _dict_Cnt
    return '语料已存在'

def del_value(text1, text2, flag = False):
    global _global_dict
    global _dict_Cnt
    if (text1 in _global_dict) == False:
        return '语料不存在'
    if (text2 in _global_dict[text1]) == False:
        return '语料不存在'
    _global_dict[text1].remove(text2)
    _dict_Cnt -= 1
    if len(_global_dict[text1]) == 0:
        _global_dict.pop(text1)
    if flag == False:
        f = open(_corpus_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
        f.write('del' + '\n')
        f.write(text1 + '\n')
        f.write(text2 + '\n')
        f.close()
    return '语料删除成功！当前语料总数 %d' % _dict_Cnt

def del_all(text):
    global _global_dict
    global _dict_Cnt
    if (text in _global_dict) == False:
        return '语料不存在'
    _dict_Cnt -= len(_global_dict[text])
    f = open(_corpus_file_name, 'a', encoding = 'utf-8', errors = 'ignore')
    for text2 in _global_dict[text]:
        f.write('del' + '\n')
        f.write(text + '\n')
        f.write(text2 + '\n')
    f.close()
    _global_dict.pop(text)
    return '语料删除成功！当前语料总数 %d' % _dict_Cnt

def clear():
    global _global_dict
    global _dict_Cnt
    _dict_Cnt = 0
    _global_dict = {}
    f = open(_corpus_file_name, 'w', encoding = 'utf-8', errors = 'ignore')
    f.close()

def refresh_corpus():
    global _global_dict
    f = open(_corpus_file_name, 'w', encoding = 'utf-8', errors = 'ignore')
    for i in _global_dict:
        for j in _global_dict[i]:
            f.write('add' + '\n')
            f.write(i + '\n')
            f.write(j + '\n')
    f.close()

def _init():
    global _global_dict
    global _dict_Cnt
    f = open(_corpus_file_name, 'r', encoding = 'utf-8', errors = 'ignore')
    _corpus_list = f.readlines()
    f.close()
    l = len(_corpus_list)
    print(l)
    for i in range(0, l, 3):
        if _corpus_list[i][:-1] == 'add':
            set_value(_corpus_list[i + 1][:-1], _corpus_list[i + 2][:-1], flag = True)
        else:
            del_value(_corpus_list[i + 1][:-1], _corpus_list[i + 2][:-1], flag = True)
    refresh_corpus()

def get_corpus_size():
    return _dict_Cnt

def get_value(text):
    global _global_dict
    # print(text, len(_global_dict))
    if (text in _global_dict) == False:
        return '#@$'
    s = ''
    for text1 in _global_dict[text]:
        s += text1 + '$%$'
    return s

'''
目前计划，按群号建立文件夹，构建 corpus
则进行语料库读取时，需要传入消息类型（群聊、私聊）及群号或 QQ 号
（似乎只需要改一下读文件就可以了）
（假了假了，字典也得改）
（初始化的时候也得遍历文件夹）
（这样的话自动通过加群/加好友申请也得加上了，加的时候建立相关 data 文件）
（口胡完了，懒得实现了（雾））
'''
