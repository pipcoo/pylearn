#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

def append_list(file,read_count,rflag):     #将文件内容转换成列表 file传如打开的文件 read_count 传如当前已读取的位置 rflag 记录是否第一次读取到 backend 字段
    read_flag = rflag
    file2list = []
    for line in file:
        read_count+=len(line)
        if len(line)>1:                     #判断读取的字段是否有数据 忽略 回车 换行符等
            line2list=line.replace("\r\n"," ").split()
            if line2list[0]=='backend' and read_flag:
                read_count-=len(line)
                file.seek(read_count)       #如果没第一次读取 backend 字段 则直接退出 设置标志位 减掉当前已读取的行
                read_flag=False             #设置第一次读取 backend 字段为假
                break
            elif line2list[0]=='backend' and not read_flag:
                file2list.append(line)      #不是第一次读取 到 backend 字段 则添加到列表中
                read_flag = True
            else:
                file2list.append(line)
    return file2list,read_count,read_flag

def read_cfg_file():

    f=open("haproxy.cfg","r",encoding="utf-8")
    read_count=0
    filesize=0
    for read in f:              #获取文件总长度
        filesize+=len(read)
    f.seek(0)                   #重置读取位置
    backend_list=[]
    exit_flag=False
    rflag = True                #是否读取过beckend字段标示
    while not exit_flag :
        list1, read_count,rflag = append_list(f, read_count,rflag)
        backend_list.append(list1)
        if read_count ==filesize:
            exit_flag=True      #读取到文件结尾 则退出循环
    f.close()
    return backend_list


def list2dict(_inlist):
    backend={}
    record={}
    server=''
    for i in range(len(_inlist)):
        list1 = _inlist[i].split()

        if list1[0]=='backend':
            backend['backend']=list1[1]
        elif list1[0]=='server':
            index_of_weight=list1.index('weight')
            index_of_maxconn=list1.index('maxconn')
            record['server']=",".join(list1[1:index_of_weight])
            record['weight']=int(list1[index_of_weight+1])
            record['maxconn']=int(list1[index_of_maxconn+1])
    backend['record']=record
    return backend

def display1():
    print('\t1、查询 \n \t2、添加 \n \t3、修改 \n \t4、删除 \n \t键入【q】 退出')
    __input=input(">>")
    return __input

if __name__== '__main__':
    backendset=[]
    list_of_file = read_cfg_file()
    for i in range(1,len(list_of_file)):
        backendset.append(list2dict(list_of_file[i]))


    print(type(display1()))
    print(display1())


