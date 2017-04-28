# @---wufeng---

import os,sys,re
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
