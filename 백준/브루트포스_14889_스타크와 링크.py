# -*- coding: utf-8 -*-

import itertools as it

# n = 6
n = int(input())

data = []
for i in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

# data = [
#         [0,1,2,3],
#         [4,0,5,6],
#         [7,1,0,2],
#         [3,4,5,0]
#         ]

# data = [
#         [0,1,2,3,4,5],
#         [1,0,2,3,4,5],
#         [1,2,0,3,4,5],
#         [1,2,3,0,4,5],
#         [1,2,3,4,0,5],
#         [1,2,3,4,5,0]
#         ]

pick = it.combinations(range(1, n+1), n//2)
count = 0
pick_list = []
for p in pick: #모든 스타와 링크팀 나누는 경우의 수
    if 1 not in p:
        break
    pick_list.append(p)
    count += 1
    
#print(pick_list)

minVal = 1000000000000
for star in pick_list:
    star = list(star)
    link = []
    for j in range(1, n+1): #스타와 링크팀 구분
        if j not in star:
            link.append(j)
    
    starVal = 0
    for i in range(len(star)): #스타팀 가중치 합산
        for j in range(len(star)):
            starVal += data[star[i]-1][star[j]-1]
            
    linkVal = 0
    for i in range(len(link)): #링크팀 가중치 합산
        for j in range(len(link)):
            linkVal += data[link[i]-1][link[j]-1]
            
    minVal = min(minVal, abs(starVal - linkVal))
    
print(minVal)


