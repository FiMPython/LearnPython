# -*- coding: utf-8 -*-
# @Time : 2020/7/3 14:06
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : test_package_demo.py
# @Software: PyCharm

import test_package.lucky_package

test_package.lucky_package.say_hi()
print('Version', test_package.lucky_package.__version__)


from test_package.lucky_package import say_hi, __version__

say_hi()
print('Version', __version__)