#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 学习python的字符串和编码相关知识
# 最新的Python 3版本中，字符串是以Unicode编码的，也就是说python支持多语言

# 对于单个字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
# ord()、chr()相当于一对互逆操作
a = 'A'
b = '中'

print(ord(a))  # 65
print(ord(b))  # 20013

print(chr(ord(a)))  # A
print(chr(ord(b)))  # 中

print('%x %x' % (ord('中'), ord('文')))  # 4e2d 6587  算出'中文'这两个字分别的unicode编码值

# 如果知道对应的字符串的unicode编码，还可以直接这么写字符串，前缀u表示Unicode编码
print('\u4e2d\u6587')  # 中文

# Python的字符串类型是str，在内存中以Unicode表示，但是如果要保存在文件或者在网络中传输，需要转化为字节，也就是byte类型
# byte类型在python中以b作为前缀
print(b'ABC')  # b'ABC'为byte类型的值

# 以Unicode表示的str通过encode()方法可以编码为指定的bytes
print('ABC'.encode('ascii'))   # b'ABC'
print('中文'.encode('utf-8'))  # b'\xe4\xb8\xad\xe6\x96\x87'
print('中文'.encode())         # b'\xe4\xb8\xad\xe6\x96\x87', python3 encode默认为utf-8

# encode 对应的方法是 decode
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))  # 中文
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode())         # 中文

# 计算str包含多少个字符，可以用len()函数
print(len('中文'))  # 2
print(len('ABC'))  # 3


'''
由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，在保存源代码时，就需要务必指定保存为UTF-8编码。
当Python解释器读取源代码时，为了让它按UTF-8编码读取，我们通常在文件开头写上这两行：

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

从本文件的开头即可以看到

第一行注释是为了告诉Linux/OS X系统，这是一个Python可执行程序，Windows系统会忽略这个注释；
第二行注释是为了告诉Python解释器，按照UTF-8编码读取源代码，否则，你在源代码中写的中文输出可能会有乱码。
'''


# 字符串的格式化
# 在Python中，采用的格式化方式和C语言是一致的，用%实现
# %运算符就是用来格式化字符串的。
# 在字符串内部，%s表示用字符串替换，%d表示用整数替换，
# 有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略
print('Hello %d' % 18)  # Hello 18
print('Hello %s' % 'world')  # Hello world
print('Hello %s, happy %d' % ('xiaoming', 18))  # Hello xiaoming, happy 18

# 其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：
print('%2d-%02d' % (3, 1))  # ' 3-01'
print('%.2f' % 3.1415926)   # '3.14'

# 如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：
print('Age: %s. Gender: %s' % (25, True))  # 'Age: 25. Gender: True'

# 有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：
print('growth rate: %d %%' % 7)  # 'growth rate: 7 %'


# 练习题
'''
小明的成绩从去年的72分提升到了今年的85分，请计算小明成绩提升的百分点，并用字符串格式化显示出'xx.x%'，只保留小数点后1位：
'''
s1 = 72
s2 = 85
print("%.1f %%" % ((s2 - s1) * 100 / s1))  # 18.1  发现 %f 还会进行四舍五入
print("%.2f %%" % ((s2 - s1) * 100 / s1))  # 18.06

