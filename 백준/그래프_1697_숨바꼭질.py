# -*- coding: utf-8 -*-

from collections import deque

n, k = map(int, input().split())

time = 0
if n >= k: #n이 k보다 오른쪽에 있다면
    print(n-k) #왼쪽으로 1씩 이동한 시간
else: #n < k  -> n이 k보다 왼쪽에 있다면
    q = []
    q = deque(q)
    visit = [0 for i in range(100001)]
    visit[n] = 1
    count = 0
    q.append([n, count])
    while q:
        nowN = q.popleft()
        count = nowN[1] + 1
        #print(nowN, count, q)
        if nowN[0] == k:
            print(nowN[1])
            break
        try:
            if nowN[0]-1 > -1 and visit[nowN[0]-1] == 0:
                q.append([nowN[0]-1, count])
                visit[nowN[0]-1] = 1
            if visit[nowN[0]+1] == 0:
                q.append([nowN[0]+1, count])
                visit[nowN[0]+1] = 1
            if nowN[0]*2 <= 100000 and visit[nowN[0]*2] == 0:
                q.append([nowN[0]*2, count])
                visit[nowN[0]*2] = 1
        except:
            continue