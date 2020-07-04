# -*- coding: utf-8 -*-
# @Time : 2020/7/3 13:01
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : module_using_sys.py
# @Software: PyCharm
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

