#!/usr/bin/env python3


def fibonacci(n):
    i = 1
    a, b = 0, 1
    while i < n:
        a, b = b, a + b
        i = i + 1

    return b


# 输入前20个fibonacci数列的值
t = 1
while t < 20:
    print(fibonacci(t))
    t = t + 1

