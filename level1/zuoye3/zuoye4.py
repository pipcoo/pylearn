#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng

def read_cfg():

    f=open("haproxy.cfg","r",encoding="utf-8")
    for line in f:

    f.close()

a='backend www.oldboy.org'
b='        server 100.1.7.9 100.1.7.9 weight 20 maxconn 3000'
c=list(b)
d=b[0:8]

if d == '        ':
    print(True)

print(b.split())
print(d)
