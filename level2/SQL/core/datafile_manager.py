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

import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATADIR=BASE+'\data'

def show_tables():
    f = open(DATADIR+"\\table.list","r",encoding="utf-8")
    tablelist=f.readline().split(' ')
    for tablename in tablelist:
        print(tablename,'\n')