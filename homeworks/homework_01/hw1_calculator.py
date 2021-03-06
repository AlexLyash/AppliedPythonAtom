#!/usr/bin/env python
# coding: utf-8


def calculator(x, y, operator):
    '''
    Простенький калькулятор в прямом смысле. Работает c числами
    :param x: первый агрумент
    :param y: второй аргумент
    :param operator: 4 оператора: plus, minus, mult, divide
    :return: результат операции или None, если операция не выполнима
    '''

#    if isinstance(x,str): x = int(x)
#    if isinstance(y,str): y = float(y)
    if not isinstance(x, (int,float)): return None
    if not isinstance(y, (int,float)): return None 

    if operator == "plus":
        return x + y
    elif operator == "minus":
        return x - y
    elif operator == "divide":
        if y != 0:
            return x / y
        else:
            return None
    elif operator == "mult":
        return x * y
    else:
        return None
    #raise NotImplementedError

