#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: dbf_manager.py
@time: 2017/4/9 11:24
"""

import os,sys,json

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def dbf_load():
    f = open (BASE+'/data/db.dbf','r',encoding='utf-8')
    db = json.load(f)
    return db

