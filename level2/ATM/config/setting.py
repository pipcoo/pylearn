# @---wufeng---
import  time

DBNAME      = "atmdb"   # 数据库名称
LOGFILE     = "atm.logs" # 日志文件名称
LOGLEVEL    = "DEBUG"    # 日志级别
DBMODE      = "filedb"  # 存储引擎
ACCOUNT_DEFAULT_LIMIT = 15000   #初始化信用额度
now = time.strftime('%Y-%m-%d %H:%M:%S')    # 当前时间格式

#提现费率--初始化时生效
CASH_WITHDRAWAL_RATE = -0.01
#转账费率--初始化时生效
TRANSFER_RATE = -0.005
