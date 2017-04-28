
import os,sys,re

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



def user_account_view():
    pass
def repayment():
    pass
def withdraw():
    pass
def transfer_accounts():
    pass
def bill_view():
    pass


def account_view():
    pass
def set_limit():
    pass
def create_account():
    pass
def cencel_account():
    pass
def frozen_account():
    pass


def menu_print(menu_level_name,menu_list):
    exit_flag = False
    while not exit_flag:
        print(menu_list)
        _input = input('输入选择编号: \n>>')
        if _input == '0':
            exit_flag = True
        else:
            menu_select(menu_level_name, _input)

def account_manager():
    menu1 = '''
    ------- Bank -------
    1、个人账户信息
    2、还款
    3、取款
    4、转账
    5、账单
    0、退出
    '''
    menu_print('menu1', menu1)

def bank_clerk():
    menu2 = '''
    ------- Bank clerk Manager -------
    1、账户查看
    2、设置额度
    3、开户
    4、销户
    5、冻结
    0、退出
    '''
    menu_print('menu2', menu2)


def menu_select(menu_no,select_num):

    menu_list0 = {
        '1': account_manager,
        '2': bank_clerk
    }

    menu_list1 = {
        '1': user_account_view,
        '2': repayment,
        '3': withdraw,
        '4': transfer_accounts,
        '5': bill_view
    }

    menu_list2 = {
        '1': account_view,
        '2': set_limit,
        '3': create_account,
        '4': cencel_account,
        '5': frozen_account
    }

    menu_level = {
        'menu0': menu_list0,
        'menu1': menu_list1,
        'menu2': menu_list2

    }

    if select_num in menu_level[menu_no]:
        return menu_level[menu_no][select_num]()
    else:
        print('请输入正确的编号')


def run():

    menu0 = '''
    1、个人用户
    2、银行职员
    0、退出
    '''
    menu_print('menu0',menu0)



run()