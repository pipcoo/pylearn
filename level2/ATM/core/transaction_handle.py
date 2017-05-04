# @---wufeng---

import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from config.logger import log
from core import atm
from config import setting
db = db_handle.dbapi
dbssc = db_handle.dbapi_select_single_col
dbssv = db_handle.dbapi_select_single_value

#交易类型的计算关系
transaction_features = {
    'repayment':'plus',
    'withdraw':'reduce',
    'transfer':'reduce',
    'payment':'reduce'
}
def amount_handle(value1,value2,calc_type):
    """
    交易金额处理 
    :param value1: 
    :param value2: 
    :param calc_type: 
    :return: 
    """
    if calc_type == 'plus':
        return value1 + value2
    elif calc_type == 'reduce':
        return value1 - value2

def sign_handle(amount,calc_type):
    """
    交易金额 符号处理  返回 字符串类型的 交易金额
    :param amount: 
    :param calc_type: 
    :return: 
    """
    if calc_type == 'plus':
        return '+'+ str(amount)
    elif calc_type == 'reduce':
        return '-'+ str(amount)

def transaction_handle(party_id,txf,amount,txdesc,counterparty_id = ''):
    """
    交易处理 
    :param party_id:  账户id
    :param txf:  交易类型
    :param amount:  交易金额
    :param txdesc:  交易描述
    :param counterparty_id: 交易对手ID 
    :return: 
    """
    rate = dbssv('select transaction_rate from transaction_rate where transaction_type = %s'%txf)
    acc1_old_amount = float(dbssv('select card_balance from party where party_id = %s'%party_id))
    if counterparty_id == '':
        acc1_new_amount = amount_handle(acc1_old_amount,amount,transaction_features[txf]) + amount*rate
        db('update party set card_balance = %s where party_id = %s' %
           (acc1_new_amount, party_id))
        transaction_record(txf, party_id, '', amount, txdesc)
        if amount*rate != 0:
            transaction_record(txf, party_id, '', abs(amount*rate), '手续费')

    else:
        acc2_old_amount = float(dbssv('select card_balance from party where party_id = %s'%counterparty_id))
        acc1_new_amount = amount_handle(acc1_old_amount,amount,transaction_features[txf]) + amount*rate
        acc2_new_amount = amount_handle(acc2_old_amount,amount,transaction_features['repayment'])
        db('update party set card_balance = %s where party_id = %s' %
           (acc1_new_amount,party_id) )
        db('update party set card_balance = %s where party_id = %s' %
           (acc2_new_amount, counterparty_id))
        transaction_record(txf, party_id, counterparty_id, amount, txdesc)
        transaction_record(txf, party_id, '', abs(amount*rate), '转账手续费')
        transaction_record('repayment', counterparty_id, party_id, amount, txdesc)

def transaction_record(txf, acc1_id, acc2_id, amount,txdesc):
    """
    交易流水记录 
    :param txf:  交易类型
    :param acc1_id:  交易账户ID
    :param acc2_id:  交易对手账户ID
    :param amount:  交易金额
    :param txdesc:  交易描述
    :return: 
    """
    db('insert into transaction values \(\'\',%s,%s,%s,%s,%s,%s,%s\)' %
       (txf, acc1_id, acc2_id, amount, sign_handle(amount,transaction_features[txf]),setting.now,txdesc))


#transaction_handle(1,'transfer',1000,'转账xxx1',2)
#transaction_handle(1,'withdraw',5000,'取款5000')