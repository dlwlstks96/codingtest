# -*- coding: utf-8 -*-

import sys
import itertools as it

a, b = map(int, sys.stdin.readline().split())
# a, b = 789, 123

a = list(str(a))


num_list = []
res = it.permutations(a,len(a)) #순열
for r in res:
    #print(r)
    tmp = ''
    for i in r:
        tmp += i
    if tmp[0] != '0':
        num_list.append(int(tmp))
    
num_list.sort(reverse = True)

#print(num_list)

answer = -1
for n in num_list:
    if n < b:
        answer = n
        break
    
print(answer)