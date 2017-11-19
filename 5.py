#!/bin/usr/env python
# coding=utf-8
'''
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
'''

x = raw_input('请输入x:')
y = raw_input('请输入y:')
z = raw_input('请输入z:')
num_list = [x, y, z]
print min(num_list)