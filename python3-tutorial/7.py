#!/usr/bin/env python3
# -*- coding: utf-8 -*-

f = open("6.py")
print(f.read())
f.close()

f = open("1.log", "w")
f.write("This is a log line")
f.close()

# with子句，用完文件自动关闭，不用显式调用close()方法
with open("5.py") as f:
    print(f.read())
print(f.closed)

