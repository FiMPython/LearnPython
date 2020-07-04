# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:28
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : oop_method.py
# @Software: PyCharm
class Person:
    def say_hi(self):
        print('Hello, how are you?')

p = Person()
p.say_hi()
# 前面两行同样可以写作
# Person().say_hi()