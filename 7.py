#!/bin/usr/env python
# coding=utf-8

'''
题目：将一个列表的数据复制到另一个列表中。
'''

a = [1, 2, 3]
print id(a)
b = a[:]  # 浅copy
print id(b)
c = a  # 深copy
print id(c)
d = a[::-1] # 倒序
print b
print d