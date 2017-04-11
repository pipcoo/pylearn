
import re


def add(_add):
    _add_r = 0
    for i in _add:
        _add_r+=float(i)
    return str(_add_r)

def subtract(_sub_i1,_sub_i2):
    _sub_i1=_sub_i1.replace(' ','')
    _sub_i2=_sub_i2.replace(' ','')
    _sub_r = float(_sub_i1) - float(_sub_i2)
    return str(_sub_r)

def multiply (_mul_i1,_mul_i2):
    _mul_i1 = _mul_i1.replace(' ','')
    _mul_i2 = _mul_i2.replace(' ','')
    _mul_r = float(_mul_i1) * float(_mul_i2)
    return str(_mul_r)

def divide(_div_i1,_div_i2):
    _div_i1 = _div_i1.replace(' ','')
    _div_i2 = _div_i2.replace(' ','')
    _div_r = float(_div_i1) / float(_div_i2)
    return str(_div_r)

def formula_to_list(formula):
    if re.match('\(.*\)\Z',formula):
        formula = formula[1:-1]

    f_list = []
    d = ''
    for i in formula:
        if i in '*/':
            f_list.append(i)
            d = ''
        elif i in '+-':
            f_list.append(i)
            d = ''
        elif i == ' ':
            pass
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
            f_list.insert(f_index-1,str(divide_result))
        elif f_list.count('*') > 0:
            f_index = f_list.index('*')
            multiply_result = multiply(f_list[f_index - 1], f_list[f_index + 1])
            del f_list[f_index + 1]
            del f_list[f_index ]
            del f_list[f_index - 1]
            f_list.insert(f_index-1,str(multiply_result))
        elif f_list.count('-') > 0:
            f_index = f_list.index('-')
            subtract_result = subtract(f_list[f_index - 1], f_list[f_index + 1])
            del f_list[f_index + 1]
            del f_list[f_index ]
            del f_list[f_index - 1]
            f_list.insert(f_index-1,str(subtract_result))
        else :
            if f_list.count('+') >0:
                f_index = f_list.index('+')
                del f_list[f_index]

            add_result=add(f_list)
            exit_flag = True

    return add_result


def core(formula):

    if re.search(r'\([^()]+\)',formula):
        brackets_calc = re.search(r'\([^()]+\)', formula).group(0)

        result = calc(formula_to_list(brackets_calc))

        formula = re.sub(r'\([^()]+\)', result, formula, 1)
        #print(formula)
        return core(formula)
    else:
        return calc(formula_to_list(formula))


if __name__== '__main__':
    __input = "1-11*(1-11*(1-11*(1-11*(1-11*(1-11*(1-11*(1111-333)))))))"
    print(core(__input))


