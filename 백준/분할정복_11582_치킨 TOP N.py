# -*- coding: utf-8 -*-

n = int(input())

data = list(map(int, input().split()))

k = int(input())

res = [] #결과를 담을 리스트

count = 0
group = int(n/k) #이 갯수만큼 한 그룹으로 묶어야함
while count < n:
    tmp = data[count:(count+group):]
    tmp.sort()
    res.append(tmp)
    
    count += group
#print(res)
for i in range(len(res)):
    for j in range(len(res[i])):
        print(res[i][j], end = ' ')