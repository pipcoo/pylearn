#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: main.py
@time: 2017/4/5 23:48
"""
import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from core import command_exec
import re

def sqlplus():
    exit_flag = False
    while not exit_flag:
        sql_input=input('SQL>')
        if len(sql_input)>1:
            sql_command = re.match('\w+',sql_input).group()
            if sql_command == 'exit':
                exit_flag=True
            elif sql_command == 'show':
                command_exec._show(sql_input)
            elif sql_command == 'create':
                command_exec._create(sql_input)
            elif sql_command == 'insert':
                command_exec._insert(sql_input)
            elif sql_command == 'select':
                command_exec._select(sql_input)
            elif sql_command == 'delete':
                command_exec._delete(sql_input)
            elif sql_command == 'drop':
                command_exec._drop(sql_input)
            else:
                print('输入错误！~')
        else:
            print('输入错误！~')
