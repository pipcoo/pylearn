# -*- coding:utf-8 -*-
# @---wufeng---

import requests

from aliyunauth import CmsAuth

ACCESS_KEY='LTAIIp5cY52rQjFI'
SECRET_KEY='SB4WHPs47IWMZz12qudBkr4hOd7Z0j'
URL='https://metrichub-cms-cn-hangzhou.aliyuncs.com'

udata = {"content":"123,abc","groupId":100,"name":"Event_0","time":"20171127T144439.948+0800"}

req = requests.post(URL+'/event/custom/upload',data=udata,auth=CmsAuth(ACCESS_KEY,SECRET_KEY)).

print(req)

