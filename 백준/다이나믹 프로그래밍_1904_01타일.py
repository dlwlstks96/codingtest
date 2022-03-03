# -*- coding: utf-8 -*-

'''

2 = 2
3 = 3
4 = 5
5 = 8
6 = 13

'''

import sys

n = int(sys.stdin.readline())
#n = int(input())

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    data = [0] * 1000001
    data[1] = 1
    data[2] = 2
    for i in range(3, n+1):
        data[i] = (data[i-1] + data[i-2]) % 15746
        
    print(data[n])