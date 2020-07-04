# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:45
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : break.py
# @Software: PyCharm
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    print('Length of the string is', len(s))
print('Done')