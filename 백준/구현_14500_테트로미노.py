# -*- coding: utf-8 -*-

#n, m = int(input())

# n, m = 5, 5

# board = [
#     [1, 2, 3, 4, 5],
#     [5, 4, 3, 2, 1],
#     [2, 3, 4, 5, 6],
#     [6, 5, 4, 3, 2],
#     [1, 2, 1, 2, 1]
#     ]


# minoOne = [[0,0], [0,1], [0,2], [0,3]]

# minoTwo = [[0,0], [0,1], [1,0], [1,1]]

# minoThree = [[0,0], [1,0], [2,0], [2,1]]

# minoFour = [[0,0], [1,0], [1,1], [2,1]]

# minoFive = [[0,0], [0,1], [0,2], [1,1]]

# def oneTurn(mino):
#     mino[0] = 

from collections import deque as dq

n, m = 5, 5

board = [
    [1, 2, 3, 4, 5],
    [5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6],
    [6, 5, 4, 3, 2],
    [1, 2, 1, 2, 1]
    ]

for x in range(m):
    for y in range(n):
        visit = []
        q = []
        q = dq(q)
        startIdx = [x, y]
        visit.append((x, y))
        q.append(startIdx)
        while q:
            nowIdx = q.popleft()
            
        
        