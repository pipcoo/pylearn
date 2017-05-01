# @---wufeng---

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
        log.info(result)
        return result
    elif setting.DBMODE == 'mysql':
        pass #todo

