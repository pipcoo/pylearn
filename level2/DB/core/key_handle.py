#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: key_handle.py
@time: 2017/4/9 22:56
"""

from . import dbfile_handle


def check_tabname(tabname):
    db = dbf_manager.dbf_load()
    if tabname in db[tablelist]:
        return True
    else:
        return False


def get_tablename(command_key,command):
    command_list = command.split(' ')
    if command_key == 'select':
        tablename = command_list[command_list.index('from') + 1]
    elif command_key == 'insert':
        tablename = command_list[command_list.index('into') + 1]
    elif command_key == 'update':
        tablename = command_list[command_list.index('update') + 1]
    elif command_key == 'delete':
        tablename = command_list[command_list.index('from') + 1]
    elif command_key == 'drop':
        tablename = command_list[command_list.index('table') + 1]
    return tablename

def get_colname(current_database,tabname,command):
    """
    获取需要查询的列
    :param command: 
    :return: 
    """
    colsname=[]
    command_list = command.split(' ')
    cols = command_list[command_list.index('from') - 1]
    tablename = command_list[command_list.index('from') + 1]
    if cols == '*':
        tabdata = dbfile_handle.read_tbf(current_database, tabname)
        columns = tabdata['columns']
        for dict in columns:
            for k in dict:
                colsname.append(k)
    else:
        colsname = cols.split(',')

    return colsname

#print(get_colname('emp','staff_table','select * from staff_table'))

def judge_key_split(current_database,tabname,in_wkey,judge_key):
    """
    处理条件判断分隔符 
    :param current_database:
    :param tabname: 
    :param in_wkey: 一组where条件
    :param judge_key: 判断符
    :return: 返回 包含 列名，判断条件，值 在内的一个列表 
    """
    wkey = []
    wkey_list = in_wkey.split(judge_key)
    wkey_colname = wkey_list[0].replace(' ','')
    colname_check_result = dbfile_handle.check_colname(current_database,tabname,wkey_colname)
    if colname_check_result[0]:
        wkey.append(wkey_colname)
        wkey.append(judge_key)
        if colname_check_result[1] == 'int':
            wkey_value = int(wkey_list[1].replace(' ', '').replace('\'', '').replace('\"', ''))
            wkey.append(wkey_value)
        else:
            wkey_value = str(wkey_list[1].replace(' ', '').replace('\'', '').replace('\"', ''))
            wkey.append(wkey_value)
        return wkey
    else:
        print('列不存在',in_wkey)
        return False

def get_where_key(current_database,tabname,command):
    """
    获取where条件 
    :param current_database: 
    :param tabname: 
    :param command: 
    :return: 返回包含 所有where条件的列表 eg：[[x],[x],...]
    """
    where_key = []
    command_list = command.split('where')
    where_list  = command_list[1].replace(' ','').split('and')
    for i in where_list:
            if '=' in i and '>' not in i and '<' not in i:
                if  judge_key_split(current_database,tabname,i,'='):
                    where_key.append(judge_key_split(current_database,tabname,i,'='))
                else:
                    break
            elif '>' in i and '=' not in i and '<' not in i:
                if  judge_key_split(current_database,tabname,i,'>'):
                    where_key.append(judge_key_split(current_database,tabname,i,'>'))
                else:
                    break
            elif '<' in i and '=' not in i and '>' not in i:
                if  judge_key_split(current_database,tabname,i,'<'):
                    where_key.append(judge_key_split(current_database,tabname,i,'<'))
                else:
                    break
            elif '<>' in i and '=' not in i :
                if  judge_key_split(current_database,tabname,i,'<>'):
                    where_key.append(judge_key_split(current_database,tabname,i,'<>'))
                else:
                    break
            elif '<=' in i :
                if  judge_key_split(current_database,tabname,i,'<='):
                    where_key.append(judge_key_split(current_database,tabname,i,'<='))
                else:
                    break
            elif '>=' in i :
                if  judge_key_split(current_database,tabname,i,'>='):
                    where_key.append(judge_key_split(current_database,tabname,i,'>='))
                else:
                    break
            elif 'like' in i:
                if  judge_key_split(current_database,tabname,i,'like'):
                    where_key.append(judge_key_split(current_database,tabname,i,'like'))
                else:
                    break
            else:
                print('where 条件输入错误！')
                break
    else:
        return where_key


def _update_set_key_handle(command):
    set_value = []
    set_value.append(command.split('=')[0].rstrip().split(' ')[-1])
    set_value.append(command.split('=')[1].lstrip().split(' ')[0])
    return set_value

# a= "select * from staff_table where staff_id = 1 and phone like '133'"
# print (get_where_key('emp','staff_table',a))