#!/usr/bin/env python3


# 循环的else子句（只要循环没有经过break，那么在循环语句完毕后，会执行循环的else子句（没进入过循环也算，同样会执行else））
for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, ' * ', n//x)
            break
    else:   # 注意，这里else是for的子句，而不是if的
        print(n, 'is a prime number.')

