### 作业要求

ATM：模拟实现一个ATM + 购物商城程序

- 额度 15000或自定义
实现购物商城，买东西加入 购物车，调用信用卡接口结账
可以提现，手续费5%
支持多账户登录
支持账户间转账
记录每月日常消费流水
提供还款接口
ATM记录操作日志
提供管理接口，包括添加账户、用户额度，冻结账户等。。。
用户认证用装饰器

### 实现功能 

- 第一次运行需要  执行 init_atmdb.py 进行初始化数据库 初始化之前可以编辑查看config目录下的setting.py文件中的参数 。保存后运行初始化可将费率等基本信息初始化到数据库中。

- 执行atm_start.py 运行atm的功能  第一次运行只有管理员可以登录 账号 admin  密码 admin  进行开户操作后 可以使用开户的用户密码进场常规用户登录操作。 
本程序底层支持一个用户多个账户 即多张卡 多个类型的卡片 目前只实现了一个卡的开户以及 一种信用卡片的开户 

- 执行shoppint_start.py  运行购物功能，该模块沿用上一阶段作业的购物车程序，在结算模块加入采用ATM结算，登录用户 可以使用 liyang 密码 123  进行测试
会直接调用ATM接口程序进行结算，atm结算时需要输入atm用户的账号密码 认证通过选择卡号支付。

- 本程序数据库模块采用 上一个作业开发的 数据库。 直接将数据保存到文件中， 用到的表如下：


### 表结构

- 用户信息表 account

userid|username|account_status|password|rule|create_time
---|---|---|---|---|---
用户id|用户名|用户状态|密码|角色|创建时间

- 账户信息表 party

party_id|userid|card_num|card_type|create_time|card_balance|card_limit
---|---|---|---|---|---|---
账户ID|用户ID|账户号|账户类型|开户时间|账户余额|账户额度

- 交易费率表  transaction_rate 

rate_id|transaction_type|transaction_rate
---|---|---|---
费率id|交易类型|交易费率|

- 交易流水表 transaction

transaction_id|transtaction_type|party_id|counterparty_id|amount|tx_amount_dis|txdate|txdesc
---|---|---|---|---|---|---|---|---
交易编码|交易类型|账户id|交易对手id|金额|交易金额|交易时间|交易描述



### 目录结构

ATM.
│  README.md
│
├─bin
│      account.txt
│      atm_start.py					atm 启动入口
│      init_atmdb.py				atm 数据库初始化
│      shoppint_start.py			购物商城程序 启动入口
│      __init__.py
│
├─config
│      logger.py					日志配置
│      setting.py					参数配置
│      __init__.py
│
├─core
│      atm.py						atm各模块
│      auth.py						认证
│      db_handle.py					数据库处理
│      main.py						主入口
│      payapi.py					支付接口
│      transaction_handle.py		交易处理
│      __init__.py
│
├─ext								扩展模块目录
│  │  __init__.py
│  │
│  ├─DB								数据库模块
│  │  │  README.md
│  │  │
│  │  ├─bin
│  │  │      apitest.py
│  │  │      dbstart.py
│  │  │      __init__.py
│  │  │
│  │  ├─core
│  │  │      command_handle.py
│  │  │      db.py
│  │  │      dbfile_handle.py
│  │  │      key_handle.py
│  │  │      __init__.py
│  │  │
│  │  └─data
│  │      │  __init__.py
│  │      │
│  │      └─atmdb
│  │              account.tbf
│  │              party.tbf
│  │              transaction.tbf
│  │              transaction_rate.tbf
│  │
│  └─shopping						购物商城模块
│          account.txt
│          shopping.py
│
└─logs								日志文件夹
        atm.logs					日志文件
		
		
-日志文件保存在 logs 目录下

##### 博客地址：http://www.blcat.cc   (备案尚未完成 可能看不到)