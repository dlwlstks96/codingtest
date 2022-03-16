# -*- coding: utf-8 -*-

from collections import deque as dq

n = int(input())

answer = []

# paint = [
#     [-1, -1, -1, -1, -1, -1, -1], 
#     [-1, 1, 1, 1, 3, 3, -1], 
#     [-1, 2, 2, 3, 3, 3, -1],
#     [-1, 3, 3, 3, 1, 1, -1],
#     [-1, 3, 3, 1, 1, 1, -1],
#     [-1, 1, 1, 1, 1, 1, -1],
#     [-1, -1, -1, -1, -1, -1, -1]
#     ]

paint = [[-1 for i in range(n+2)]]
for i in range(n):
    tmp = str(input())
    listTmp = [-1]
    for t in tmp:
        if t == 'R':
            listTmp.append(1)
        elif t == 'G':
            listTmp.append(2)
        else:
            listTmp.append(3)
    listTmp.append(-1)
    paint.append(listTmp)
paint.append([-1 for i in range(n+2)])

red = []
green = []
blue = []

for i in range(1, n+1): #좌표 정보 획득
    for j in range(1, n+1):
        if paint[i][j] == 1:
            red.append((i, j))
        elif paint[i][j] == 2:
            green.append((i, j))
        elif paint[i][j] == 3:
            blue.append((i, j))
            
colorCount = [0, 0, 0, 0]

q = []
q = dq(q)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if paint[i][j] > 0:
            nowColor = paint[i][j]
            colorCount[nowColor] += 1
            q.append((i, j, nowColor))
            paint[i][j] = 0
            
            while q:
                nowY, nowX, nowColor = q.popleft()
                for k in range(4):
                    nextY = nowY + move[k][0]
                    nextX = nowX + move[k][1]
                    if paint[nextY][nextX] == nowColor:
                        q.append((nextY, nextX, nowColor))
                        paint[nextY][nextX] = 0
                        
# print(colorCount)

answer.append(sum(colorCount))

#다시 색깔 칠하기(적록색약)
for y, x in red:
    paint[y][x] = 1
for y, x in green:
    paint[y][x] = 1
for y, x in blue:
    paint[y][x] = 3
    
colorCount = [0, 0, 0, 0]

q = []
q = dq(q)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        if paint[i][j] > 0:
            nowColor = paint[i][j]
            colorCount[nowColor] += 1
            q.append((i, j, nowColor))
            paint[i][j] = 0
            
            while q:
                nowY, nowX, nowColor = q.popleft()
                for k in range(4):
                    nextY = nowY + move[k][0]
                    nextX = nowX + move[k][1]
                    if paint[nextY][nextX] == nowColor:
                        q.append((nextY, nextX, nowColor))
                        paint[nextY][nextX] = 0
                        
answer.append(sum(colorCount))

for i in answer:
    print(i, end = ' ')

