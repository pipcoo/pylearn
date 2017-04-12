#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: dbfile_handle.py
@time: 2017/4/12 23:02
"""

import os,sys,re,json

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def get_databases():
    databases = []
    databases_dir = os.listdir(BASE+'/data')
    for i in databases_dir:
        if os.path.isdir(BASE+'/data/'+i):
            databases.append(i)
    return databases

def get_tables(current_database):
    tabnames = []
    tables_dir = os.listdir(BASE+'/data/'+current_database+'/')
    for i in tables_dir:
        if os.path.isfile(BASE+'/data/'+current_database+'/'+i):
            if re.match('.+\.tbf\Z',i):
                tabnames.append(i[0:-4])
    return tabnames


def create_database(database_name):
    if not os.path.exists(BASE+'/data/'+database_name):
        os.mkdir(BASE+'/data/'+database_name)
    else:
        print("数据库已存在！~")


def create_table(current_database,create_command):
    table_create_template = {
    'columns':[],
    'table_data':[],
    'not_null_col':[],
    'auto_add_col':'',
    'cur_auto_add_num':0
}
    columns=[]
    not_null_col=[]
    auto_add_col=''
    columns_info={}
    # create table emp （id int,name str)
    if re.match('create\s+table\s+.+\s+\(.*\)\Z',create_command):
        tabname = create_command.split(' ')[2]
        colname = re.search('\(.+\)',create_command).group()[1:-1].split(',')
        for i in colname:
            attr = i.split(' ')
            columns_name = attr[0]
            columns_attr = attr[1]
            if attr.count('not') > 0 :
                if attr[attr.index('not')+1] == 'null':
                    not_null_col.append(columns_name)
                else:
                    print('关键字语法错误！')
            elif  attr.count('auto_increment') > 1 and auto_add_col == '':
                auto_add_col = columns_name
            elif  attr.count('auto_increment') > 1 and auto_add_col != '':
                print('一个表只能有一个自增列！')
            columns_info[columns_name]=columns_attr
            columns.append(columns_info)
            columns_info={}

        table_create_template['columns'] = columns
        table_create_template['not_null_col'] = not_null_col
        table_create_template['auto_add_col'] = columns_name

        if os.path.isfile(BASE+'/data/'+current_database+'/'+tabname+'.tbf'):
            print('表%s已存在！'%tabname)
        else:

            f = open(BASE+'/data/'+current_database+'/'+tabname+'.tbf',"w",encoding="utf-8")
            f.write(json.dumps(table_create_template))
            f.close()
    else:
        print('语法错误！')



def drop_table(current_database,tabname):
    if os.path.exists(BASE+'/data/'+current_database+'/'+tabname+'.tbf'):
        os.remove(BASE+'/data/'+current_database+'/'+tabname+'.tbf')
        print("%s已删除"%tabname)
    else:
        print("表不存在！~")


def drop_databases(database_name):
    if os.path.isdir(BASE+'/data/'+database_name):
        os.removedirs(BASE+'/data/'+database_name)
        print("数据库%s已删除！~"%database_name)
    else:
        print("数据库%s不存在！~" %database_name)


create_table('emp','create table emp (id int not null auto_increment ,name str)')
