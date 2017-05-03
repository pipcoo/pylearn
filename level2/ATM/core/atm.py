# @---wufeng---
# -*- coding: utf-8 -*-
import os,sys,re,random
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from core import transaction_handle
from config.logger import log
from config import setting
db = db_handle.dbapi
dbssc = db_handle.dbapi_select_single_col
dbssv = db_handle.dbapi_select_single_value

userdata = {
    'auth_status' : False,
    'amount' : None,
    'userid': 2
}

user_type = {'1':'bank_clerk','2':'general_account'}
transaction_type = {
    'repayment':'存入',
    'withdraw':'提现',
    'transfer':'转账'
}

def auth():
    pass

def user_account_view(username):
    dis_template = '账户名: %s \t卡号: %s \t开户时间: %s \t剩余额度: %s \t账户状态: %s'
    for row in db('select userid,card_num,create_time,card_balance,party_id from party')[1]:
        row[4] = dbssc('select account_status from account where userid = %s' % row[0])[0]
        row[0] = dbssc('select username from account where userid = %s' % row[0])[0]
        log.debug(row)
        if username == row[0]:
            print(dis_template % tuple(row))
    input('任意键退出')

def select_party(userid,txtype):
    party_list = dbssc('select card_num from party where userid = %s' % (userid))
    rownum = 0
    rownum_list = []
    for i in party_list:
        print('%s. 卡号[%s]'%(rownum,i))
        rownum_list.append(rownum)
        rownum+=1
    exit_flag = False
    while not exit_flag:
        select_card_num = int(input('请输入选择 %s 账户的编号：\n>>'%transaction_type[txtype]))
        if select_card_num in rownum_list:
            exit_flag = True
            select_card = party_list[select_card_num]
        else:
            print('输入账号编码错误')
            log.warn('输入账号编码错误')
    party_id = dbssv('select party_id from party where card_num = %s' % (select_card))
    return party_id

def repayment():
    repayment_dis = ['存款金额']
    party_id = select_party(userdata['userid'],'repayment')
    repayment_amount = float(input_handle(repayment_dis)[0])
    transaction_handle.transaction_handle(party_id, 'repayment', repayment_amount, '存入'+ str(repayment_amount))

def withdraw():
    repayment_dis = ['取现金额']
    party_id = select_party(userdata['userid'], 'withdraw')
    repayment_amount = float(input_handle(repayment_dis)[0])
    transaction_handle.transaction_handle(party_id, 'withdraw', repayment_amount, '提现' + str(repayment_amount))

def transfer_accounts():

    pass

def bill_view():
    dis_template = '交易时间: %s \t用户名： %s \t账号: %s \t交易类型: %s \t交易金额: %s \t对手用户名: %s \t对手账号: %s \t交易信息: %s'
    transaction_hist_list = db('select txdate,party_id,transaction_type,tx_amount_dis,counterparty_id,txdesc from transaction')
    if len(transaction_hist_list[1]) > 0:
        for row in transaction_hist_list[1]:
            party_id = row[1]
            row.insert(1,get_user_info(party_id)[0])
            row[2] = get_user_info(party_id)[1]
            if row[5] is not None:
                counterparty_id = row[5]
                row.insert(5,get_user_info(party_id)[0])
                row[6] = get_user_info(counterparty_id)[1]
            else:
                row.insert(5,None)
            row[3]=transaction_type[row[3]]
            print(dis_template % tuple(row))
    else:
        print('没有消费记录')
    input('任意键退出')

def get_user_info(party_id):
    if party_id is not None:
        user_id = dbssv('select userid from party where party_id = %s' %(party_id))
        username = dbssv('select username from account where userid = %s' % (user_id))
        card_num = dbssv('select card_num from party where party_id = %s' % (party_id) )
        return username,card_num
    else:
        log.warn('没有交易对手')




def account_view():
    dis_template = '账户名: %s \t卡号: %s \t开户时间: %s \t信用额度: %s \t可用额度: %s \t账户状态: %s'

    for row in db('select userid,card_num,create_time,card_limit,card_balance,party_id from party')[1]:
        row[5] = dbssc('select account_status from account where userid = %s' % row[0])[0]
        row[0] = dbssc('select username from account where userid = %s' % row[0])[0]
        log.debug(row)
        print(dis_template % tuple(row))

    input('任意键退出')
def set_limit():
    set_limit_dis = ['账户名','新的额度是']
    set_limit_name,set_limit_new_amount = input_handle(set_limit_dis)
    if set_limit_name not in dbssc('select username from account'):
        print('账户不存在')
        log.warn('账户 %s 不存在' % set_limit_name)
    else:
        db('update party set card_balance = %d where userid = %d '
           %(int(set_limit_new_amount),dbssc('select userid from account where username = %s'%(set_limit_name))[0]))

def create_account():
    user_type_default = 'general_account'
    create_data_inpit = ['用户名','密码']
    create_data = input_handle(create_data_inpit)
    if create_data[0] in dbssc('select username from account'):
        print('账户名已存在')
    else:
        db('insert into account values \(\'\',%s,open,%s,%s,%s\)'%(create_data[0],create_data[1],user_type_default,setting.now))
        user_id = dbssc('select userid from account where username = %s'%(create_data[0]))[0]
        create_party(user_id)
def cencel_account():
    cencel_account_dis = ['账户名']
    cencel_account_name = input_handle(cencel_account_dis)[0]
    log.debug('销户的账户名%s'%cencel_account_name)

    if cencel_account_name not in dbssc('select username from account'):
        print('账户不存在')
        log.info('账户 %s 不存在' % cencel_account_name)
    else:
        db('delete from party where userid = %d '%(dbssc('select userid from account where username = %s'%(cencel_account_name))[0]))
        db('delete from account where username = %s'%cencel_account_name)

def frozen_account():
    frozen_account_dis = ['账户名']
    frozen_account_name = input_handle(frozen_account_dis)[0]
    if frozen_account_name not in dbssc('select username from account'):
        print('账户不存在')
        log.warn('账户 %s 不存在' % frozen_account_name)
    else:
        db('update account set account_status = locked where userid = %d '%(dbssc('select userid from account where username = %s'%(frozen_account_name))[0]))


def create_party(user_id):
    card_type_default ='credit'
    card_num = str(int(random.uniform(0.4,0.5)*10**16))
    amount_defalut = setting.ACCOUNT_DEFAULT_LIMIT
    db('insert into party values \(\'\',%s,%s,%s,%s,%d,%d\)'
       %(user_id,card_num,card_type_default,setting.now,amount_defalut,amount_defalut))

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
