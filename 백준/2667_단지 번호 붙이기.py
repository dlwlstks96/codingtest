# -*- coding: utf-8 -*-

from collections import deque as dq

# n = 7

# home = [
#         [0,0,0,0,0,0,0,0,0],
#         [0,0,1,1,0,1,0,0,0],
#         [0,0,1,1,0,1,0,1,0],
#         [0,1,1,1,0,1,0,1,0],
#         [0,0,0,0,0,1,1,1,0],
#         [0,0,1,0,0,0,0,0,0],
#         [0,0,1,1,1,1,1,0,0],
#         [0,0,1,1,1,0,0,0,0],
#         [0,0,0,0,0,0,0,0,0]
#         ]

n = int(input())

home = [[]for i in range(n+2)]
home[0] = [0 for i in range(n+2)]
home[n+1] = [0 for i in range(n+2)]
for i in range(1, n+1):
    home[i].append(0)
    tmp = str(input())
    for j in tmp:
        home[i].append(int(j))
    home[i].append(0)
    
#print(home)

def bfs(home, i, j):
    q = []
    q = dq(q) #deque 선언
    q.append([i, j])
    count = 1 #집 갯수
    home[i][j] = 0
    move = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우
    while q:
        nowXY = q.popleft()
        for i in range(4): #4방향 각각 집이 있는지 탐색
            nextY = nowXY[0] + move[i][0]
            nextX = nowXY[1] + move[i][1]
            if home[nextY][nextX] == 1:
                q.append([nextY, nextX])
                home[nextY][nextX] = 0 #집 탐색했으니 0으로 처리
                count += 1
                
    res.append(count)
        
res = []

for i in range(1, n+1):
    for j in range(1, n+1):
        if home[i][j] == 1: #현 위치가 집이라면
            bfs(home, i, j) #bfs 실시
            
print(len(res))
res.sort()
for i in res:
    print(i)