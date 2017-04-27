


import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from ext.DB.core import db

from config.logger import logging

from config import setting


def init_atmdb(dbname):
    """
    初始化atm数据库
    :return: 
    """
    logging.info('------------- database %s init'%dbname)

    db.sqlapi(dbname,'create database %s'%dbname)

    logging.info('database %s created'%dbname)

    db.sqlapi(dbname,
              'create table account \(userid int auto_increment,username str not null unique,account_status str,password str\)')
    logging.info('table account created')
    db.sqlapi(dbname,
              'create table party \(party_id int auto_increment,userid int ,card_num str,card_type str,create_time str,card_balance float\)')
    logging.info('table party created')
    db.sqlapi(dbname,
              'create table transaction_rate \(rate_id int auto_increment,transaction_type str,transaction_rate float\)')
    logging.info('table transaction_rate created')
    db.sqlapi(dbname,
              'create table transaction (transaction_id int auto_increment,transaction_type str,party_id int,counterparty_id int,amount float,txdate str)')
    logging.info('table transaction created')

    logging.info('------------- database %s init end' % dbname)
def uinstall_atmdb(dbname):
    """
    清理删除atmdb数据库
    :param dbname: 
    :return: 
    """
    logging.info('------------- database %s drop'%dbname)

    if db.sqlapi(dbname,'show databases') is not None:
        if dbname in db.sqlapi(dbname,'show databases'):
            db.sqlapi(dbname, 'drop database %s'%dbname)
            logging.info('database %s is drop' % dbname)
        else:
            print('database %s does not exist'%dbname)
            logging.warn('database %s does not exist'%dbname)
    else:
        logging.warn('database %s does not exist' % dbname)

    logging.info('------------- database %s drop end' % dbname)


uinstall_atmdb(setting.DBNAME)
init_atmdb(setting.DBNAME)