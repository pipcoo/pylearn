#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author: wufeng

import os,sys,subprocess
import yaml

BASE=os.path.dirname(os.path.abspath(__file__))

compose_file=BASE+'/docker-compose.yml'
#启动容器个数
instances_num=3
#本机IP
local_ip='192.168.20.135'
#运行环境
runenv='pro'
#镜像版本
image_ver='3.0.0-release'
#镜像地址
image_url='registry.cn-beijing.aliyuncs.com/touchfound/mcs'
#配置文件下载url
setting_url='http://cf.touchfound.net/docker-config-file/mcs/'+runenv+'/mcs-config.xml'
#本地日志路径
logpath='/data/mcs/logs'
#容器内日志路径
launcher_logpath='/opt/launcher/logs'
#mcs容器内端口配置
mcs_ports={'HTTP_PORT':8011,'KEEP_PORT':8031}
#mcs对外端口配置
mcs_ext_ports={'HTTP_PORT':8011,'KEEP_PORT':20031}

compose_map={'version': '2'}
instances_map={}


def compose_file_handle():
    for i in range(instances_num):
        instances_map["mcs"+str(i)]={'image':image_url+':'+image_ver,'volumes':[logpath+'/'+"mcs"+str(i)+':'+launcher_logpath],
                             'environment':['SETTING_URL='+setting_url,'APPNAME='+'mcs'+str(i),'RUNENV='+runenv,
                                            'IP='+local_ip,'KEEP_PORT='+str(mcs_ports['KEEP_PORT']),
                                            'HTTP_PORT='+str(str(mcs_ports['HTTP_PORT']+i))],
                                     'ports':[str(mcs_ext_ports['KEEP_PORT']+i)+':'+str(mcs_ports['KEEP_PORT']),
                                              str(mcs_ext_ports['HTTP_PORT'] + i) + ':' + str(mcs_ports['HTTP_PORT']+i)]}
    compose_map['services']=instances_map

    f = open("docker-compose.yml", "w", encoding="utf-8")
    yaml.dump(compose_map,f)
    f.close()

def compose_start():
    return subprocess.check_call(['/usr/bin/docker-compose','-f',compose_file,'up','-d'])

def compose_restart():
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', compose_file,'restart'])

def compose_stop():
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', compose_file, 'kill'])

def compose_rm():
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', compose_file, 'rm','-f'])

def compose_reload():
    pull_url = image_url+':'+image_ver
    res = subprocess.check_call(['/usr/bin/docker','pull',pull_url])
    compose_stop()
    compose_rm()
    compose_start()

def compose_status():
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', compose_file, 'ps'])

if __name__ == '__main__':
    compose_file_handle()
    if sys.argv[1]=='start':
        compose_start()
    elif sys.argv[1]=='stop':
        compose_stop()
    elif sys.argv[1]=='restart':
        compose_restart()
    elif sys.argv[1]=='reload':
        compose_reload()
    elif sys.argv[1]=='status':
        compose_status()
    elif sys.argv[1]=='rmall':
        compose_rm()
    else:
        print('please input start|stop|restart|status|reload|rmall')
