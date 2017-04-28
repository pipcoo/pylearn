# @---wufeng---

import os,sys,re
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from ext.DB.core import db
from config.logger import log


def dbapi(command):
    """
    数据库接口
    :param command:   接收sql语句传入
    :return: 
    """
    if setting.DBMODE == 'filedb':
        log.info('dbsql: %s'%command)
        return db.sqlapi(setting.DBNAME,command)
    elif setting.DBMODE == 'mysql':
        pass #todo

