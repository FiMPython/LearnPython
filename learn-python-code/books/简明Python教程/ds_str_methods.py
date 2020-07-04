# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:12
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : ds_str_methods.py
# @Software: PyCharm

# 这是一个字符串对象
name = 'Swaroop'

if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')

if 'a' in name:
    print('Yes, it contains the string "a"')

if name.find('war') != -1:
    print('Yes, it contains the string "war"')

delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))