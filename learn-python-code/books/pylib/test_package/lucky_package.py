# -*- coding: utf-8 -*-
# @Time : 2020/7/3 13:40
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : lucky_package.py
# @Software: PyCharm

# 导入random模块，我们要制作的包要用
import random


# 定义自定义包模块的简单功能
def test():
    print(random.randint(1, 10))
    return ('hello world')


def say_hi():
    print('Hi, this is mymodule speaking.')

__version__ = '0.1'