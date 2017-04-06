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

from . import datafile_manager


def _show(command):
    if command == 'show tables;':
        datafile_manager.show_tables()

def _select(command):
    print('this is select')

def _insert(command):
    print('this is insert')

def _update(command):
    print('this is update')

def _drop(command):
    print('this is drop')

def _create(command):
    print('this is create %s'%(command))

