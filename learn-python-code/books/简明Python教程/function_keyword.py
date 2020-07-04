# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:52
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_keyword.py
# @Software: PyCharm
def func(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)

func(3, 7)
func(25, c=24)
func(c=50, a=100)