#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

'''
HAproxy配置文件操作：
1. 根据用户输入输出对应的backend下的server信息
2. 可添加backend 和sever信息
3. 可修改backend 和sever信息
4. 可删除backend 和sever信息
5. 操作配置文件前进行备份
6. 添加server信息时，如果ip已经存在则修改;如果backend不存在则创建；若信息与已有信息重复则不操作
配置文件 参考 http://www.cnblogs.com/alex3714/articles/5717620.html
'''
import time

"""
append_list 函数接受传入的打开文件实例 读取文件内容
遇到 backend 关键字 就返回一个列表 病返回当前读取的位置 以及 是否存储过backend 信息
"""

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

"""
read_cfg_file 函数负责读取配置文件 抓取文件中的backend信息 返回一个所有backend信息的列表
"""

def read_cfg_file():

    f=open("haproxy.cfg","r",encoding="utf-8")
    read_count=0
    filesize=0
    for read in f:                          #获取文件总长度
        filesize+=len(read)
    f.seek(0)                               #重置读取位置到开始
    backend_list=[]
    exit_flag=False
    rflag = True                            #是否读取过beckend字段标示
    while not exit_flag :
        list1, read_count,rflag = append_list(f, read_count,rflag)
        backend_list.append(list1)
        if read_count >= filesize:
            exit_flag=True                  #读取到文件结尾 则退出循环
    f.close()
    return backend_list

"""
list2dict 负责将传入的bachend 列表格式转换成 字典格式
"""
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

"""
display1 登录打印菜单信息 获取用户输入选择的菜单
         判断输入是否有效 有效返回用户选择的编号信息
"""

def display1():
    while True:
        print('\t1、查询 \n \t2、添加 \n \t3、修改 \n \t4、删除 \n \t键入【q】 退出')
        __input=input(">>")
        if __input in ('1','2','3','4','q'):
            break
        else:
            print('\n 编号输入错误 请重新输入 \n')
    return __input

"""
backend_select 处理用户 查询backend的 功能
"""
def backend_select(backendset):
    exit_flag = False
    while not exit_flag:
        __backend_input=input('输入要查询的backend 域名 【按q退出】\n>>')
        for i in range(len(backendset)):
            if backendset[i]['backend'] == __backend_input:
                print("\nbackend: %s " %(__backend_input))
                print("server: %s weight: %d maxconn: %d \r\n" % (backendset[i]['record']['server'],backendset[i]['record']['weight'],backendset[i]['record']['maxconn']))
                break
            elif 'q' == __backend_input:
                exit_flag=True
        else:
            print('您输入的backend信息未找到')

"""
backend_add 处理用户 添加backend的 功能
"""


