
import os,sys
BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(BASE)

from core import db_handle
from config.logger import log
from config import setting

db = db_handle.dbapi
dbname = setting.DBNAME

def init_atmdb():
    """
    初始化atm数据库
    :return:
    """
    log.info('------------- database %s init'%dbname)
    db('create database %s'%dbname)
    log.info('database %s created'%dbname)
    db('create table account \(userid int auto_increment,'
       'username str not null unique,account_status str,password str,rule str,create_time str\)')
    log.info('init super admin info')
    db('insert into account values \(\'\',admin,open,admin,admin,%s\)'%setting.now)
    log.info('table account created')
    db('create table party \(party_id int auto_increment,'
       'userid int ,card_num str,card_type str,create_time str,card_balance float\)')
    log.info('table party created')
    db('create table transaction_rate \(rate_id int auto_increment,'
       'transaction_type str,transaction_rate float\)')
    db('insert into transaction_rate values \(\'\',withdraw,%s\)' % setting.CASH_WITHDRAWAL_RATE)
    db('insert into transaction_rate values \(\'\',transfer,%s\)' % setting.TRANSFER_RATE)
    db('insert into transaction_rate values \(\'\',repayment,0\)' )
    log.info('table transaction_rate created')
    db('create table transaction (transaction_id int auto_increment,'
       'transaction_type str,party_id int,counterparty_id int,amount float,txdate str)')
    log.info('table transaction created')
    log.info('------------- database %s init end' % dbname)


def uinstall_atmdb():
    """
    清理删除atmdb数据库
    :param dbname:
    :return:
    """
    log.info('------------- database %s drop'%dbname)

    if db('show databases') is not None:
        if dbname in db('show databases'):
            db('drop database %s'%dbname)
            log.info('database %s is drop' % dbname)
        else:
            print('database %s does not exist'%dbname)
            log.warn('database %s does not exist'%dbname)
    else:
        log.warn('database %s does not exist' % dbname)
    log.info('------------- database %s drop end' % dbname)


uinstall_atmdb()
init_atmdb()

