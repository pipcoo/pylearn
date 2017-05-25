#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: wufeng
# @Date:   2016-09-20 17:42:06
# @Last Modified by:   wufeng
# @Last Modified time: 2016-09-21 13:05:50

import base64
import datetime
import requests
import logging


logger = logging.getLogger('mylogger')
logger.setLevel(logging.DEBUG)

# 创建一个handler，用于写入日志文件
fh = logging.FileHandler('vm_commander.log')
fh.setLevel(logging.DEBUG)

# 再创建一个handler，用于输出到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# 定义handler的输出格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)

# 给logger添加handler
logger.addHandler(fh)
logger.addHandler(ch)

# 记录一条日志
#logger.info('foorbar')


#发起http请求
# def urlOpen(req,data=None):
#     res = urllib2.urlopen(req,data)
#     data = res.read()
#     res.close()
#
#生成HTTP报文
def createHttpReq(body,responseMode):
    headers = {}
    headers["Content-Type"] = "application/"+responseMode
    headers["Content-Length"] = str(len(body))

    return headers

#
# class RestAPI:
#
#     HOST = "http://192.168.101.233"
#     PORT = "8890"
#     SOFTVER = "cmd/Command/exec"
#     JSON = 'json'
#
#     def __init__(self,innercode):
#         self.innercode = innercode
#
#     def sendcommand(self,command):
#         now = datetime.datetime.now()
#         timestamp = now.strftime("%Y%m%d%H%M%S")
#         url = self.HOST + ":" + self.PORT + "/" + self.SOFTVER
#         responseMode = self.JSON
#         body = '{"<InnerCode>k__BackingField":%s,"<Cmd>k__BackingField":%s,"<UserName>k__BackingField":null,"<Token>k__BackingField":null}'%(self.innercode,command)
#         logger.info(body)
#         req = requests.get(url)
#         return urlOpen(createHttpReq(req,body,responseMode))

class RestAPI:

    HOST = "http://192.168.101.233"
    PORT = "8890"
    SOFTVER = "cmd/Command/exec"
    JSON = 'json'

    def __init__(self,innercode):
        self.innercode = innercode

    def sendcommand(self,command):
        now = datetime.datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")
        url = self.HOST + ":" + self.PORT + "/" + self.SOFTVER
        responseMode = self.JSON
        body = '{"<InnerCode>k__BackingField":"%s","<Cmd>k__BackingField":"%s","<UserName>k__BackingField":null,"<Token>k__BackingField":null}'%(self.innercode,command)
        logger.info(body)
        req = requests.get(url)
        r = requests.post(url,body,headers=createHttpReq(body,self.JSON))
        http_request = r.json()
        http_status = r.status_code
        return http_status,http_request


def main():
    innercode  =  '02100022'
    a = RestAPI(innercode)
    b = []
    http_status , http_request = a.sendcommand('tasklist')

    b.append(http_request)
    print(http_status)
    print(http_request)




if __name__ == '__main__':
    main()