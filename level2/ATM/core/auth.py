# @---wufeng---
# -*- coding: utf-8 -*-
import os,sys,re
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)
from core.atm import userdata
from core.atm import input_handle
from core import db_handle
from config.logger import log
dbssc = db_handle.dbapi_select_single_col
dbssv = db_handle.dbapi_select_single_value

def auth(user_type):
    login_info_dis = ['用户名','密码']
    username,password =  input_handle(login_info_dis)
    if username in dbssc('select username from account where rule = %s'%(user_type)):
        if password == dbssv('select password from account where username = %s'%(username)) and dbssv('select account_status from account where username = %s'%(username)) == 'open' :
            userdata['auth_status'] = True
            userdata['userid'] = dbssv('select userid from account where username = %s'%(username))
            userdata['user_type'] = user_type
            log.info('用户 %s 认证登陆成功'%(username))
            return True
        elif dbssv('select account_status from account where username = %s'%(username)) == 'locked':
            log.warn('用户 %s 账户锁定 请求认证失败' % (username))
            print('用户 %s 账户锁定 请求认证失败' % (username))
            return False
        else:
            log.warn('用户 %s 密码错误 请求认证失败' % (username))
            print('用户 %s 密码错误 请求认证失败' % (username))
            return False
    else:
        log.warn('用户 %s 不存在 请求认证失败' % (username))
        print('用户 %s 不存在 请求认证失败' % (username))
        return False

def login_required(func):
    def wrapper(*args,**kwargs):
        if args[0].get('auth_status') and args[1] == args[0].get('user_type'):
            return func(*args,**kwargs)
        elif args[0].get('auth_status') and args[1] != args[0].get('user_type'):
            exit("用户权限不足")
        else:
            if auth(args[1]):
                return func(*args, **kwargs)
            else:
                log.error('用户认证失败')
                exit("用户认证失败")
    return wrapper

# @login_required
# def rr(data,user_type):
#     print(data)
#
# rr(atm.userdata,'general_account')