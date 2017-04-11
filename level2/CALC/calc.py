

import re



# b = a[1:-1]
# c=[]
# d=''
# for i in b:
#     if i in '*/':
#         c.append(i)
#         d=''
#     elif i in '+-':
#         c.append(i)
#         d = ''
#     else:
#         d+=i
#         if len(c)==0:
#             c.append(d)
#         else:
#             if c[-1] in '*/':
#                 c.append(d)
#             if  '+' in c[-1] or '-' in c[-1]:
#                 c[-1]+=i
#             else:
#                 c[-1]=d
#


def add(*_add):
    _add_r = 0
    for i in _add:
        _add_r+=int(i)
    return str(_add_r)

def subtract(_sub_i1,_sub_i2):
    _sub_r = int(_sub_i1) - int(_sub_i2)
    return str(_sub_r)

def multiply (_mul_i1,_mul_i2):
    _mul_r = int(_mul_i1) * int(_mul_i2)
    return str(_mul_r)

def divide(_div_i1,_div_i2):
    _div_r = int(_div_i1) / int(_div_i2)
    return str(_div_r)

def formula_to_list(formula):
    f_list = []
    d = ''
    for i in formula:
        if i in '*/':
            f_list.append(i)
            d = ''
        elif i in '+-':
            f_list.append(i)
            d = ''
        else:
            d += i
            if len(f_list) == 0:
                f_list.append(d)
            else:
                if f_list[-1] in '*/':
                    f_list.append(d)
                if '+' in f_list[-1] or '-' in f_list[-1]:
                    f_list[-1] += i
                else:
                    f_list[-1] = d
    return f_list

def calc(f_list):
    exit_flag = False
    while not exit_flag:
        if f_list.count('/') >0  :
            f_index = f_list.index('/')
            divide_result=divide(f_list[f_index-1],f_list[f_index+1])
            del f_list[f_index + 1]
            del f_list[f_index ]
            del f_list[f_index - 1]
            f_list.append(str(divide_result))
        elif f_list.count('*') > 0:
            f_index = f_list.index('*')
            multiply_result = multiply(f_list[f_index - 1], f_list[f_index + 1])
            del f_list[f_index + 1]
            del f_list[f_index]
            del f_list[f_index - 1]
            f_list.append(str(multiply_result))
        else:
            add_result=add(f_list)
            exit_flag = True

    return add_result


def core(formula):
    brackets_calc = re.findall(r'\([^()]+\)',formula)
    for i in brackets_calc:
        brackets = i
        result=calc(formula_to_list(i[1:-1]))
        formula = re.sub(brackets,result,formula)

    if re.search(r'\([^()]+\)',formula):
        return core(formula)
    else:
        return calc(formula)


if __name__== '__main__':
    __input = " 1 - 2 * ( (680-30 +(-40/5+3+2*3/2+8-9292) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
    print(core(__input))