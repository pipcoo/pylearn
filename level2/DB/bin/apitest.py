#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: dbstart.py
@time: 2017/4/5 23:38
"""

import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from core import db




db.sqlapi('emp','drop table staff_table')

db.sqlapi('emp','create table staff_table (staff_id int not null auto_increment,name str unique,age int ,phone str ,dept str,enroll_date str )')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li,22,13651054608,IT,2013-04-01\)')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li2,22,13651054608,IT,2013-04-01\)')

print(db.sqlapi('emp','select * from staff_table where staff_id >= 1'))