
博客地址http://wwww.blcat.cc  (备案没文成 可能看不了)
详细描述参考http://www.cnblogs.com/alex3714/articles/5740985.html
有以下员工信息表
当然此表你在文件存储时可以这样表示
1,Alex Li,22,13651054608,IT,2013-04-01
insert into staff_table values ('',Alex Li,22,13651054608,IT,2013-04-01)
现需要对这个员工信息文件，实现增删改查操作

可进行模糊查询，语法至少支持下面3种:
    select name,age from staff_table where age > 22
    select * from staff_table where dept = "IT"
    select * from staff_table where enroll_date like "2013"
查到的信息，打印后，最后面还要显示查到的条数
可创建新员工纪录，以phone做唯一键，staff_id需自增
可删除指定员工信息纪录，输入员工id，即可删除
可修改员工信息，语法如下:
    UPDATE staff_table SET dept="Market" WHERE where dept = "IT"
 意：以上需求，要充分使用函数，请尽你的最大限度来减少重复代码！
 
程序主要功能
 
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