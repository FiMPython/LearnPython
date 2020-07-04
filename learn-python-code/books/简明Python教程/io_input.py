# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:43
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : io_input.py
# @Software: PyCharm

def reverse(text):
    return text[::-1]


def is_palindrome(text):
    return text == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes, it is a palindrome")
else:
    print("No, it is not a palindrome")