# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

check = [0 for i in range(10000)] 

for i in range(n):
    tmp = int(sys.stdin.readline())
    check[tmp-1] += 1 #수의 범위가 작기 때문에 횟수만 체크해줘도 됨(메모리 절약)
    
for i in range(1, 10001):
    if check[i-1] != 0:
        for j in range(check[i-1]):
            print(i)

