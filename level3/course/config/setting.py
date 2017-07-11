# @---wufeng---
import  time
import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

LOGFILE     = "css.log" # 日志文件名称
LOGLEVEL    = "DEBUG"    # 日志级别
NOW = time.strftime('%Y-%m-%d %H:%M:%S')    # 当前时间格式
DBFILE = BASE+'/data'

