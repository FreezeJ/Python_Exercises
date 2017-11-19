#!/bin/usr/env python
# coding=utf-8

'''
题目：斐波那契数列。
'''

def Fib(n):
	a, b = 0, 1
	if n == 1:return 0
	if n == 2:return 1
	for i in range(n-1):
		c = a + b
		a, b = b, c
	return c

print Fib(11)