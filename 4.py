#!/bin/usr/env python
# coding=utf-8

'''
题目：输入某年某月某日，判断这一天是这一年的第几天？
'''

year=int(raw_input("年：\n"))
month=int(raw_input("月：\n"))
day=int(raw_input("日：\n"))
months1=[0,31,60,91,121,152,182,213,244,274,305,335,366] #闰年
months2=[0,31,59,90,120,151,181,212,243,273,304,334,365] #平年

if year % 4 == 0:
	if year % 100 == 0:
		if year % 400 == 0:
			print '今年是闰年'
			mounths = months1
		else:
			print '今年是平年'
			mounths = months2
	else:
		print '今年是闰年'
		mounths = months1
else:
	print '今年是平年'
	mounths = months2
print '这是' + str(year) + '年的第' + str(mounths[month - 1] + day) + '天'