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

import os,re,json

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
            print('表%s创建成功！' % tabname)

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




def make_insert_command(current_database,tabname,):
    pass


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
        print('要插入值的数量不符！')
    #print(coldata)
    if check_result:
        tabdata['table_data'].append([len(tabdata['table_data']),coldata])
        write_tbf(current_database, tabname, tabdata)


def delete_table(current_database,tabname,where_key=''):
    delete_count = 0
    delete_list = select_table(current_database,tabname,where_key)[1]
    tabdata = read_tbf(current_database, tabname)
    data = tabdata['table_data']
    keep_data =[]
    for row in data:
        if row[0] in delete_list:
            delete_count+=1
        else:
            keep_data.append(row)
    tabdata['table_data'] = keep_data
    if delete_count > 0 :
        write_tbf(current_database, tabname, tabdata)
        return delete_count
    else:
        return delete_count

def update_table(current_database,tabname,set_value,where_key=''):
    update_list = select_table(current_database, tabname, where_key)[1]
    tabdata = read_tbf(current_database, tabname)
    columns = tabdata['columns']
    data = tabdata['table_data']
    set_value_index = columns_handle(columns,set_value[0])[1]
    updated_count = 0
    result_date =[]
    for row in data:
        if row[0] in update_list:
            row[1][set_value_index]=set_value[1]
            result_date.append(row)
            updated_count+=1
        else:
            result_date.append(row)
    tabdata['table_data'] = result_date
    if updated_count > 0 :
        write_tbf(current_database, tabname, tabdata)
        return updated_count
    else:
        return updated_count


def columns_handle(columns,col_name):
    for dict in columns:
        for k in dict:
            if k == col_name:
                return dict[k],columns.index(dict)

def check_colname(current_database,tabname,check_colname):
    """
    检查列名是否存在 
    :param current_database: 
    :param tabname: 
    :param check_colname: 
    :return: 存在返回 True 列类型 列索引 不存在返回False
    """
    tabdata = read_tbf(current_database, tabname)
    columns = tabdata['columns']
    columns_all = []
    for dict in columns:
        for k in dict:
            columns_all.append(k)
    if check_colname in columns_all:
        columns_type = columns_handle(columns,check_colname)[0]
        colunms_index = columns_handle(columns,check_colname)[1]
        return True,columns_type,colunms_index
    else:
        return False, '', ''


def row_handle(data,col_index,_judge,judge_key):
    result_data = []
    result_index = []
    for row in data:
        if _judge == '>':
            if row[1][col_index] > judge_key:
                result_data.append(row)
                result_index.append(row[0])
        elif _judge == '=':
            if row[1][col_index] == judge_key:
                result_data.append(row)
                result_index.append(row[0])
        elif _judge == '<':
            if row[1][col_index] < judge_key:
                result_data.append(row)
                result_index.append(row[0])
        elif _judge == '<=':
            if row[1][col_index] <= judge_key:
                result_data.append(row)
                result_index.append(row[0])
        elif _judge == '>=':
            if row[1][col_index] >= judge_key:
                result_data.append(row)
                result_index.append(row[0])
        elif _judge == 'like':
            if re.search(judge_key,row[1][col_index]):
                result_data.append(row)
                result_index.append(row[0])
        else:
            print('条件输入错误！')
            break
    else:
        return result_data,result_index

def key_handle(data,where_key_index,surplus_row_index=[]):

    if len(where_key_index) > 0:
        current_handle = where_key_index.pop()
        surplus = row_handle(data,current_handle[0],current_handle[1],current_handle[2])
        surplus_row = surplus[0]
        surplus_row_index=surplus[1]
        return key_handle(surplus_row,where_key_index,surplus_row_index)
    else:
        return data,surplus_row_index

def select_table(current_database,tabname,where_key=''):
    """
    查询表 没有where条件则全部输出 有where条件进行筛选
    :param current_database: 当前数据库 名
    :param tabname: 当前表名
    :param where_key: where条件 列表模式 eg：[['id','>',1],['name','like','wang']]
    :return: 返回数据 和数据的行号
    """
    tabdata = read_tbf(current_database, tabname)
    data = tabdata['table_data']
    columns = tabdata['columns']
    where_key_index=[]
    result_data_index=[]
    if where_key != '':
        for i in where_key:
            i[0]=columns_handle(columns,i[0])[1]
            where_key_index.append(i)
        result = key_handle(data,where_key_index)
        result_data = result[0]
        result_data_index = result[1]
        return result_data,result_data_index
    else:
        for row in data:
            result_data_index.append(row[0])

        return data,result_data_index

def drop_table(current_database,tabname):
    """
    删除表
    :param current_database: 
    :param tabname: 
    :return: 
    """
    if os.path.exists(io_path(current_database,tabname)):
        os.remove(io_path(current_database,tabname))
        print("表%s已删除"%tabname)
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

def print_row(row_list,dis_index):

    dis_row = ''
    for i in row_list:
        if row_list.index(i) in dis_index:
            dis_row += '| %s '%i
    else:
        dis_row += '|'
    print ('-'*len(dis_row))
    print (dis_row)
    return len(dis_row)

def print_result(current_database,tabname,display_list,display_col):
    tabdata = read_tbf(current_database, tabname)
    columns = tabdata['columns']
    display_idx = []
    display_title = ''
    for col_name in display_col:
        display_idx.append(columns_handle(columns,col_name)[1])

    if len(display_list) > 0:
        for d in display_col:
            display_title += '| %s ' % d
        else:
            display_title += '|'
        print('-' * len(display_title))
        print(display_title)

        for i in display_list:
            hnum=print_row(i[1],display_idx)
        else:
            print('-'*hnum)
    print('%d row selected'%(len(display_list)))


#drop_table('emp','staff_table')
#create_table('emp','create table staff_table (staff_id int not null auto_increment,name str,age int ,phone str ,dept str,enroll_date str )')

# print (get_databases())
#
# create_database('emp2')
#
# drop_databases('emp2')


''' 
drop_table('emp','staff_table')
create_table('emp','create table staff_table (staff_id int not null auto_increment,name str,age int ,phone str ,dept str,enroll_date str )')

# a= [{"staff_id": "int"}, {"name": "str"}, {"age": "int"}, {"phone": "str"}, {"dept": "str"}, {"enroll_date": "str"}]
# print(columns_handle(a,'phone'))
#
insert_table('emp','staff_table',{"staff_id": 1,"name": "Alex Li4","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
insert_table('emp','staff_table',{"staff_id": 2,"name": "Alex Li5","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
insert_table('emp','staff_table',{"staff_id": 3,"name": "Alex Li6","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
insert_table('emp','staff_table',{"staff_id": 4,"name": "Alex Li7","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
insert_table('emp','staff_table',{"staff_id": 5,"name": "Alex Li8","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
insert_table('emp','staff_table',{"staff_id": 6,"name": "Alex Li9","age": 22,"phone": "13651054608","dept": "IT","enroll_date": "2013-04-01"})
#print (update_table('emp','staff_table',('phone','1561515615'),[['dept','like','I']]))
#print(select_table('emp','staff_table'))
#print(delete_table('emp','staff_table'))
#print(select_table('emp','staff_table'))
print_result('emp','staff_table',select_table('emp','staff_table',[['staff_id','>',5]])[0],['staff_id','name'])
'''

#print (check_colname('emp','staff_table','phone'))
