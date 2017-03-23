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
    __account.append(line.split())
f.close()
input_count=0
pass_count=0
change_tags=False
exit_tags = True
while exit_tags  :

    if input_count > 2 :
        print("input count too many")
        exit_tags = False
        break

    username = input("please input your username:")
    password = input("please input your password:")

    for index in range(len(__account)):
        if __account[index][0] == username and __account[index][1]==password and __account[index][2]=='unlock':
            print("Login Successful!")
            exit_tags=False
            break
        elif  __account[index][0] == username and  __account[index][2]=='locked':
            print("user is  Locked!")
            exit_tags = False
            break
        elif __account[index][0] == username and __account[index][1] != password and __account[index][2]=='unlock':
            if pass_count == 2:
                print("user is  Locked!")
                __account[index][2]='locked'
                change_tags=True
                exit_tags=False
                break
            print("Wrong username or password;")
            pass_count +=1

            break

    else:
        print("%s does not exist." %username)


    input_count += 1

if change_tags :
    f = open("account.txt", "w", encoding="utf-8")
    for list1 in __account:
        f.write(" ".join(list1))
        f.write("\n")
    f.close()

