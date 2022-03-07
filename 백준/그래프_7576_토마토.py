# -*- coding: utf-8 -*-

import sys
from collections import deque as dq

# m, n = 6, 4

# board = [
#         [0,0,0,0,0,0,0,0],
#         [0,1,-1,0,0,0,0,0],
#         [0,0,-1,0,0,0,0,0],
#         [0,0,0,0,0,-1,0,0],
#         [0,0,0,0,0,-1,1,0],
#         [0,0,0,0,0,0,0,0]
#         ]

m, n = map(int, input().split())

board = [[-1 for i in range(m+2)]]
for i in range(n):
    tmp = [-1]
    tmp += (list(map(int, input().split())))
    tmp += [-1]
    board.append(tmp)
board.append([-1 for i in range(m+2)])

t_one = []
t_zero = []

for i in range(1, n+1):
    for j in range(1, m+1):
        if board[i][j] == 1:
            t_one.append([i, j])
        elif board[i][j] == 0:
            t_zero.append([i, j]) #토마토 밭 정보 획득
            
if len(t_zero) == 0: #처음부터 모든 토마토 익어있다면
    print(0)
    sys.exit()


q = []
q = dq(q)
day = 0
for i in range(len(t_one)):
    q.append([t_one[i], day]) #익은 모든 토마토를 큐에 삽입
    
while q:
    nowT = q.popleft() #토마토 꺼내기
    day = max(day, nowT[1]) #날짜 최신화
    move = [[-1,0], [1,0], [0,-1], [0,1]]
    for i in range(4):
        nextT_Y = nowT[0][0] + move[i][0]
        nextT_X = nowT[0][1] + move[i][1]
        if board[nextT_Y][nextT_X] == 0:
            q.append([[nextT_Y, nextT_X], nowT[1]+1])
            board[nextT_Y][nextT_X] = 1 #익은 것으로 처리

for t in t_zero:
    if board[t[0]][t[1]] == 0: #모두 익지 못하는 상황이면
        print(-1)
        sys.exit()
            
print(day)