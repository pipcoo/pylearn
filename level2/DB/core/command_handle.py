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
from . import dbfile_handle,key_handle

def check_dbuse_tabname(current_database,command_key,command):
    """
    检查表名是否存在
    :param current_database: 
    :param command_key: 
    :param command: 
    :return: 
    """

    tabname = key_handle.get_tablename(command_key, command)
    if current_database == '':
        print('请选择当前数据库~')
        return ''
    elif current_database != '' and tabname not in dbfile_handle.get_tables(current_database):
        print('表 %s 不存在' % (tabname))
        return ''
    else:
        return tabname

def _show(command,current_database=''):
    """
    处理 show table  show database 命令
    :param command: 
    :param current_database: 
    :return: 
    """

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
    """
    处理 select查询
    :param command: 
    :param current_database: 
    :return: 
    """

    tabname = check_dbuse_tabname(current_database,'select',command)
    if tabname != '':
        if re.match('select\s+(\*|.+)\s+from\s+\w+\.*',command) and 'where' not in command:
            dbfile_handle.print_result(current_database, tabname,
                             dbfile_handle.select_table(current_database, tabname)[0],
                             key_handle.get_colname(current_database, tabname,command))
            return dbfile_handle.select_api_return(current_database, tabname,
                             dbfile_handle.select_table(current_database, tabname)[0],
                             key_handle.get_colname(current_database, tabname,command))

        elif re.match('select\s+(\*|.+)\s+from\s+\w+\s+where\.*',command):
            dbfile_handle.print_result(current_database, tabname,
                             dbfile_handle.select_table(current_database, tabname,
                             key_handle.get_where_key(current_database, tabname,command))[0],
                             key_handle.get_colname(current_database, tabname,command))
            return dbfile_handle.select_api_return(current_database, tabname,
                             dbfile_handle.select_table(current_database, tabname,
                             key_handle.get_where_key(current_database, tabname,command))[0],
                             key_handle.get_colname(current_database, tabname,command))
        else:
            print('语法错误！~')
            return None

def _insert_value_handle(current_database,tabname,insert_value_list):
    """
    处理insert 插入操作的 插入值处理
    :param current_database: 
    :param tabname: 
    :param insert_value_list: 
    :return: 
    """
    tabdata = dbfile_handle.read_tbf(current_database, tabname)
    columns = tabdata['columns']
    columns_list = dbfile_handle.columns_handle(columns)
    not_null_col = tabdata['not_null_col']
    auto_add_col = tabdata['auto_add_col']
    cur_auto_add_num = tabdata['cur_auto_add_num']
    insert_command = {}


    if len(insert_value_list) != len(columns_list):
        print('插入的值数量不符')
    else:
        for i in columns_list:

            if dbfile_handle.columns_handle(columns, i)[0] == 'int' and insert_value_list[columns_list.index(i)] != '':
                i_val = int(insert_value_list[columns_list.index(i)])
            elif dbfile_handle.columns_handle(columns, i)[0] == 'int' and insert_value_list[columns_list.index(i)] == '':
                i_val = None
            else:
                i_val = str(insert_value_list[columns_list.index(i)])

            if not_null_col.count(i) > 0 and i_val != '' and i != auto_add_col:
                insert_command[i] = i_val
            elif not_null_col.count(i) > 0 and (i_val == '' or i_val == None) and i != auto_add_col:
                print('列 %s 不能为空~'%(i))
                break
            elif i == auto_add_col and i_val != None:
                print('列 %s 是自增列 不能赋值~'%(i))
                break
            elif i == auto_add_col and i_val == None:
                insert_command[i] = cur_auto_add_num + 1
            elif i != auto_add_col and not_null_col.count(i) == 0:
                insert_command[i] = i_val
        else:
            dbfile_handle.insert_table(current_database,tabname,insert_command)

