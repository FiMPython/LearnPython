# -*- coding: utf-8 -*-
# @Time : 2020/7/3 19:19
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : exceptions_using_with.py
# @Software: PyCharm
'''
在 try 块中获取资源，然后在 finally 块中释放资源是一种常见的模式。
因此，还有一个 with 语句使得这一过程可以以一种干净的姿态得以完成。

'''
with open("poem.txt") as f:
    for line in f:
        print(line, end='')