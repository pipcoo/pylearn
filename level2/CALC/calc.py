#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
@version: 0.1
@author: wufeng
@contact: pipcoo@pipcoo.com
@site: http://www.pipcoo.com
@software: PyCharm
@file: key_obtain.py
@time: 2017/4/11 22:21
"""

import re


def add(_add):
    """
    加法计算
    :param _add: 输入要计算的列表
    :return:     返回计算结果
    """
    _add_r = 0
    for i in _add:
        _add_r+=float(i)
    return str(_add_r)

def subtract(_sub_i1,_sub_i2):
    """
    减法计算
    :param _sub_i1: 减数
    :param _sub_i2: 被减数
    :return: 
    """
    _sub_i1=_sub_i1.replace(' ','')
    _sub_i2=_sub_i2.replace(' ','')
    _sub_r = float(_sub_i1) - float(_sub_i2)
    return str(_sub_r)

def multiply (_mul_i1,_mul_i2):
    """
    乘法计算
    :param _mul_i1: 乘数
    :param _mul_i2: 被乘数
    :return: 
    """
    _mul_i1 = _mul_i1.replace(' ','')
    _mul_i2 = _mul_i2.replace(' ','')
    _mul_r = float(_mul_i1) * float(_mul_i2)
    return str(_mul_r)

def divide(_div_i1,_div_i2):
    """
    除法计算
    :param _div_i1: 除数
    :param _div_i2: 被除数
    :return: 
    """
    _div_i1 = _div_i1.replace(' ','')
    _div_i2 = _div_i2.replace(' ','')
    _div_r = float(_div_i1) / float(_div_i2)
    return str(_div_r)

def formula_to_list(formula):
    """
    将计算式转换成列表
    :param formula:  输入计算式
    :return: 返回列表
    """
    if re.match('\(.*\)\Z',formula):    #判断 如果输入的计算式带括号 则去除
        formula = formula[1:-1]

    f_list = []
    d = ''
    for i in formula:
        if i in '*/+-':                      # 有计算符号添加到列表中
            f_list.append(i)
            d = ''
        elif i == ' ':                       # 去除空格
            pass
        else:
            d+=i
            if len(f_list) == 0:             # 第一次直接插入
                f_list.append(d)
            else:
                if f_list [ -1 ] in '*/':   # 有乘除计算符号跳过
                    f_list.append(d)
                if '+' in f_list[-1] or '-' in f_list[-1]:      # 列表左后一个值第一个值是加减符号则在此基础上拼接
                    f_list[-1]+= i
                else:
                    f_list[-1] = d              # 列表最后一个值非计算符开头 拼接添加
    return f_list

def _del(f_list,f_index):
    """
    列表元素删除
    :param f_list: 输入列表
    :param f_index: 输入要删除的 计算福的位置
    :return: 
    """
    del f_list[f_index + 1]
    del f_list[f_index]
    del f_list[f_index - 1]
    return f_list

def calc(f_list):
    """
    计算
    :param f_list: 输入列表
    :return: 
    """
    exit_flag = False
    while not exit_flag:

        if f_list.count('/') >0  :                                     #判断列表包含 /
            f_index = f_list.index('/')
            divide_result=divide(f_list[f_index-1],f_list[f_index+1])   #计算
            f_list=_del(f_list,f_index)
            f_list.insert(f_index-1,str(divide_result))                 #插回计算结果
        elif f_list.count('*') > 0:
            f_index = f_list.index('*')
            multiply_result = multiply(f_list[f_index - 1], f_list[f_index + 1])
            f_list = _del(f_list, f_index)
            f_list.insert(f_index-1,str(multiply_result))
        elif f_list.count('-') > 0:
            f_index = f_list.index('-')
            subtract_result = subtract(f_list[f_index - 1], f_list[f_index + 1])
            f_list = _del(f_list, f_index)
            f_list.insert(f_index-1,str(subtract_result))
        else :
            if f_list.count('+') >0:                                    #如果计算符号是加号 清除
                f_index = f_list.index('+')
                del f_list[f_index]
            add_result=add(f_list)                                       #计算完所有乘除减 将列表所有值相加
            exit_flag = True

    return add_result


def core(formula):
    """
    括号计算判断
    :param formula: 
    :return: 
    """

    if re.search(r'\([^()]+\)',formula):                            #判断计算式中是否有括号
        brackets_calc = re.search(r'\([^()]+\)', formula).group(0)

        result = calc(formula_to_list(brackets_calc))                 #计算最内侧括号

        formula = re.sub(r'\([^()]+\)', result, formula, 1)         #计算完替换
        #print(formula)
        return core(formula)                                         #递归计算
    else:
        return calc(formula_to_list(formula))                        #计算式不包含括号直接计算


if __name__== '__main__':
    exit_flag = False
    while not exit_flag :
        __input = input('请输入计算式 【按q退出】\n >>')
        if __input =='q':
            exit_flag = True
        elif re.search('[A-Za-z]+',__input):
            print('请输入正确的计算式！')
        else:
            print('计算结果：%s'%(core(__input)))


