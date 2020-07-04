# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:23
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : str_format.py
# @Software: PyCharm

age = 20

name = 'Swaroop'

print('{0} was {1} years old when he wrote this book'.format(name, age))

print('Why is {0} playing with that python?'.format(name))

# 对于浮点数 '0.333' 保留小数点(.)后三位
print('{0:.3f}'.format(1.0/3))
# 使用下划线填充文本，并保持文字处于中间位置
# 使用 (^) 定义 '___hello___'字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))

'''
由于我们正在讨论格式问题，就要注意 print 总是
会以一个不可见的“新一行”字符（\n）结尾，因此重
复调用 print将会在相互独立的一行中分别打印。为
防止打印过程中出现这一换行符，你可以通过 end 指定其应以空白结尾：
'''
print('a', end='')
print('b', end=' ')