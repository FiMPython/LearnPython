# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:48
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_param.py
# @Software: PyCharm
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')

# 直接传递字面值
print_max(3, 4)

x = 5
y = 7

# 以参数的形式传递变量
print_max(x, y)