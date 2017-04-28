# @---wufeng---

import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from config.logger import log
db = db_handle.dbapi

def transaction_handle():
    pass
