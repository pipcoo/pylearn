#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re,arrow

mcslog_file = open("pro_mcs_info_2017-11-09.log","r",encoding="UTF-8")
usr_time_file = open('use_time.log',"w",encoding="UTF-8")
ask_list = []
result_list = []
interval_time =arrow.get('05','ss')

for line in mcslog_file :

    if re.search('.*com\.kdx\.mcs\.core\.vm\.VirtualVm.*',line) and re.search('ask',line):
        start_time = arrow.get(re.search('2017.*,\d+',line).group(),'YYYY-MM-DD HH:mm:ss,SSS')
        start_ask=eval(re.search('{.*}\sis',line).group().replace('false','False').replace('true','True').replace('is',''))
        start_ask['start_time']=start_time
        ask_list.append(start_ask)
    else:
        for ask_message in ask_list:
            if re.search('.*com\.kdx\.mcs\.keep\.mina\.ConnectionHandler.*', line) and re.search(str(ask_message['sn']),line):
                re_time = arrow.get(re.search('2017.*,\d+', line).group(),'YYYY-MM-DD HH:mm:ss,SSS')
                ask_list.remove(ask_message)
                ask_message['re_time'] = re_time
                use_time=ask_message['re_time']-ask_message['start_time']
                ask_message['use_time']=use_time
                # print(arrow.get(str(use_time),'HH:mm:ss,SSS'))
                if arrow.get(use_time,'HH:mm:ss,SSSSSS')>interval_time:
                #
                    write_info = str(ask_message['start_time'].format('YYYY-MM-DD HH:mm:ss'))+'\t'+str(ask_message['data']['innerCode'])+'\t'+str(use_time)+'\n'
                    usr_time_file.write(write_info)



