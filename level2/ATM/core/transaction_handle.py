# @---wufeng---

import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from config.logger import log
db = db_handle.dbapi
dbssc = db_handle.dbapi_select_single_col
dbssv = db_handle.dbapi_select_single_value

transaction_features = {
    'repayment':'plus',
    'withdraw':'reduce'
}
def amount_handle(v1,v2,calc_type):
    if calc_type == 'plus':
        return v1+v2
    elif calc_type == 'reduce':
        return v1-v2

def transaction_handle(userid,txf,amount,counterparty_id = ''):
    rate = dbssv('select transaction_rate from transaction_rate where transaction_type = %s'%txf)
    if counterparty_id == '':
        new_amount = amount_handle(old_amount,amout,transaction_features[txf]) + amount*rate

