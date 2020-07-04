# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:38
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : expression.py
# @Software: PyCharm

length = 5
breadth = 2

area = length * breadth
print('Area is', area)
print('Perimeter is', 2 * (length + breadth))

'''
它是如何工作的

矩形的长度（Length）与宽度（Breadth）存储在以各自名称命名的变量中。
我们使用它们并借助表达式来计算矩形的面积（Area）与周长（Perimeter）。
我们将表达式 length * breadth 的结果存储在变量 area 中并将其通过使
用 print 函数打印出来。在第二种情况中，我们直接在 print 函数中使用
了表达式 2 * (length + breadth) 的值。

同时，你需要注意到 Python是如何漂亮地打印出 输出结果的。尽管我们没有
特别在 Area is 和变量 area 之间指定空格，Python 会帮我
们加上所以我们就能得到一个整洁的输出结果，同时程序也因为这样的处理方
式而变得更加易读（因为我们不需要在用以输出的字符串中考虑空格问题）。这
便是一个 Python 是如何让程序员的生活变得更加便捷美好的范例。
'''