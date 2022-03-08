# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())
pos = sorted(list(map(int, sys.stdin.readline().split())))

if k >= n:
    print(0)
    sys.exit()

dist = []
for i in range(1, n): #인접한 센서들간의 거리 구하기
    dist.append(pos[i] - pos[i-1])

dist.sort(reverse=True) #내림차순 정렬
for _ in range(k-1): #가장 먼 순서대로 연결 고리 제거
    dist.pop(0)

print(sum(dist))


''' 아래가 내 풀이

1 3 6(2) 7 9

3 6 7 8 10 12 14 15 18 20

import math

n = 10
k = 5
#sensor = [1, 6, 9, 3, 6, 7] #1, 3, 6, 6, 7, 9
sensor = [20, 3, 14, 6, 7, 8, 18, 10, 12, 15]

sensor = list(set(sensor))

sensor.sort()

print(sensor)

point = []
for i in range(1, k+1):
    point.append([round((max(sensor)/(k+1)))*i])
print(point)

sumDis = 0
for s in sensor:
    minDis = 999999999
    groupNum = -1
    for i in range(len(point)):
        if minDis > abs(point[i][0] - s):
            minDis = abs(point[i][0] - s)
            groupNum = i
    point[groupNum].append(s)
    sumDis += minDis

print('sumDis = ', sumDis)

cnt = 0
while True:
    prevDis = sumDis
    sumDis = 0
    
    for i in range(len(point)):
        tmp = point[i][1:]
        avg = round(sum(tmp)/len(tmp))
        point[i] = [avg]
    
    for s in sensor:
        minDis = 999999999
        groupNum = -1
        for i in range(len(point)):
            if minDis > abs(point[i][0] - s):
                minDis = abs(point[i][0] - s)
                groupNum = i
        point[groupNum].append(s)
        sumDis += minDis
        
    cnt += 1
    if cnt == 1000:
        print('zzzz', point, sumDis)
        break
print(sumDis)
    
    # if prevDis == sumDis:
    #     print('zzzz', point, sumDis)
    #     break
'''    