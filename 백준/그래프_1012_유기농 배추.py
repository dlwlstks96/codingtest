# -*- coding: utf-8 -*-

def dfs(y, x):
    stack = []
    stack.append([y, x])
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    while stack:
        nowXY = stack.pop()
        for i in range(4):
            nextY = nowXY[0] + move[i][0]
            nextX = nowXY[1] + move[i][1]
            if board[nextY][nextX] == 1:
                stack.append([nextY, nextX])
                board[nextY][nextX] = 0 #탐색했으니 0으로

t = int(input())

res = []

for i in range(t):
    m, n, k = map(int, input().split())
    board = [[0 for _ in range(m+2)] for _ in range(n+2)]
    for j in range(k):
        x, y = map(int, input().split())
        x += 1
        y += 1
        board[y][x] = 1 #양배추 세팅
        
    count = 0
    for a in range(1, n+1):
        for b in range(1, m+1):
            if board[a][b] == 1:
                board[a][b] = 0
                dfs(a, b)
                count += 1
        
    res.append(count)
    
for i in res:
    print(i)
        