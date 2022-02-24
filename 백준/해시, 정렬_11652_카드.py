# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
#n = int(input())

dic = {}

for i in range(n):
    tmp = int(sys.stdin.readline())
    #tmp = int(input())
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1
        
#print(dic)
        
cntMax = 0
numList = []

for i in dic.items():
    if cntMax < i[1]:
        numList.clear()
        numList.append(i[0])
        cntMax = i[1]
    elif cntMax == i[1]:
        numList.append(i[0])

numList.sort()

print(numList[0])