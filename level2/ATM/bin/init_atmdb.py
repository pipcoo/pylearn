


import os,sys

BASE=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(BASE)

from ext.DB.core import db



def init_atmdb(dbname):
    """
    初始化atm数据库
    :return: 
    """
    db.sqlapi(dbname,'create database %s'%dbname)

    db.sqlapi(dbname,
              'create table account \(userid int auto_increment,username str not null unique,account_status str,password str\)')
    db.sqlapi(dbname,
              'create table party \(party_id int auto_increment,userid int ,card_num str,card_type str,create_time str,card_balance float\)')
    db.sqlapi(dbname,
              'create table transaction_rate \(rate_id int auto_increment,transaction_type str,transaction_rate float\)')
    db.sqlapi(dbname,
              'create table transaction (transaction_id int auto_increment,transaction_type str,party_id int,counterparty_id int,amount float,txdate str)')

def uinstall_atmdb(dbname):
    """
    清理删除atmdb数据库
    :param dbname: 
    :return: 
    """

    if db.sqlapi(dbname,'show databases') is not None:
        if dbname in db.sqlapi(dbname,'show databases'):
            db.sqlapi(dbname, 'drop database %s'%dbname)
        else:
            print('database %s does not exist'%dbname)
    else:
        print('database %s does not exist' % dbname)



uinstall_atmdb('atmdb')
init_atmdb('atmdb')