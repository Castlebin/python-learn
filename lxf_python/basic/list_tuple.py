#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 使用list和tuple

# list是一种有序的集合，可以随时添加和删除其中的元素。
classmates = ['Michael', 'Bob', 'Lee']
print(classmates)  # ['Michael', 'Bob', 'Lee']
print(len(classmates))  # 3

# 用索引来访问list中每一个位置的元素，记得索引是从0开始的, 记住数组不能越界
print(classmates[0])  # Michael
print(classmates[1])  # Bob
# print(classmates[4])  # IndexError: list index out of range

# -1可以表示倒数第一个位置的元素，类似的-2表示倒数第二个，依次类推，但记住同样的也不能越界了
print(classmates[-1])  # Lee
# print(classmates[-4])  # IndexError: list index out of range

# list是一个可变的有序表，所以，可以往list中追加元素到末尾，使用append方法
classmates.append('Adam')
print(classmates)  # ['Michael', 'Bob', 'Lee', 'Adam']

# 也可以将元素插入到list的指定的位置
classmates.insert(1, 'LiLei')
print(classmates)  # ['Michael', 'LiLei', 'Bob', 'Lee', 'Adam']

# 要删除list末尾的元素，用pop()方法  (list这个特性可以当做栈来用了)
classmates.pop()
print(classmates)  # ['Michael', 'LiLei', 'Bob', 'Lee']

# 当然，也可以删除指定位置的元素，同样的使用pop方法，不过方法需要传入一个参数
classmates.pop(1)  # 删除了index位置为1的元素
print(classmates)  # ['Michael', 'Bob', 'Lee']

# 要把某个元素替换成别的元素，可以直接赋值给对应的索引位置（就是个数组）
classmates[1] = 'HanMeimei'
print(classmates)  # ['Michael', 'HanMeimei', 'Lee']

# list里面的元素甚至类型可以不一样，eg
L = ['Apple', 123, True]
print(L)  # ['Apple', 123, True]

# list元素也可以是另一个list(类似于java里面的数组，数组里元素也可以再是另外一个数组)
s = ['python', 'java', ['asp', '.net'], 'scala', 11111]
print(s)  # ['python', 'java', ['asp', '.net'], 'scala', 11111]

# 空list
L = []
print(len(L))  # 0


# 另一种有序列表叫元组：tuple。tuple和list非常类似，但是tuple一旦初始化就不能修改 (类似java里的不可变集合)
classmates = ('Michael', 'Bob', 'Tracy')
print(classmates)   # ('Michael', 'Bob', 'Tracy')

classmates = ()  # 空tuple
print(classmates)  # ()

# 要初始化只有一个元素的tuple稍微有点特殊了，必须在后面额外加一个,号（因为语法上和括号表达式有歧义，所以需要区分开来）
classmates = ('lei')  # 被当做括号表达式了，现在classmates变量的类型是str
print(type(classmates))  # <class 'str'>

# 这才是正确声明一个只有一个元素的tuple的姿势
classmates = ('lei',)
print(type(classmates))  # <class 'tuple'>
# Python在显示只有1个元素的tuple时，也会加一个逗号,，以免你误解成数学计算意义上的括号
print(classmates)  # ('lei',)


'''
练习题：
请用索引取出下面list的指定元素：
# -*- coding: utf-8 -*-

L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

# 打印Apple:
print(?)
# 打印Python:
print(?)
# 打印Lisa:
print(?)

'''
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])
