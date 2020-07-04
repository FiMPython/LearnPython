# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:49
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_global.py
# @Software: PyCharm


x = 50

def func():
    global x

    print('x is', x)
    x = 2
    print('Changed global x to', x)


func()
print('Value of x is', x)

'''
如果你想给一个在程序顶层的变量赋值（也就是说它不存在于任何作用域中，无论是函数还是类），
那么你必须告诉 Python 这一变量并非局部的，而是全局（Global）的。我们需要
通过 global 语句来完成这件事。因为在不使用 global 语句的情况下，
不可能为一个定义于函数之外的变量赋值。

你可以使用定义于函数之外的变量的值（假设函数中没有具有相同名字的变量）。然而
，这种方式不会受到鼓励而且应该避免，因为它对于程序的读者来说是含糊不清的，
无法弄清楚变量的定义究竟在哪。而通过使用 global 语句便可清楚看出这
一变量是在最外边的代码块中定义的。

'''