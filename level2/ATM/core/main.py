# @---wufeng---

import os,sys,re
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from config import setting
from core import atm


def menu_print(menu_level_name,menu_list):
    """
    处理菜单打印
    :param menu_level_name: 
    :param menu_list: 
    :return: 
    """
    exit_flag = False
    while not exit_flag:
        print(menu_list)
        _input = input('输入选择编号:\n>>')
        if _input == '0':
            exit_flag = True
        else:
            menu_select(menu_level_name, _input)

def general_account():
    """
    用户功能菜单
    :return: 
    """
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
    """
    银行职员菜单
    :return: 
    """
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
    """
    处理惨淡选择对应关系
    :param menu_no: 
    :param select_num: 
    :return: 
    """

    menu_list0 = {
        '1': general_account,
        '2': bank_clerk
    }

    menu_list1 = {
        '1': atm.user_account_view,
        '2': atm.repayment,
        '3': atm.withdraw,
        '4': atm.transfer_accounts,
        '5': atm.bill_view
    }

    menu_list2 = {
        '1': atm.account_view,
        '2': atm.set_limit,
        '3': atm.create_account,
        '4': atm.cencel_account,
        '5': atm.frozen_account
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
    """
    运行入口
    :return: 
    """

    menu0 = '''
    1、个人用户
    2、银行职员
    0、退出
    '''
    menu_print('menu0',menu0)



run()