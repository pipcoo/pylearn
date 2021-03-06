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


db.sqlapi('','create database emp')

db.sqlapi('emp','drop table staff_table')

db.sqlapi('emp','create table staff_table (staff_id int not null auto_increment,name str unique,age int ,phone str ,dept str,enroll_date str )')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li,22,13651054608,IT,2013-04-01\)')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li2,22,13651054608,IT,2013-04-01\)')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li2,22,13651054608,IT,2013-04-01\)')

db.sqlapi('emp','update staff_table set name = wang1 where staff_id = 1')

db.sqlapi('emp','delete from staff_table where staff_id = 2')

db.sqlapi('emp','insert into staff_table values \(\'\',wang1,22,13651054608,IT,2013-04-01\)')

db.sqlapi('emp','insert into staff_table values \(\'\',Alex Li,22,13651054608,IT,2013-04-01\)')

print(db.sqlapi('emp','select * from staff_table where staff_id >= 1'))

print(db.sqlapi('emp','select age,name,phone from staff_table where name like "Li" '))



#db.sqlapi('','create database atmdb')
db.sqlapi('atmdb','drop table account')
db.sqlapi('atmdb','create table account (userid int auto_increment,username str not null unique,account_amount float,account_status str)')
db.sqlapi('atmdb','insert into account values \(\'\',wang1,15000.00,open   \)')

print(db.sqlapi('atmdb','select * from account'))

