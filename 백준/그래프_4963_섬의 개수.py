# -*- coding: utf-8 -*-

from collections import deque as dq

# w, h = 5, 4 #너비 w, 높이 h

# graph = [
#     [0, 0, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 0, 0, 0],
#     [0, 1, 0, 0, 0, 0, 0],
#     [0, 1, 0, 1, 0, 1, 0],
#     [0, 1, 0, 0, 1, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
#     ]

while True:
    w, h = map(int, input().split())
    if w == 0 or h == 0:
        break
    
    #맵 그리기
    graph = [[0 for _ in range(w+2)]]
    for _ in range(h):
        map_tmp = list(map(int, input().split()))
        graph.append([0] + map_tmp + [0])
    graph.append([0 for _ in range(w+2)])
    
    q = dq([])
    count = 0 #섬 갯수 카운트
    move = [[1, 0], [0, 1], [-1, 0], [0, -1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        
    for i in range(1, h+1):
        for j in range(1, w+1):
            nowXY = graph[i][j]
            if nowXY == 0:
                continue
            q.append((i, j))
            graph[i][j] = 0
            count += 1
            
            while q:
                nowPoint = q.popleft()
                nowY = nowPoint[0]
                nowX = nowPoint[1]
                
                for m in move:
                    nextY = nowY + m[0]
                    nextX = nowX + m[1]
                    if graph[nextY][nextX] == 1:
                        q.append((nextY, nextX))
                        graph[nextY][nextX] = 0
                        
    print(count)
    