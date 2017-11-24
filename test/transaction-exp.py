#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: wufeng


import models
from sqlalchemy import Table, Column, Integer, String, Date, Float, create_engine, and_,or_
from sqlalchemy.orm import sessionmaker, aliased
# import config
# DB class
import os, sys, inspect
import datetime,time

os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.ZHS16GBK'

db = create_engine('oracle://vms4uat:123456789@60.205.220.93:1521/uatdb', echo=True)

Session = sessionmaker(bind=db)

session = Session()

classlist = []
for name, obj in inspect.getmembers(models):
    if inspect.isclass(obj):
        classlist.append((name.lower(), obj))

classdict = dict(classlist)

t_master = aliased(classdict['tslordermaster'])
t_cost = aliased(classdict['tslordercost'])
t_refund = aliased(classdict['tslorderrefund'])
t_vendout = aliased(classdict['tslordervendout'])
t_notify = aliased(classdict['tslordernotify'])
t_sku = aliased(classdict["tmtsku"])
t_vm = aliased(classdict["tmtvm"])
t_node = aliased(classdict["tmtnode"])
t_channel = aliased(classdict['tmtvmchannel'])


def get_transaction(begin_time, end_time):
    try:
        L = session.query(t_node.node_name,
                          t_master.order_seq,
                          t_vm.inner_code,
                          t_channel.channel_code,
                          t_sku.sku_id,
                          t_sku.sku_name,
                          t_cost.cost_type,
                          t_master.order_price,
                          t_cost.cost_time,
                          t_cost.cost_status,
                          t_vendout.vendout_time,
                          t_vendout.vendout_status,
                          t_vendout.vendout_status,
                          t_refund.refund_status).select_from(t_master). \
            join(t_cost, t_master.order_id == t_cost.order_id). \
            join(t_vm, t_vm.vm_id == t_master.vm_id). \
            join(t_node, t_node.node_id == t_vm.node_id). \
            join(t_sku, t_sku.sku_id == t_master.sku_id). \
            outerjoin(t_vendout, t_vendout.order_id == t_master.order_id). \
            outerjoin(t_channel, t_channel.channel_id == t_vendout.vendout_channel_id). \
            outerjoin(t_refund, t_refund.order_id == t_master.order_id). \
            outerjoin(t_notify, t_notify.order_id == t_master.order_id) #. \
            # filter(t_master.order_time > begin_time)
            # filter(and_(t_master.order_time > begin_time, t_master.order_time <= end_time))


    except NoResultFound as e:
        print(e)
    else:
        return L


begin_time_str="2017-09-25 17:00:00"
end_time_str="2017-09-26 17:00:00"

begin_time=time.strptime(begin_time_str, "%Y-%m-%d %H:%M:%S")
end_time=time.strptime(end_time_str, "%Y-%m-%d %H:%M:%S")

tr_list = get_transaction(begin_time,end_time)

print(tr_list.first())
# print(tr_list.count())
session.close()



