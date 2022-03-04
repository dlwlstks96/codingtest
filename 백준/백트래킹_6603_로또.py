# -*- coding: utf-8 -*-

import itertools as it

answer = []

while True:
    data = list(map(int, input().split()))
    if data[0] == 0:
        break
    data = data[1:]
    res = it.combinations(data, 6)
    tmp = []
    for i in res:
        tmp.append(i)
    answer.append(tmp)
    
for i in answer:
    for j in i:
        for k in range(len(j)):
            if k != len(j)-1:
                print(j[k], end = ' ')
            else:
                print(j[k])
    print()