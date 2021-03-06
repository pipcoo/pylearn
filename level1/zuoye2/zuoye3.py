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
6、用户下一次登录后，输入用户名密码，直接回到上次的状态，
   即上次消费的余额什么的还是那些，再次登录可继续购买
7、允许查询之前的消费记录
'''

import time #引入模块用于购物时间的格式化记录

'''read_of_file 功能负责读取文件 返回一个字典类的结构数据'''
def read_of_file():
    f=open("account.txt","r",encoding="utf-8")
    menu=''
    for line in f:
        menu+=line.strip()
    f.close()
    return eval(menu)

'''login 处理登录认证'''
def login(username,password):
    if username in __db[0]:
        if password == __db[0][username]['password']:
            return True
        else:
            return False
    else:
        return False


'''first_login_check 验证是否是第一次登录'''
def first_login_check(username):
    if __db[0][username]['salary'] == '':
        return True
    else:
        return False


'''set_user_salary 设置用户的工资金额'''
def set_user_salary(username,salary):
    __db[0][username]['salary']=salary

'''print_commodity 用来打印库存商品信息'''
def print_commodity():
    for keys in __db[1]:
        print(keys,__db[1][keys][0],"¥",__db[1][keys][1])

'''处理运行后的数据保存'''
def save_to_file():
    r={}
    r['account']=__db[0]
    r['commodity'] = __db[1]
    f=open("account.txt","w",encoding="utf-8")
    f.write(str(r))
    f.close()


'''check_money 处理添加到购物车前 工资是否足够 购买所选商品'''
def check_money(username,commodity_id):
    expense=__db[1][commodity_id][1]
    if len(__db[0][username]['shoppingcart']) > 0 : #购物车不为空 则将未结算的物品价格综合也计算进来
        for i in range(len(__db[0][username]['shoppingcart'])):
            expense+=__db[0][username]['shoppingcart'][i][2]
    if __db[0][username]['salary'] > expense:
        return True
    else:
        return False


'''check_inventory 检查是否有库存 用于用户购买'''
def check_inventory(commodity_id):
    if __db[1][commodity_id][2] > 0:
        return True
    else:
        return False


'''add_commodity 添加用户选择的商品ID到购物车中'''
def add_commodity(username,commodity_id):
    shoppingcart=__db[0][username]['shoppingcart']
    commodity_info=[commodity_id,__db[1][commodity_id][0],__db[1][commodity_id][1],time.strftime('%Y-%m-%d %H:%M:%S')]
    shoppingcart.append(commodity_info)
    __db[0][username]['shoppingcart']=shoppingcart


'''settle_account 用于结算 结算完成后 保存用户数据到文件'''
def settle_account():
    shoppingcart = __db[0][username]['shoppingcart']
    order= __db[0][username]['order']
    for i in range(len(shoppingcart)):
        order.append(shoppingcart[i])
        __db[0][username]['salary']-=shoppingcart[i][2]
        __db[1][shoppingcart[i][0]][2] -=1
        this_time_shopping.append(shoppingcart[i])
    __db[0][username]['order']=order
    __db[0][username]['shoppingcart']=[]
    save_to_file()



'''shopping 购买过程'''
def shopping(username):
    shopping_flag=True
    while shopping_flag:
        print_commodity()
        __input=input('请输入需要购买物品的编码。【按q返回上级】')

        if __input=='q':
            shopping_flag=False
        elif __input in __db[1]:
            commodity_inventory=check_inventory(__input)
            if commodity_inventory :
                enough_of_money = check_money(username,__input)
                if enough_of_money:
                    add_commodity(username,__input)
                    print('已将%s加入购物车'%__input)
                else:
                    print('余额不足，请重新选择！')
            else:
                print('库存不足，请重新选择！')
        else:
            print('输入错误请重新输入')

    #return False


'''look_shoppingcart 查看购物车功能'''
def look_shoppingcart(username):
    shoppingcart=__db[0][username]['shoppingcart']

    if len(shoppingcart) > 0 :    #购物车不为空 打印所添加物品
        print("=============================================================================")
        for i in range(len(shoppingcart)):
            print("商品名称:%s \t商品价格:¥%s \t购买时间:%s   " %(shoppingcart[i][1],shoppingcart[i][2],shoppingcart[i][3]))
        print("=============================================================================")
    else:
        print('你的购物车还空着呢，赶快去抢购吧~')
        return True

    __input=input("按‘q’退出，按‘c’清空购物车，按‘e’结算")
    if __input=='q':            #退出
        return True
    elif __input == 'e':        #结算
        settle_account()
        return False
    elif __input=='c':          #清空
        __db[0][username]['shoppingcart']=[]
        print('购物车清空成功，赶快重新选购吧~')

'''look_historys 打印历史购买记录'''
def look_historys(username):
    order = __db[0][username]['order']
    if len(order) > 0:
        print( "=============================================================================")
        for i in range(len(order)):
            print("商品名称:%s \t商品价格:¥%s \t购买时间:%s   " % (
                order[i][1], order[i][2], order[i][3]))
        print( "=============================================================================")
    else:
        print("您还没有购物记录，赶快去抢购吧。")

'''print_this_time_shopping 用于退出时打印本次购买的记录'''
def print_this_time_shopping(username):
    if len(this_time_shopping) > 0:
        expense=0
        print( "=============================================================================")
        for i in range(len(this_time_shopping)):
            print("商品名称:%s \t商品价格:¥%s \t购买时间:%s   " % (
                this_time_shopping[i][1], this_time_shopping[i][2], this_time_shopping[i][3]))
            expense+=this_time_shopping[i][2]
        print( "=============================================================================")
        print('您本次购物共消费：¥%d' % (expense))
        print('您账户余额为：¥%d'%(__db[0][username]['salary']))
    else:
        print("您未购买任何物品！")
        print("=============================================================================")
        print('您账户余额为：¥%d' % (__db[0][username]['salary']))
        print("=============================================================================")
        print("欢迎再次光临~")


__db=[]                     #初始化一个数据列表
f=read_of_file()
__db.append(f['account'])   #将用户数据添加到数据列表
__db.append(f['commodity']) #将商品数据添加到数据列表
this_time_shopping=[]
exit_flag=True

while exit_flag:
    username=input('输入用户名:')
    password=input('输入密码:')
    if login(username,password):
        if first_login_check(username):
            salary=int(input('输入工资:'))
            set_user_salary(username,salary)
        else:
            print('您账户余额为：¥ %d'%(__db[0][username]['salary']))
        while exit_flag:

            print('''\na> 购买商品\nb> 查看购物车并结算\nc> 查看历史订单\nq> 退出\n''')
            __input=input('输入编码：')
            if __input == 'q':
                print_this_time_shopping(username)
                save_to_file()
                exit_flag = False
            elif __input == 'a':
                shopping_flag = shopping(username)
            elif __input == 'b':
                shopping_flag = look_shoppingcart(username)
            elif __input == 'c':
                shopping_flag = look_historys(username)
    else:
        print("用户名或密码错误，请重新输入.")

