# -*- coding: utf-8 -*-
# @Time : 2020/7/3 12:46
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : continue.py
# @Software: PyCharm
while True:
    s = input('Enter something : ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # 自此处起继续进行其它任何处理