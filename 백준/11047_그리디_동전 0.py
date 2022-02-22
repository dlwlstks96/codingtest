# -*- coding: utf-8 -*-

n, k = map(int, input().split())

data = []

for i in range(n):
    tmp = int(input())
    data.append(tmp)
    
answer = 0
    
for i in range(len(data)-1, -1, -1):
    tmp = k // data[i]
    #print(k, data[i], tmp)
    k -= data[i] * tmp
    answer += tmp
    
print(answer)
    