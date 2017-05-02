# @---wufeng---

import os,sys,re,random
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from config.logger import log
from config import setting
db = db_handle.dbapi

userdata = {
    'auth_status' : False,
    'amount' : None
}

user_type = {'1':'bank_clerk','2':'general_account'}


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
    db('select username,rule,create_time,account_status from account')
    input('任意键退出')
def set_limit():
    pass
def create_account():
    user_type_default = 'general_account'
    create_data_inpit = ['用户名','密码']
    create_data = input_handle(create_data_inpit)
    if create_data[0] in row_to_list(db('select username from account')[1]):
        print('账户名已存在')
    else:
        db('insert into account values \(\'\',%s,open,%s,%s,%s\)'%(create_data[0],create_data[1],user_type_default,setting.now))
        user_id = db('select userid from account where username = %s'%(create_data[0]))
        create_party(user_id[1][0][0])
def cencel_account():
    cencel_account_dis = ['账户名']
    cencel_account_name = input_handle(cencel_account_dis)[0]

    if cencel_account_name not in row_to_list(db('select username from account')[1]):
        print('账户不存在')
    else:
        db('delete from party where userid = %d '%(db('select userid from account where username = %s'%(cencel_account_name))))
        db('delete from account where username = %s'%cencel_account_name)

def frozen_account():
    pass

def create_party(user_id):
    card_type_default ='credit'
    card_num = str(int(random.uniform(0,1)*10**16))
    amount_defalut = setting.ACCOUNT_DEFAULT_LIMIT
    db('insert into party values \(\'\',%s,%s,%s,%s,%d\)'
       %(user_id,card_num,card_type_default,setting.now,amount_defalut))

def user_type_select():
    user_type_dis = '''
    1、银行职员
    2、普通用户
    '''
    exit_flag = False
    while not exit_flag:
        print('请选择账户类型\n %s '%user_type_dis)
        _input=input('>>')
        if _input in user_type:
            user_select = user_type[_input]
            exit_flag = True
        else:
            print('请输入正确的类型编码')

    return user_select


def input_handle(in_data_list):

    out_data_list = []
    for i in in_data_list:
        if i == 'user_type':
            out_data_list.append(user_type_select())
        else:
            out_data_list.append(input('请输入 %s :'%i))
    return out_data_list


def row_to_list (row):

    list1 = []
    for i in row:
        list1.append(i[0])

    return list1
