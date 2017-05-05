# 运行说明
- 作业要求
详细描述参考http://www.cnblogs.com/alex3714/articles/5740985.html
有以下员工信息表
当然此表你在文件存储时可以这样表示
1,Alex Li,22,13651054608,IT,2013-04-01
insert into staff_table values ('',Alex Li,22,13651054608,IT,2013-04-01)
现需要对这个员工信息文件，实现增删改查操作

- 可进行模糊查询，语法至少支持下面3种:
    - select name,age from staff_table where age > 22
    - select * from staff_table where dept = "IT"
    - select * from staff_table where enroll_date like "2013"
- 查到的信息，打印后，最后面还要显示查到的条数
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
    - UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
- 以上需求，要充分使用函数，请尽你的最大限度来减少重复代码！
 
### 程序主要功能实现
###### 具有增删改查 功能  
###### 运行 bin目录下的  dbstart.py   
###### 只在 python 3.0以上版本测试铜锅 2.x版本没有测试
###### 数据类型支持 str int float
###### 建表语句支持 非空 (关键字 not null) 唯一 (关键字 unique)  自增(关键字 auto_increment)
###### 支持的语句如下
- create database xxx
- create table xxx （xxx int auto_increment not null unique,name str )
- select * from xxx
- select * from xxx where xxx= xxx
- select * from xxx where xxx= xxx and xxx=xxx
- insert into xxx values(xxx,xxx,xxx)
- insert into (xxx,xx,xx) values (xxx,xx,xxx)
- update xxx set xxx=xxx 
- update xxx set xxx=xxxx where xxx=xxx
- delete table xxx
- delete table xxx where xxx=xxxx
- drop table xxx
- drop database xxx
- show databases
- show tables
- use database xxx

where 条件判断符号 支持 > < >= <= = like  支持 and 叠加筛选

###### 运行需要先建库 
###### 然后再切换到数据库 切换命令 use database xxx 再做查询

###### 本代码实现了查询api接口 调用接口 需要 from core import db db.sqlapi 函数可实现接口调用 同样支持上述命令
 
### 目录结构
DB.
│  README.md
│
├─bin
│      apitest.py       接口测试
│      dbstart.py       主入口
│      __init__.py
│
├─core                      主要代码
│      command_handle.py    命令行处理
│      db.py                
│      dbfile_handle.py     数据文件处理
│      key_handle.py
│      __init__.py
│
└─data                      数据存放
    │  __init__.py
    │
    ├─atmdb                 数据库目录
    │      account.tbf      表存储
    │
    └─emp                   数据库目录
            staff_table.tbf  表存储
            
            
##### 博客地址http://wwww.blcat.cc  (备案没文成 可能看不了)