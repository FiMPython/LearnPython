# -*- coding: utf-8 -*-
# @Time : 2020/7/3 19:13
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : exceptions_handle.py
# @Software: PyCharm

try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:
    print('You entered {}'.format(text))