'''
1.使用while 循环 输出 2-3+4-5 ... +100
2.将列表['alax','eric','rain'] 中每一个元素使用'_' 连接为一个字符串
3.n='老男孩' 将a转换成 utf-8 的字节 再将 转换的字节重新转换为 utf-8 字符


'''
#1
n = 2
count = 0
while n <=100 :
    if (n%2) == 0 :
        count += n
    else:
        count -= n
    n += 1
print(count)

#2
a=['alax','eric','rain']
alist = "_".join(a)
print(alist)

#3
n='老男孩'

b_utf8=n.encode("utf-8")
b_str=b_utf8.decode("utf-8")
print(b_str)


s = "你是风儿%%我是沙%s"
n=s%('僧')
print(n)

print("%%%s"%'22')