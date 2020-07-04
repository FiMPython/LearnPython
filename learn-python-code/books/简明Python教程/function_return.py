# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:55
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_return.py
# @Software: PyCharm

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y

print(maximum(2, 3))

'''
它是如何工作的

maximum 函数将会返回参数中的最大值，在本例中是提供给函数的数值。
它使用一套简单的 if...else 语句来找到较大的那个值并将其返回。

要注意到如果 return 语句没有搭配任何一个值则代表着 返回 None。
None 在 Python 中一个特殊的类型，代表着虚无。举个例子， 它用于
指示一个变量没有值，如果有值则它的值便是 None（虚无）。

每一个函数都在其末尾隐含了一句 return None，除非你写了你自己的 return 语句。
你可以运行 print(some_function())，其中 some_function 函数不使用 return 语句，
就像这样：

def some_function():
    pass


Python 中的 pass 语句用于指示一个没有内容的语句块。
'''