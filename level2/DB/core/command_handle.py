#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: command_handle.py
@time: 2017/4/12 22:56
"""

import re
#import dbf_manager
from . import dbfile_handle,key_handle


def _show(command,current_database=''):
    if re.match('show\s+databases\Z', command):
        dbfile_handle.get_databases(command)
    elif re.match('show\s+tables\Z', command):
        if current_database != '':

            dbfile_handle.get_tables(current_database)
        else:
            print('请选择当前数据库~')
    else:
        print('语法错误！~')

def _select(command,current_database=''):
#select * from emp & select xx,xx from emp
    if re.match('select\s+(\*|.+)\s+from\s+\w+\.*',command):
        if current_database != '':
            tabname = key_handle.get_tablename(command)
            if tabname in dbfile_handle.get_tables(current_database):
                dbfile_handle.print_result(current_database, tabname, \
                             dbfile_handle.select_table(current_database, tabname,key_handle.get_where_key(current_database, tabname,command))[0],
                             key_handle.get_colname(command))

            else:
                print('表%s不存在'%(tabname))
            print(key_handle.get_colname(command))
        else:
            print('请选择当前数据库~')

    else:
        print('语法错误！~')

def _insert(command,current_database=''):
#insert into emp values (xxxxxx.xxx.xx)
    if re.match('insert\s+into+'
                '\s+.+\s+\(.*\)',command):
        pass  # todo
    else:
        print('语法错误！~')

def _update(command,current_database=''):
#update emp set sss=sss where xxx
    pass  # todo

def _drop(command,current_database=''):
#drop table emp;
    pass  # todo

def _create(command,current_database=''):
# create table xxx (id int ,name str)
    if re.match('create\s+table\s+.+\s+\(.*\)',command):
        print(ok)
    else:
        print('语法错误！~')

def _use(command):

    if re.match('use\s+\w+)',command):
        current_database  = dbfile_handle.get_databases(command)
        if current_database in dbfile_handle.get_databases():
            return current_database
        else:
            print ('您输入的数据库不存在！')
    else:
        print('语法错误！~')


def _delete(command,current_database=''):
#drop table emp;
    pass  # todo