def backend_add(backendset):
    exit_flag = False
    bak_flag = False
    while not exit_flag:
        __backend_input = input('输入要添加的backend 信息 【按q退出】\n>>')
        if __backend_input == 'q':
            exit_flag=True
        elif '=' in __backend_input:                                      #判断用户输入是否包含 = 关键字
            __backend_add = eval(__backend_input.split('=')[1])         #以 = 分割 将=后信息转换为字典格式
            if __backend_add.get('backend') and __backend_add.get('record','server') and __backend_add.get('record','weight') and __backend_add.get('record','maxconn'):
                                                                        #判断用户输入的信息是否符合要存入的格式
                for i in range(len(backendset)):                        #遍历列表 查抄用户输入的backend 信息是否已经存在
                    if backendset[i]['backend'] == __backend_add['backend']:
                        print("你输入的backend信息已经存在，如需修改请选择 3")
                        break
                else:                                                   #信息不存在 插入输入信息
                    backendset.append(__backend_add)
                    bak_flag = True
                    exit_flag = True
                    break
            else:
                print("输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
        else:
            print("输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
    return backendset,bak_flag

"""
backend_del 处理用户 删除backend的 功能
"""

def backend_del(backendset):
    exit_flag = False
    bak_flag = False
    while not exit_flag:
        __backend_input = input('输入要删除的backend 信息 【按q退出】\n>>')
        if __backend_input == 'q':
            exit_flag=True
        elif '=' in __backend_input:                                    # 判断用户输入是否包含 = 关键字
            __backend_del = eval(__backend_input.split('=')[1])         # 以 = 分割 将=后信息转换为字典格式
            if __backend_del.get('backend') and __backend_del.get('record', 'server') and __backend_del.get('record', 'weight') and __backend_del.get('record', 'maxconn'):
                                                                        # 判断用户输入的信息是否符合要存入的格式
                for i in range(len(backendset)):                        # 遍历列表 查抄用户输入的backend 信息是否已经存在
                    print(backendset[i])
                    if backendset[i]==__backend_del:
                        backendset.pop(i)
                        bak_flag = True
                        exit_flag = True
                        break
                else:                                                   # 信息不存在 插入输入信息
                    print("你输入的backend信息不存在或不完全匹配，请核对backend信息")
                    break
            else:
                print(
                    "输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
        else:
            print(
                "输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
    return backendset,bak_flag

"""
backend_modify 处理用户 修改backend的 功能
"""

def backend_modify(backendset):
    exit_flag = False
    bak_flag=False
    while not exit_flag:
        __backend_input = input('输入要修改的backend 信息 【按q退出】\n>>')
        if __backend_input == 'q':
            exit_flag=True
        elif '=' in __backend_input:  # 判断用户输入是否包含 = 关键字
            __backend_mod = eval(__backend_input.split('=')[1])  # 以 = 分割 将=后信息转换为字典格式
            if __backend_mod.get('backend') and __backend_mod.get('record', 'server') and __backend_mod.get('record', 'weight') and __backend_mod.get('record', 'maxconn'):
                # 判断用户输入的信息是否符合要存入的格式
                for i in range(len(backendset)):  # 遍历列表 查抄用户输入的backend 信息是否已经存在
                    if backendset[i]['backend'] == __backend_mod['backend']:
                        backendset[i]['record']['server'] = __backend_mod['record']['server']
                        backendset[i]['record']['weight'] = __backend_mod['record']['weight']
                        backendset[i]['record']['maxconn'] = __backend_mod['record']['maxconn']
                        bak_flag=True
                        exit_flag = True
                        break
                else:  # 信息不存在 插入输入信息
                    print("你输入的backend信息不存在，如需添加请选择2")
                    break
            else:
                print(
                    "输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
        else:
            print(
                "输入的格式有误！请重新输入。注意格式为：\r\n args={'backend':'xxx.xxx.xxx','record':{'server':'x.x.x.x','weight':xx,'maxconn':xx}}")
    return backendset,bak_flag

"""
file_save 处理 最终保存文件功能
"""

def file_save(globalset,backendset):

    f=open("2.cfg","w",encoding="utf-8")
    for g in range(len(globalset)):             #遍历公共参数部分 写入文件
        f.write(globalset[g])

    for b in range(len(backendset)):            #遍历backend列表部分 写入文件
        backend_info = "backend "+ backendset[b]['backend']
        server_info = "        server "+ backendset[b]['record']['server']+" weight "+ str(backendset[b]['record']['weight']) + " maxconn "+  str(backendset[b]['record']['maxconn'])
        f.write("\n")
        f.write(backend_info)
        f.write("\n")
        f.write(server_info)
        f.write("\n")

    f.close()

"""
create_bakfile 处理创建备份
"""
def create_bakfile():
    config_file = "haproxy.cfg"
    bak_file = "haproxy.cfg_"+time.strftime('%Y%m%d%H%M')
    print (bak_file)
    f1 = open(config_file, "r", encoding="utf=8")
    f2 = open(bak_file, "w", encoding="utf=8")
    for line in f1.readlines():
        f2.write(line)
    f2.flush()
    f1.close()
    f2.close()



"""
入口函数
"""

if __name__== '__main__':
    backendset=[]
    list_of_file = read_cfg_file()
    for i in range(1,len(list_of_file)):
         backendset.append(list2dict(list_of_file[i]))
    print(backendset)
    exit_flag=False

    while not exit_flag:
        __menu_input=display1()
        if __menu_input == '1':
            backend_select(backendset)
        elif __menu_input == '2':
            backendset,bak_flag = backend_add(backendset)
            if bak_flag:
                create_bakfile()
                file_save(list_of_file[0],backendset)
        elif __menu_input == '3':
            backendset,bak_flag = backend_modify(backendset)
            if bak_flag:
                create_bakfile()
                file_save(list_of_file[0],backendset)
        elif __menu_input == '4':
            backendset,bak_flag = backend_del(backendset)
            if bak_flag:
                create_bakfile()
                file_save(list_of_file[0],backendset)
        elif __menu_input == 'q':
            exit_flag = True




