# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:53
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : function_varargs.py
# @Software: PyCharm


def total(a=5, *numbers, **phonebook):
    print('a', a)

    #遍历元组中的所有项目
    for single_item in numbers:
        print('single_item', single_item)

    #遍历字典中的所有项目
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

'''
它是如何工作的

当我们声明一个诸如 *param 的星号参数时，
从此处开始直到结束的所有位置参数（Positional Arguments）都将被收集并汇集成
一个称为“param”的元组（Tuple）。

类似地，当我们声明一个诸如 **param 的双星号参数时，
从此处开始直至结束的所有关键字参数都将被收集并汇集成一个名为 param 的字典（Dictionary）。

'''