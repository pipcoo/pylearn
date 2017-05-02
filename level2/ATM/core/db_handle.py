# @---wufeng---
# -*- coding: utf-8 -*-
import os,sys,re
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from ext.DB.core import db
from config.logger import log
from config import setting

def dbapi(command):
    """
    数据库接口
    :param command:   接收sql语句传入
    :return: 
    """
    if setting.DBMODE == 'filedb':
        log.info('dbsql: %s'%command.replace('\\',''))
        result = db.sqlapi(setting.DBNAME,command)
        log.debug(result)
        return result
    elif setting.DBMODE == 'mysql':
        pass #todo


def dbapi_select_single_col(command):
    """
    单列查询接口 返回一个列表
    :param command: 
    :return: 
    """
    result_list = []
    if re.match('select\s+\w+\s+from\s+.+',command):
        for i in dbapi(command)[1]:
            result_list.append(i[0])
        log.debug(result_list)
        return result_list
    else:
        print('只能查询一列')

def dbapi_select_single_value(command):
    """
    单列查询接口 返回一个值
    :param command: 
    :return: 
    """
    result = dbapi_select_single_col(command)
    if len(result) > 1:

        return result[0]
    else:
        log.error('存在多个值')