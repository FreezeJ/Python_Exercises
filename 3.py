#!/bin/usr/env python
# coding=utf-8
'''
题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
'''
# 通用办法(运算量较大)
import math
n = 0
while True:
	if (n + 1) ** 2 - n ** 2 > 168: break
	n += 1
print '可能的范围为',n
i = -100
while True:
	i += 1
	if i > n ** 2: break
	result1 = math.sqrt(i  + 100)
	if result1 - int(result1) != 0:
		continue
	result2 = math.sqrt(i  + 100 + 168)
	if result2 - int(result2) != 0:
		continue
	print "符合条件的整数有:", i

# 比较简便的办法（需要经过一定数学运算得出公式）

for m in range(168):
    for n in range(m):
        if (m+n)*(m-n)==168:
            x=n**2-100
            print "符合条件的整数有:",x
