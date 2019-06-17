#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 理解一下python的代码执行过程
'''  result:
1
2
myclass
lssssss
main
'''


print("1")


def f1():
    print("f1")


print("2")


def main():
    print("main")


class MyClass:
    print("myclass")

    def __init__(self):
        print("MyClass init")

    print("lssssss")


if __name__ == '__main__':
    main()

