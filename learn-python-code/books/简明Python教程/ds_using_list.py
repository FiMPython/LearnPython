# -*- coding: utf-8 -*-
# @Time : 2020/7/3 15:03
# @Author : yuhui.Mr
# @Email : 1299824045@qq.com
# @File : ds_using_list.py
# @Software: PyCharm

# This is my shopping list
shoplist = ['apple', 'mango', 'carrot', 'banana']

print('I have', len(shoplist), 'items to purchase.')

print('These items are:', end=' ')
for item in shoplist:
    print(item, end=' ')

print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)

print('I will sort my list now')
'''
列表的 sort 方法对列表进行排序。在这里要着重理解到这一方法影响到的是列表本身，
而不会返回一个修改过的列表——这与修改字符串的方式并不相同。同时，这也是我们所说的，
列表是可变的（Mutable）而字符串是不可变的（Immutable）。
'''
shoplist.sort()
print('Sorted shopping list is', shoplist)

print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)