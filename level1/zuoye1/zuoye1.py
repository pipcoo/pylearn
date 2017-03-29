#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng


'''
模拟登陆：
1. 用户输入帐号密码进行登陆
2. 用户信息保存在文件内
3. 用户密码输入错误三次后锁定用户
'''

__account=[]

f = open("account.txt","r",encoding="utf-8")
for line in f:
    __account.append(line.split())      #将文件每一行转换成列表保存
f.close()
input_count=0
pass_count=0
change_tags=False
exit_tags = True
while exit_tags  :

    if input_count > 2 :                #判断输入次数 输入大于3次就退出
        print("input count too many")
        exit_tags = False
        break

    username = input("please input your username:")
    password = input("please input your password:")

    for index in range(len(__account)): #遍历用户列表
        if __account[index][0] == username and __account[index][1]==password and __account[index][2]=='unlock':
            print("Login Successful!")  #用户密码都对应 且用户状态没锁 返回成功 并退出循环
            exit_tags=False
            break
        elif  __account[index][0] == username and  __account[index][2]=='locked':
            print("user is  Locked!")   #用户存才 状态是锁定 打印用户锁定
            exit_tags = False
            break
        elif __account[index][0] == username and __account[index][1] != password and __account[index][2]=='unlock':
            if pass_count == 2:         #用户存在 密码输错 次数大于3次 则退出
                print("user is  Locked!")
                __account[index][2]='locked'    #设置 用户状态标识
                change_tags=True
                exit_tags=False
                break
            print("Wrong username or password;")
            pass_count +=1              #密码输入错误次数+1

            break

    else:
        print("%s does not exist." %username)   # 遍历一遍后没有找到用户 报用户不存在


    input_count += 1                            # 输入次数+1

if change_tags :
    f = open("account.txt", "w", encoding="utf-8")
    for list1 in __account:                     #遍历列表
        f.write(" ".join(list1))                #列表转换成字符串 空格分开 写入文件
        f.write("\n")                           #写入回车
    f.close()

