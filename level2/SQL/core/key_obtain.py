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

from . import dbf_manager

def check_tabname(tabname):
    db = dbf_manager.dbf_load()
    if tabname in db[tablelist]:
        return True
    else:
        return False


def get_tablename(command):
    command_list = command.split(' ')
    tablename = command_list[command_list.index('from') + 1]
    return tablename

def get_colname(command):
    """
    获取需要查询的列
    :param command: 
    :return: 
    """
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


