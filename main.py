# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 14:20:09 2023

@author: jungw
"""

##함수 선언부
def add_func(n1, n2):
    return n1 + n2

def sub_func(n1, n2):
    return n1 - n2

def mul_func(n1, n2):
    return n1 * n2

##전역 변수부
num1, num2, res = 100, 200, 0

##메인 코드부
res = add_func(num1, num2)
print(num1, "+", num2, '=', res)

res = sub_func(num1, num2)
print(num1, '-', num2, '=', res)

res = mul_func(num1, num2)
print(num1, 'x', num2, '=', res)
