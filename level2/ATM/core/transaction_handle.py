from DB.core import db

a = db.sqlapi('emp','select * from staff_table')
b = db.sqlapi('emp','insert into staff_table (name) values \(\'li\'\)')
print (a)
print (b)