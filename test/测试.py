# -*- coding:utf-8 -*-
# @---wufeng---






def addspam(func):
    def new(*args):
        print ("spam,spam,spam")
        return func(*args)
    return new


# @addspam
def useful(a,b):
    print (a**2+b**2)


addspam(usefu)

useful(4,3)
