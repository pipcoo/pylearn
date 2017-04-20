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

        print(dbfile_handle.get_databases())

    elif re.match('show\s+tables\Z', command):
        if current_database != '':

            print(dbfile_handle.get_tables(current_database))
        else:
            print('请选择当前数据库~')
    else:
        print('语法错误！~')

def _select(command,current_database=''):
#select * from emp & select xx,xx from emp
    if re.match('select\s+(\*|.+)\s+from\s+\w+\.*',command) and 'where' not in command:
        if current_database != '':
            tabname = key_handle.get_tablename(command)
            if tabname in dbfile_handle.get_tables(current_database):
                dbfile_handle.print_result(current_database, tabname, \
                             dbfile_handle.select_table(current_database, tabname)[0], \
                             key_handle.get_colname(current_database, tabname,command))

            else:
                print('表%s不存在'%(tabname))
            #print(key_handle.get_colname(current_database, tabname,command))
        else:
            print('请选择当前数据库~')
    elif re.match('select\s+(\*|.+)\s+from\s+\w+\s+where\.*',command):
        if current_database != '':
            tabname = key_handle.get_tablename(command)
            if tabname in dbfile_handle.get_tables(current_database):
                dbfile_handle.print_result(current_database, tabname, \
                             dbfile_handle.select_table(current_database, tabname,key_handle.get_where_key(current_database, tabname,command))[0],
                             key_handle.get_colname(current_database, tabname,command))

            else:
                print('表%s不存在'%(tabname))
            #print(key_handle.get_colname(current_database, tabname,command))
        else:
            print('请选择当前数据库~')

    else:
        print('语法错误！~')

def _insert(command,current_database=''):
#insert into emp values (xxxxxx.xxx.xx)
    if re.match('insert\s+into+\s+\w+\s+values\s+\(.*\)',command):
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
    if re.match('create\s+table\s+.+\s+\(.*\)',command) and current_database != '':
        tabname =command.replace('   ',' ').replace('  ',' ').split(' ')[2]
        dbfile_handle.create_table(current_database,command)
    elif re.match('create\s+table\s+.+\s+\(.*\)',command) and current_database == '':
        print('请选择数据库')
    elif re.match('create\s+database\s+.+',command):
        database_name = command.replace(' ','').split('database')[1]
        dbfile_handle.create_database(database_name)
    else:
        print('语法错误！~')


def _use(command):

    if re.match('use\s+\w+',command):
        current_database  = command.replace('  ',' ').split(' ')[1]

        if current_database in dbfile_handle.get_databases():
            return current_database
        else:
            print ('您输入的数据库不存在！')
            return ''
    else:
        print('语法错误！~')
        return ''


def _delete(command,current_database=''):
#drop table emp;
    pass  # todo


#dbfile_handle.print_result('emp', 'staff_table', dbfile_handle.select_table('emp', 'staff_table')[0], key_handle.get_colname('emp', 'staff_table','select * from staff_table'))