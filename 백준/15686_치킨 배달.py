# -*- coding: utf-8 -*-

from itertools import combinations

# N = 5
# M = 3
# board = [
#     [0, 2, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 1],
#     [2, 2, 0, 1, 2]
#         ]
 
## 맵크기(N), 치킨집 최대 선택가능개수(M)
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
 
## 빈칸(0), 집(1), 치킨집(2)
house = []
chicken = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1: house.append((i, j))
        elif board[i][j] == 2: chicken.append((i, j))
        
#print('chicken = ', chicken)
#print('house = ', house)
 
minv = float('inf')
for ch in combinations(chicken, M):
    sumv = 0
    for home in house:
        sumv += min([abs(home[0]-i[0])+abs(home[1]-i[1]) for i in ch])
        #print(sumv, home)
        #print(ch)
        #print('ssssssssssssss')
        if minv <= sumv: break
    if sumv < minv: minv = sumv
    #print('============')
 
print(minv)


'''아래가 내 풀이

#===============================

import itertools as it

# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# res = it.combinations(l, 6)
# for i in res:
#     print(i)
    
    #=================================
    
n = 5
m = 3
city = [
    [0, 2, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [2, 0, 0, 1, 1],
    [2, 2, 0, 1, 2]
        ]

res = it.combinations(range(12), m)
# for i in res:
#     print(i)

chickenList = []
homeList = []
for i in range(len(city)):
    for j in range(len(city[i])):
        if city[i][j] == 2:
            chickenList.append((i, j))
        elif city[i][j] == 1:
            homeList.append((i, j))
            
for i in res:
    minChickenDist = 9999
    for h in homeList:
        myMinDist = 99999
        for r in i:
            x = abs(chickenList[r][0] - homeList[h][0])
            y = abs(chickenList[r][1] - homeList[h][1])
            if myMinDist > x+y:
                myMinDist = x+y
    
    
       #==============================     

# n = 5
# m = 3
# city = [
#     [0, 2, 0, 1, 0],
#     [1, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0],
#     [2, 0, 0, 1, 1],
#     [2, 2, 0, 1, 2]
#         ]

# # city = [
# #     [1, 2, 0, 0, 0],
# #     [1, 2, 0, 0, 0],
# #     [1, 2, 0, 0, 0],
# #     [1, 2, 0, 0, 0],
# #     [1, 2, 0, 0, 0]
# #         ]

# chickenList = []
# homeList = []
# for i in range(len(city)):
#     for j in range(len(city[i])):
#         if city[i][j] == 2:
#             chickenList.append((i, j))
#         elif city[i][j] == 1:
#             homeList.append((i, j))

# chickenCount = len(chickenList)
# homeCount = len(homeList)
            
# print(chickenList)
# print(homeList)

# chickenDist = [[0 for i in range(homeCount)] for j in range(chickenCount)]

# for i in range(chickenCount):
#     for j in range(homeCount):
#         x = abs(chickenList[i][0] - homeList[j][0])
#         y = abs(chickenList[i][1] - homeList[j][1])
#         chickenDist[i][j] = x + y
        
# print(chickenDist)

# resList = []

# for i in range(homeCount):
#     minDist = 9999
#     myMinIdx = 9999
#     for j in range(chickenCount):
#         if minDist > chickenDist[j][i]:    
#             minDist = chickenDist[j][i]
#             myMinIdx = j
#     resList.append((myMinIdx))

# print(resList)

# distSumList = []

# for i in range(len(chickenDist)):
#     tmp = sum(chickenDist[i])
#     distSumList.append(tmp)
    
# print(distSumList)

'''