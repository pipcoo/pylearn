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
    menu+=line.strip()
f.close()
menu=eval(menu)
exit_flag=True
current_menu=[]

while exit_flag:

    for key in menu:
        print(key)

    __input=input("please input your choose【enter q to exit,enter b to back uplevel】 :")

    if __input=='q' or __input=='Q':
        exit_flag=False
        break

    if __input=='b':
        menu=current_menu[-1]
        current_menu.pop()
    else:
        current_menu.append(menu)
        menu=menu[__input]



