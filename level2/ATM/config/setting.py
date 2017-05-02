# @---wufeng---
import  time

DBNAME      = "atmdb"
LOGFILE     = "atm.logs"
LOGLEVEL    = "DEBUG"
DBMODE      = "filedb"
ACCOUNT_DEFAULT_LIMIT = 15000
now = time.strftime('%Y-%m-%d %H:%M:%S')

#提现费率--初始化时生效
CASH_WITHDRAWAL_RATE = -0.01
#转账费率--初始化时生效
TRANSFER_RATE = -0.005
