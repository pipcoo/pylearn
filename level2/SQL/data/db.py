#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: db.py
@time: 2017/4/8 23:36
"""

import json

db={
    "tablelist":{"emp":[{'staff_id':['int','True','True']},{'name':['str','True','False']},{'age':['int','True','False']},{'phone':['str','True','False']},{'dept':['str','True','False']},{'enroll_date':['str','True','False']}]
},
    "tabledata":{"emp":[[1,'Alex Li',22,'13651054608','IT','2013-04-01'],[2,'pipcoo',21,'13900001111','HR','2017-03-01']]}
}

f=open("db.dbf","w",encoding="utf-8")

f.write(json.dumps(db))

f.close()