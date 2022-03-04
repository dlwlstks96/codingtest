# -*- coding: utf-8 -*-

from collections import deque as dq

#n, m = 4, 6

# data = [
#         [0,0,0,0,0,0,0,0],
#         [0,1,1,0,1,1,0,0],
#         [0,1,1,0,1,1,0,0],
#         [0,1,1,1,1,1,1,0],
#         [0,1,1,1,1,0,1,0],
#         [0,0,0,0,0,0,0,0]
#         ]

# visit = [
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0],
#         [0,0,0,0,0,0,0,0]
#         ]

n, m = map(int, input().split())
data = [[0 for i in range(m+3)]]
for i in range(n):
    tmp = list(map(int, str(input())))
    tmp = [0] + tmp + [0]
    data.append(tmp)
data.append([0 for i in range(m+3)])

visit = [[0 for i in range(m+3)] for j in range(n+3)]

q = []
q = dq(q)
count = 1
q.append([1, 1, count])

answer = 0
while q:
    nowXY = q.popleft()
    if nowXY[0] == n and nowXY[1] == m: #목적지 도착
        answer = nowXY[2]
        break
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    count = nowXY[2] + 1
    for i in range(4):
        nextY = nowXY[0] + move[i][0]
        nextX = nowXY[1] + move[i][1]
        if data[nextY][nextX] == 1 and visit[nextY][nextX] == 0:
            q.append([nextY, nextX, count])
            visit[nextY][nextX] = 1
            
print(answer)