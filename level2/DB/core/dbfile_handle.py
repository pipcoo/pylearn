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

import os,sys,re,json,types

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def io_path(current_database='',tabname=''):
    """
    数据库 、 表 文件存储路径处理 
    :param current_database: 
    :param tabname: 
    :return: 返回需要的路径
    """
    if current_database != '' and tabname == '':
        return BASE+'/data/'+current_database+'/'
    elif current_database != '' and tabname != '':
        return BASE+'/data/'+current_database+'/'+tabname+'.tbf'
    elif current_database == '' and tabname == '':
        return BASE+'/data/'

def get_databases():
    """
    获取已存在的数据库文件夹
    :return: 
    """
    databases = []
    databases_dir = os.listdir(io_path())
    for i in databases_dir:
        if os.path.isdir(io_path()+i):
            databases.append(i)
    return databases

def get_tables(current_database):
    """
    获取数据库路径下的所有表
    :param current_database: 
    :return: 
    """
    tabnames = []
    tables_dir = os.listdir(io_path(current_database))
    for i in tables_dir:
        if os.path.isfile(io_path(current_database)+i):
            if re.match('.+\.tbf\Z',i):
                tabnames.append(i[0:-4])
    return tabnames


def create_database(database_name):
    """
    创建数据库
    :param database_name: 
    :return: 
    """
    if not os.path.exists(io_path(database_name)):
        os.mkdir(io_path(database_name))
        print("数据库%s创建成功！~" % database_name)
    else:
        print("数据库已存在！~")


def create_table(current_database,create_command):
    """
    创建表
    :param current_database:   数据库名
    :param create_command:     剪标语句
    :return: 
    """
    table_create_template = {
    'columns':[],
    'table_data':[],
    'not_null_col':[],
    'auto_add_col':'',
    'unique':[],
    'cur_auto_add_num':0,
    'create_tab_ddl':''
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
            if  attr.count('auto_increment') > 0 and auto_add_col == '':
                auto_add_col = columns_name
            elif  attr.count('auto_increment') > 0 and auto_add_col != '':
                print('一个表只能有一个自增列！')
            columns_info[columns_name]=columns_attr
            columns.append(columns_info)
            columns_info={}

        table_create_template['columns'] = columns
        table_create_template['not_null_col'] = not_null_col
        table_create_template['auto_add_col'] = auto_add_col
        table_create_template['create_tab_ddl'] = create_command

        if os.path.isfile(io_path(current_database,tabname)):
            print('表%s已存在！'%tabname)
        else:
            write_tbf(current_database,tabname,table_create_template)

    else:
        print('语法错误！')

def read_tbf(current_database,tabname):
    f = open (io_path(current_database,tabname),"r",encoding="utf-8")
    tabdata = json.load(f)
    f.close()
    return tabdata

def write_tbf(current_database,tabname,tabdata):
    f = open(io_path(current_database,tabname),"w",encoding="utf-8")
    f.write(json.dumps(tabdata))
    f.close()

def check_types(check_data,_type):
    if _type ==  'int':
        if isinstance(check_data,int):
            return True
        else:
            return False
    elif _type == 'str':
        if isinstance(check_data,str):
            return True
        else:
            return False


def insert_table(current_database,tabname,values):
    """
    插入表
    :param current_database: 
    :param tabname: 
    :param values:  字典格式
    :return: 
    """
    tabdata = read_tbf(current_database,tabname)
    coldata = []
    columns = tabdata['columns']
    check_result =True
    if len(values) == len(columns):
        for dict in columns:
            for k in dict:
                if check_types(values[k],dict[k]) :
                    coldata.append(values[k])
                else:
                    print('插入数据格式不匹配!')
    else:
        print('要插入的值不够！')
    print(coldata)
    if check_result:
        tabdata['table_data'].append(coldata)
        write_tbf(current_database, tabname, tabdata)


def delete_table(current_database,tabname,where_key):
    pass #todo

def update_table(current_database):
    pass #todo

def select_table(current_database,tabname,where_key):
    tabdata = read_tbf(current_database, tabname)
    data = tabdata['table_data']
    columns = tabdata['columns']
    for i in 



def drop_table(current_database,tabname):
    """
    删除表
    :param current_database: 
    :param tabname: 
    :return: 
    """
    if os.path.exists(io_path(current_database,tabname)):
        os.remove(io_path(current_database,tabname))
        print("%s已删除"%tabname)
    else:
        print("表不存在！~")


def drop_databases(database_name):
    """
    删除数据库
    :param database_name: 
    :return: 
    """
    if os.path.isdir(io_path(database_name)):
        os.removedirs(io_path(database_name))
        print("数据库%s已删除！~"%database_name)
    else:
        print("数据库%s不存在！~" %database_name)

#drop_table('emp','staff_table')
#create_table('emp','create table staff_table (staff_id int not null auto_increment,name str,age int ,phone str ,dept str,enroll_date str )')

# print (get_databases())
#
# create_database('emp2')
#
# drop_databases('emp2')


insert_table('emp','staff_table',{"staff_id": 1,"name": "lala","age": 12,"phone": "13333333333","dept": "it","enroll_date": "2013-03-01"})
