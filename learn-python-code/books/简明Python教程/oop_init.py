# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:29
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : oop_init.py
# @Software: PyCharm
class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hello, my name is', self.name)

p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()