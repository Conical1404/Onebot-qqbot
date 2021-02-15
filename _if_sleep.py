# 2020-07-20 11:02:38
# Author: Conical
# !/usr/bin/python
# -*- coding: utf-8 -*-

flag = False

def sleep():
    global flag
    flag = True

def wake_up():
    global flag
    flag = False
