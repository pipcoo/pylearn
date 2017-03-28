#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

def append_list(file,read_count):
    file2list = []
    for line in file:
        linesize=0
        read_flag=True
        read_count+=len(line)
        if len(line)>1:
            linesize=len(line)
            line2list=line.replace("\r\n"," ").split()
            if line2list[0]=='backend' and read_flag:
                seeknum[0]-=linesize
                read_flag=False
                break
            elif line2list[0]=='backend' and not read_flag:
                file2list.append(line)
                read_flag = True
            else:
                file2list.append(line)
                #seeknum[1] = 1
    return file2list,read_count

def read_cfg():

    f=open("haproxy.cfg","r",encoding="utf-8")
    read_count=0
    backend_list=[]
    for line in f:
        list1,read_count=append_list(f,read_count)
        read_count+=len(line)
        backend_list.append(list1)
        f.seek(read_count - len(line))
    f.close()
    return backend_list

seeknum=[0,0]
a=read_cfg()

for i in range(1,len(a)):
    print(a[i])
#
# def read_cfg():
#     file2list = []
#     f=open("haproxy.cfg","r",encoding="utf-8")
#
#     a=[]
#     serverlist = []
#     for line in f:
#        key=""
#
#         seeknum[0]+=len(line)
#         if(line.startswith(backend)){
#         if(serverlist.length>1){
#         file2list.append()
#         }
#         key = line.split("")[1]
#         serverlist=[]
#         }else{
#         serverlist.append(line)
#
#         }
#
#
#         a.append(append_list(f))
#         f.seek(seeknum[0] - len(line))
#
# [key1:{'',''}]
#
#     f.close()
#     return a