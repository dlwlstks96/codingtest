# -*- coding: utf-8 -*-

import itertools as it

n = int(input())

for i in range(n):
    num = int(input())
    #print(num)
    
    l = [1, 2, 3] #1,2,3을 중복 허용하여 총합이 num인 경우의 수
    res = []
    #print(l)
    
    for j in range(1, num+1):
        tmp = it.product(l, repeat = j) #1~num+1의 갯수만큼 뽑는다
        for k in tmp:
            if sum(k) == num:
                res.append(k)
                
    print(len(res))