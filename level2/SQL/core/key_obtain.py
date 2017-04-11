#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: key_obtain.py
@time: 2017/4/9 22:56
"""

import dbf_manager

def get_tablename(command):
    command_list = command.split(' ')
    tablename = command_list[command_list.index('from') + 1]
    return tablename

def get_colname(command):
    colsname=[]
    command_list = command.split(' ')
    cols = command_list[command_list.index('from') - 1]
    tablename = command_list[command_list.index('from') + 1]
    if cols == '*':
        db = dbf_manager.dbf_load()
        for dict in db['tablelist'][tablename]:
            for k in dict:
                colsname.append(k)
    else:
        colsname = cols.split(',')

    return colsname

def get_where_key():
    pass

def check_colname():
    pass

def check_where_key():
    pass



command = 'select staff_id，name from emp'
print(get_colname(command))
