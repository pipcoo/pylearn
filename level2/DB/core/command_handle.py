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
from . import dbfile_handle


def _show(command):
    if re.match('show\s+databases\Z', command):
        dbfile_handle.get_databases()
    elif re.match('show\s+tables\Z', command):
        dbfile_handle.get_tables()
    else:
        print('语法错误！~')

def _select(command):
#select * from emp & select xx,xx from emp
    if re.match('select\s+(\*|.+)\s+from\s+\w+\.*',command):
        print(key_obtain.get_colname(command))
    else:
        print('语法错误！~')

def _insert(command):
#insert into emp values (xxxxxx.xxx.xx)
    if re.match('insert\s+into+'
                '\s+.+\s+\(.*\)',command):
        pass  # todo
    else:
        print('语法错误！~')

def _update(command):
#update emp set sss=sss where xxx
    pass  # todo

def _drop(command):
#drop table emp;
    pass  # todo

def _create(command):
# create table xxx (id int ,name str)
    if re.match('create\s+table\s+.+\s+\(.*\)',command):
        print(ok)
    else:
        print('语法错误！~')

def _use(command):
#drop table emp;
    pass  # todo


def _delete(command):
#drop table emp;
    pass  # todo