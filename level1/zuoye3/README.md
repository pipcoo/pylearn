#程序运行说明
运行zuoye4.py   配置文件是haproxy.cfg 在同一目录下
程序支持 增 删 改 查.运行后按提示操作

查询功能只需要输入域名即可

增 删 改 要求输入格式为：
##### args={'backend':'www.xxx.com','record':{'server':'1.1.1.1','weight':20,'maxconn':3000}}

输入格式不对会有提示  增加时如果 backend 已存在会直接修改
增 删 改 完成后如信息发生改变 会保存一份备份文件。 
