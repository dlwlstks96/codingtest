# -*- coding: utf-8 -*-

from collections import deque as dq

n, m = map(int, input().split())

idxList = list(map(int, input().split()))

# n, m = 10, 10
# idxList = [1, 6, 3, 2, 7, 9, 8, 4, 10, 5]

q = [0 for _ in range(n)]

q = dq(q) #deque 선언

for i in idxList:
    q[i-1] = i
    
moveCount = 0

for target in idxList:
    if q[0] == target:
        q.popleft()
        continue
    
    targetIdx = 0
    for i in range(len(q)):
        if q[i] == target:
            targetIdx = i
            break
        
    if targetIdx < len(q)/2: #타겟이 왼쪽에 더 가깝다
        for i in range(targetIdx):
            q.rotate(-1) #앞으로 당긴다
            moveCount += 1
        q.popleft()
    else: #타겟이 오른쪽에 더 가깝다
        for i in range((len(q)) - targetIdx):
            q.rotate(1) #뒤로 민다
            moveCount += 1
        q.popleft()
        
print(moveCount)


# while popCount < m:
#     print(q, moveCount)
#     if q[0] != 0:
#         q.popleft()
#         popCount += 1
#         continue
    
#     leftIdx = 0
#     for i in range(len(q)): #왼쪽부터 진행해서 1 찾기
#         if q[i] != 0:
#             leftIdx = i
#             break
        
#     rightIdx = 0
#     for i in range(len(q)-1, -1, -1): #오른쪽부터 진행해서 1 찾기
#         if q[i] != 0:
#             rightIdx = (len(q)-1) - i
#             break
        
#     print(leftIdx, rightIdx)
    
#     if leftIdx <= rightIdx: #찾는 값이 왼쪽에 더 가까울때
#         for i in range(leftIdx):
#             print(q)
#             q.rotate(-1) #앞으로 당긴다
#             moveCount += 1
#         q.popleft()
#         popCount += 1
#     else: #찾는 값이 오른쪽에 더 가까울때
#         for i in range(rightIdx):
#             print(q)
#             q.rotate(1) #뒤로 민다
#             moveCount += 1
#         q.popleft()
#         popCount += 1
        
#print(moveCount)