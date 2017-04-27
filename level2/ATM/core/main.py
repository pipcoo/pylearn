
import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from ext.DB.core import db

from config.logger import log

from config import setting


userdata = {
    'auth_status' : False,
    'amount' : None
}


def dbapi(command):
    """
    数据库接口
    :param command:   接收sql语句传入
    :return: 
    """
    if setting.DBMODE == 'filedb':
        return db.sqlapi(setting.DBNAME,command)
    elif setting.DBMODE == 'mysql':
        pass #todo


def auth():
    pass


def menu_select():
    list1 = {
        '1': 'account_manager',
        '2': 'super_manager'
    }
    list2 = {
        '1': ''
    }



def account_manager():
    pass


def super_manager():
    pass


def run():

    exit_flag = False
    menu1 = '''
    1、用户
    2、管理员
    0、退出
    '''
    while not exit_flag:
        print(menu1)
        _input = input('输入选择编号: \n>>')
        if _input == '0':
            exit_flag = True



run()