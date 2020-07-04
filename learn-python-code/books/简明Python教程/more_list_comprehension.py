# -*- coding: utf-8 -*-
# @Time : 2020/7/4 9:42
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : more_list_comprehension.py
# @Software: PyCharm
listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

'''
它是如何工作的

在本案例中，当满足了某些条件时（if i > 2），我们进行指定的操作（2*i），
以此来获得一份新的列表。要注意到原始列表依旧保持不变。

使用列表推导的优点在于，当我们使用循环来处理列表中的每个元素并将其存储到新的
列表中时时，它能减少样板（Boilerplate）代码的数量。
'''