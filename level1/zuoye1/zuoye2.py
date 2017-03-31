#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

'''
1. 运行程序输出第一级菜单
2. 选择一级菜单某项，输出二级菜单，同理输出三级菜单
3. 菜单数据保存在文件中
4. 让用户选择是否要退出
5. 有返回上一级菜单的功能
评分标准：
用多层嵌套while循环的方式完成作业2，85分
只用一层循环完成作业2，100分
'''

f=open("menu.txt","r",encoding="utf-8")
menu=''
for line in f:
    menu+=line.strip()          #遍历读取文件 整合成1行
f.close()
menu=eval(menu)                 #将整合的文件转换为字典格式
exit_flag=True
current_menu=[]                 #初始化一个列表存储当前所在目录下的字典，

while exit_flag:

    for key in menu:
        print(key)

    __input=input("please input your choose【enter q to exit,enter b to back uplevel】 :")

    if __input=='q' or __input=='Q':
        exit_flag=False
        break

    if __input=='b':
        menu=current_menu[-1]       #如果选择返回上级 则取 当前列表的最后插入的一个元素
        current_menu.pop()          #赋值后 将最后一个元素从列表移出
    else:
        current_menu.append(menu)   #如果进入下一级 将当前一级存入列表
        menu=menu[__input]          #当前目录 为所选择 key下的字典



