#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

'''
购物车程序：
1、启动程序后，输入用户名密码后，如果是第一次登录，让用户输入工资，然后打印商品列表
2、允许用户根据商品编号购买商品
3、用户选择商品后，检测余额是否够，够就直接扣款，不够就提醒
4、可随时退出，退出时，打印已购买商品和余额
5、在用户使用过程中， 关键输出，如余额，商品已加入购物车等消息，需高亮显示
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
'''

def read_of_file():
    f=open("account.txt","r",encoding="utf-8")
    menu=''
    for line in f:
        menu+=line.strip()
    f.close()
    return eval(menu)

def login(username,password):
    if username in __account:
        if password == __account[username]['password']:
            return True
        else:
            return False
    else:
        return False

def first_login_check(username):
    if __account[username]['salary'] == '':
        return True
    else:
        return False

def set_user_salary(username,salary):
    __account[username]['salary']=salary
    return  __account

def print_commodity():
    for keys in __commodity:
        print(keys,__commodity[keys][0],"¥",__commodity[keys][1])

def save_to_file(account,commodity):
    __db['account']=__account['account']
    __db['commodity']=__commodity['commodity']
    f=open("account.txt","w",encoding="utf-8")
    f.write(__db)
    f.close()

f=read_of_file()
__commodity=f['commodity']
__account=f['account']
shopping_flag=True

while shopping_flag:
    username=input('please input your username:')
    password=input('please input your password:')
    if login(username,password):
        if first_login_check(username):
            salary=int(input('please input your salary:'))
            set_user_salary(username,salary)
        while shopping_flag:
            print_commodity()
            __input=input('please input your choose commodity No.[pass q to exit]\n >>')
            if __input == 'q':
                shopping_flag=False
    else:
        print("Wrong username or password.")

