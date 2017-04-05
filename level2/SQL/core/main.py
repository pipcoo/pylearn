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

def sqlplus():
    exit_flag = False
    while not exit_flag:
        sql_input=input('SQL>')
        sql_command = sql_input.split()
        if sql_command[0] == 'exit':
            exit_flag=True
        elif sql_command[0] == 'show':
            command_exec._show
        elif sql_command[0] == 'create':
            command_exec._create
        elif sql_command[0] == 'insert':
            command_exec._insert
        elif sql_command[0] == 'select':
            command_exec._select
        elif sql_command[0] == 'delete':
            command_exec._delete
        elif sql_command[0] == 'drop':
            command_exec._drop