def _insert(command,current_database):
    """
    处理 insert 命令
    :param command: 
    :param current_database: 
    :return: 
    """

    tabname = check_dbuse_tabname(current_database, 'insert', command)

    if tabname != '':
        tabdata = dbfile_handle.read_tbf(current_database, tabname)
        columns = tabdata['columns']

        columns_list = dbfile_handle.columns_handle(columns)


        if re.match('insert\s+into+\s+\w+\s+values\s+\(.+\)',command):
            value_list = command.split('values')[1].replace('\'', '').replace('\"', '').rstrip().lstrip()[1:-1].split(',')
            _insert_value_handle(current_database,tabname,value_list)

        elif re.match('insert\s+into+\s+\w+\s+\(.*\)\s+values\s+\(.*\)',command):

            insert_col= re.search('\(.+\)',command.split('values')[0].replace('\'','').replace('\"','')) .group().rstrip().lstrip()[1:-1].split(',')
            value_list = command.split('values')[1].replace('\'', '').replace('\"', '').rstrip().lstrip()[1:-1].split(',')
            new_value_list = []
            for insert_col_name in insert_col:
                if not dbfile_handle.check_colname(current_database, tabname,insert_col_name)[0]:
                    print('要插入的列不存在')
                    break
            else:
                if len(value_list) != len(insert_col):
                    print('插入的值数量不符')
                else:
                    for i in columns_list :
                        if insert_col.count(i)>0:
                            new_value_list.append(value_list[insert_col.index(i)])
                        else:
                            new_value_list.append('')
                    _insert_value_handle(current_database, tabname, new_value_list)
        else:
            print('语法错误！~')


def _update(command,current_database=''):
    """
    处理update 命令
    :param command: 
    :param current_database: 
    :return: 
    """

    tabname = check_dbuse_tabname(current_database, 'update', command)
    if tabname != '':
        if re.match('update\s+\w+\s+set\s+\w+\s*=\s*.+',command) and 'where' not in command:
            set_value = key_handle._update_set_key_handle(command)
            if dbfile_handle.check_colname(current_database,tabname,set_value[0])[0]:
                update_count = dbfile_handle.update_table(current_database,tabname,set_value)
                print ('%d row updated'%(update_count))
            else:
                print('更新的列 %s 不在表 %s 中'%(set_value[0],tabname))
        elif re.match('update\s+\w+\s+set\s+\w+\s*=\s*\w+\s+where.+', command):
            set_value = key_handle._update_set_key_handle(command)
            if dbfile_handle.check_colname(current_database, tabname, set_value[0])[0]:
                update_count = dbfile_handle.update_table(current_database, tabname,set_value,
                                                          key_handle.get_where_key(current_database, tabname, command))
                print('%d row updated' % (update_count))
            else:
                print('更新的列 %s 不在表 %s 中' % (set_value[0], tabname))
        else:
            print('语法错误！~')

def _drop(command,current_database=''):
    """
    处理 drop table or drop database 命令
    
    :param command: 
    :param current_database: 
    :return: 
    """


    if re.match('drop\s+table+\s+\w+',command):
        tabname = check_dbuse_tabname(current_database, 'drop', command)
        if tabname != '':
            dbfile_handle.drop_table(current_database, tabname)
    elif re.match('drop\s+database+\s+\w+',command):
        dbfile_handle.drop_databases(current_database)
    else:
        print('语法错误！~')


def _delete(command,current_database):
    """
    处理delete 删除数据 命令
    
    :param command: 
    :param current_database: 
    :return: 
    """

    tabname = check_dbuse_tabname(current_database, 'delete', command)
    if tabname != '':
        if re.match('delete\s+from\s+\w+',command) and 'where' not in command:
            delete_count = dbfile_handle.delete_table(current_database, tabname)
            print('%d row deleted' % (delete_count))
        elif re.match('delete\s+from\s+\w+\s+where\s+.+',command):
            delete_count = dbfile_handle.delete_table(current_database, tabname,
                                       key_handle.get_where_key(current_database, tabname, command))
            print('%d row deleted' % (delete_count))
        else:
            print('语法错误！~')


def _create(command,current_database=''):
    """
    处理 create table  or create database 命令
    :param command: 
    :param current_database: 
    :return: 
    """

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
    """
    处理 use 命令 返回当前选择的数据库
    :param command: 
    :return: 
    """

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




#dbfile_handle.print_result('emp', 'staff_table', dbfile_handle.select_table('emp', 'staff_table')[0], key_handle.get_colname('emp', 'staff_table','select * from staff_table'))