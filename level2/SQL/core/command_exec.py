#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: sql_exec.py
@time: 2017/4/6 0:11
"""
import re
from . import dbf_manager

def _show(command):
    if re.match('show\s+tables\Z', command):
        print('ok')
    else:
        print('语法错误！~')

def _select(command):
#select * from emp & select xx,xx from emp
    if re.match('select\s+(\*|.+)\s+from\s+\w+\.*',command):
        print('ok')
    else:
        print('语法错误！~')

def _insert(command):
#insert into emp values (xxxxxx.xxx.xx)
    if re.match('insert\s+into+'
                '\s+.+\s+\(.*\)',command):
        print(ok)
    else:
        print('语法错误！~')

def _update(command):
#update emp set sss=sss where xxx
    print('this is update')

def _drop(command):
#drop table emp;
    print('this is drop')

def _create(command):
# create table xxx (id int ,name str)
    if re.match('create\s+table\s+.+\s+\(.*\)',command):
        print(ok)
    else:
        print('语法错误！~')
