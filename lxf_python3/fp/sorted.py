#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['bob', 'about', 'Zoo', 'Credit']
s = sorted(L, key=str.lower, reverse=True)
print(s)  # ['Zoo', 'Credit', 'bob', 'about']
print(L)  # ['bob', 'about', 'Zoo', 'Credit']  可见并不是直接改变了原来的list，而是生成了一个新的排序过的list

print(sorted(L))  # ['Credit', 'Zoo', 'about', 'bob']
print(L)          # ['bob', 'about', 'Zoo', 'Credit']  可见并不是直接改变了原来的list，而是生成了一个新的排序过的list

print(sorted(L, key=str.lower))  # ['about', 'bob', 'Credit', 'Zoo']
