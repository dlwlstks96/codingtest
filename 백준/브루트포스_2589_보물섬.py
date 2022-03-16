# -*- coding: utf-8 -*-

from collections import deque as dq

n, m = map(int, input().split())

# board = [
#     [-1, -1, -1, -1, -1, -1, -1, -1, -1],
#     [-1, 0, 1, 1, 0, 0, 0, 1, -1],
#     [-1, 1, 1, 1, 0, 1, 1, 1, -1],
#     [-1, 1, 0, 1, 0, 1, 0, 0, -1],
#     [-1, 1, 0, 1, 0, 1, 1, 1, -1],
#     [-1, 0, 1, 1, 0, 1, 0, 0, -1],
#     [-1, -1, -1, -1, -1, -1, -1, -1, -1]
#     ]

board = [[-1 for i in range(m+2)]]
for i in range(n):
    data = [-1]
    tmp = str(input())
    for j in tmp:
        if j == 'W':
            data.append(0)
        else:
            data.append(1)
    data.append(-1)
    board.append(data)
board.append([-1 for i in range(m+2)])

q = []
q = dq(q)
move = [(-1, 0), (1, 0), (0, -1), (0, 1)]
distance = []

landList = []
for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            landList.append((i, j)) #육지 정보 획득

for i in range(1, n+1): #완전 탐색
    for j in range(1, m+1):
        if board[i][j] == 1:
            dist = 0
            maxDist = dist
            q.append((i, j, dist))
            board[i][j] = 0
            
            while q:
                nowY, nowX, nowDist = q.popleft()
                maxDist = max(maxDist, nowDist)
                
                for k in range(4):
                    nextY = nowY + move[k][0]
                    nextX = nowX + move[k][1]
                    if board[nextY][nextX] == 1:
                        q.append((nextY, nextX, nowDist+1))
                        board[nextY][nextX] = 0
                        
            distance.append(maxDist)
            
            for y, x in landList: #다시 육지 세팅
                board[y][x] = 1

print(max(distance))