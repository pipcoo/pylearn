#!/usr/bin/python3
# -*- coding:utf-8 -*-
# @---wufeng---

import sys,subprocess
import yaml

app_config_file = '/data/docker-compose/app/docker-compose.yml'
log_config_file = '/data/docker-compose/log/docker-compose.yml'

# app_config_file = 'app.yml'
# log_config_file = 'log.yml'

def compose_start(service_name,config_file):
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', config_file, 'up', '-d',service_name])

def compose_stop(service_name,config_file):
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', config_file, 'kill', service_name])

def compose_restart(service_name,config_file):
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', config_file, 'restart', service_name])

def compose_reload(service_name,config_file):
    subprocess.check_call(['/usr/bin/docker','pull',
                           'registry.cn-beijing.aliyuncs.com/touchfound/'+images_info(service_name,config_file)[0]+':'+images_info(service_name,config_file)[1]])
    compose_stop(service_name, config_file)
    subprocess.check_call(['/usr/bin/docker-compose', '-f', config_file, 'rm', '-f', service_name])
    compose_start(service_name, config_file)

def compose_status(service_name,config_file):
    print('image name is %s \nimage version is %s'%images_info(service_name,config_file))
    return subprocess.check_call(['/usr/bin/docker-compose', '-f', config_file, 'ps', service_name])

def images_info(service_name,config_file):

    compose_config_map = compose_file_handle(config_file)

    images_info = str(compose_config_map['services'][service_name]['image']).split('/')[-1]

    if ':' in images_info:
        images_name = images_info.split(':')[0]
        images_ver = images_info.split(':')[-1]
    else:
        images_name=images_info
        images_ver='latest'

    return images_name,images_ver

def compose_file_handle(file_path):
    f = open(file_path,"r",encoding="utf-8")
    compose_config_map = yaml.load(f)
    f.close()
    return compose_config_map


def service_type_judge(service_name):
    if service_name in compose_file_handle(app_config_file)['services']:
        return app_config_file
    elif service_name in compose_file_handle(log_config_file)['services']:
        return  log_config_file
    else:
        print('input service name %s not in docker-compose.yml file'%service_name)
        exit(1)

if __name__ == '__main__':

    if len(sys.argv) != 3:
        print('please input start|stop|restart|status|reload and service name!~')
    else:
        service_name = sys.argv[2]
        config_file = service_type_judge(service_name)

        if sys.argv[1]=='start':
            compose_start(service_name,config_file)
        elif sys.argv[1]=='stop':
            compose_stop(service_name,config_file)
        elif sys.argv[1]=='restart':
            compose_restart(service_name,config_file)
        elif sys.argv[1]=='reload':
            compose_reload(service_name,config_file)
        elif sys.argv[1]=='status':
            compose_status(service_name,config_file)
        else:
            print('please input start|stop|restart|status|reload')