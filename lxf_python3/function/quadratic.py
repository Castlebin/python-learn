#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 求一元二次方程的解

import math
import sys


def quadratic(a, b, c):
    condition = b ** 2 - 4 * a * c
    print(b, ' ** 2 - 4 * ', a, ' * ', c, '(b**2 - 4*a*c) = ', condition)
    if condition < 0:
        print('b ** 2 - 4 * a * c < 0, 无解')
        raise ValueError('input error, 无解')
    if a == 0:
        return -(b / c)  # 可以看到，python函数可以返回多种值类型（动态与语言这个特性真让人不安）
    elif condition == 0:
        return -b / (2 * a)
    else:
        return (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a, (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a


def input_cal():
    try:
        print('请输入一元二次方程中的a、b、c三个参数(a * x**2 + b*x + c = 0 )')
        a = float(input('a: '))
        b = float(input('b: '))
        c = float(input('c: '))
        print(a, ' * x**2 + ', b, ' * x + ', c, ' = 0 的解为：', quadratic(a, b, c))
    except ValueError:
        print("error:", sys.exc_info()[0])


while True:
    input_cal()

