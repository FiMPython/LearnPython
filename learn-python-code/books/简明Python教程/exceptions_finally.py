# -*- coding: utf-8 -*-
# @Time : 2020/7/3 19:16
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : exceptions_finally.py
# @Software: PyCharm

import sys
import time

f = None
try:
    f = open("poem.txt")
    # 我们常用的文件阅读风格
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        # 使用了 sys.stout.flush()，以便它能被立即打印到屏幕上。
        sys.stdout.flush()
        print("Press ctrl+c now")
        # 为了确保它能运行一段时间
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally:
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")