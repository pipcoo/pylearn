#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: db.py
@time: 2017/4/12 22:50
"""

import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from . import command_handle

import re

def sqlplus():
    """
    数据库命令行控制台
    :return: 
    """
    exit_flag = False
    current_database = ''
    while not exit_flag:
        sql_input=input('SQL>')
        if len(sql_input)>1:
            sql_command = re.match('\w+',sql_input).group() #获取输入的第一个关键字
            if sql_input == 'exit':
                exit_flag=True
            elif sql_command == 'show':
                command_handle._show(sql_input,current_database)
            elif sql_command == 'use':
                current_database = command_handle._use(sql_input)
                print('切换到数据库 %s'%(current_database))
            elif sql_command == 'create':
                command_handle._create(sql_input,current_database)
            elif sql_command == 'insert':
                command_handle._insert(sql_input,current_database)
            elif sql_command == 'update':
                command_handle._update(sql_input,current_database)
            elif sql_command == 'select':
                command_handle._select(sql_input,current_database)
            elif sql_command == 'delete':
                command_handle._delete(sql_input,current_database)
            elif sql_command == 'drop':
                command_handle._drop(sql_input,current_database)
            else:
                print('输入错误！~')
        else:
            print('输入错误！~')


def sqlapi(current_database,command):

    sql_command = re.match('\w+', sql_input).group()

    if sql_command == 'create':
        command_handle._create(command, current_database)
    elif sql_command == 'insert':
        command_handle._insert(command, current_database)
    elif sql_command == 'update':
        command_handle._update(command, current_database)
    elif sql_command == 'select':
        return command_handle._select(command, current_database)
    elif sql_command == 'delete':
        command_handle._delete(command, current_database)
    elif sql_command == 'drop':
        command_handle._drop(command, current_database)
    else:
        print('输入错误！~')
