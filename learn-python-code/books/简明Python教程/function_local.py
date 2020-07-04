# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:49
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_local.py
# @Software: PyCharm
x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)


func(x)
print('x is still', x)