# -*- coding: utf-8 -*-

n = int(input())

if n < 3:
    print(1)
else:
    prevN = [1, 0]
    for i in range(2, n):
        res = [sum(prevN), prevN[0]]
        prevN = res
    print(sum(res))
    

'''

1 0 

n=1, [0, 1]
n=2, [1, 0]
n=3, [1, 1]
n=4, [2, 1]
n=5, [3, 2]
n=6, [5, 3]
n=7, [8, 5]


10

1*1*2*

101
100

011 X



'''