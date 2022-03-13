# -*- coding: utf-8 -*-

from collections import deque

MAX = 100001
check = [False] * MAX
dist = [-1] * MAX

n,k = map(int, input().split())
q = deque()
q.append(n)
check[n] = True
dist[n] = 0

while q:
    now = q.popleft()
    if now*2 < MAX and check[now*2] == False:  # 순간이동
        q.appendleft(now*2) #먼저 체크하기 위해 큐 왼쪽에 삽입
        check[now*2] = True
        dist[now*2] = dist[now]
    if now + 1 < MAX and check[now+1] == False: # x+1이동
        q.append(now+1) #나중에 체크하기 위해 큐 오른쪽 삽입
        check[now+1] = True
        dist[now+1] = dist[now] + 1
    if now - 1 >= 0 and check[now-1] == False: # x-1이동
        q.append(now-1) #나중에 체크하기 위해 큐 오른쪽 삽입
        check[now-1] = True
        dist[now-1] = dist[now] + 1
print(dist[k])


'''

import heapq
import sys

INF = int(1e9)

n, k = map(int, input().split())

if n >= k: #수빈이가 더 앞서 있다면 1초마다 뒤로 물러나기
    print(n-k)
    sys.exit()
    
timeTable = [INF for i in range(200001)]

hq = []
Time = 0
heapq.heappush(hq, (Time, n))
timeTable[n] = Time


while hq:
    nowTime, nowPoint = heapq.heappop(hq)
    #print(nowTime, nowPoint, hq)
    if nowPoint == k:
        print(nowTime)
        break
    elif nowTime >= (k - n):
        print(k-n)
        break
    
    if timeTable[nowPoint] < nowTime:
        continue
    
    flyPoint = nowPoint
    while flyPoint <= 100000:
        flyPoint *= 2
        if flyPoint == k:
            print(nowTime)
            sys.exit()
        if timeTable[flyPoint] > nowTime:
            timeTable[flyPoint] = nowTime
            heapq.heappush(hq, (nowTime, flyPoint))
    
    nextTime = nowTime + 1
    
    nextPoint1 = nowPoint - 1
    if nextPoint1 > -1:
        if timeTable[nextPoint1] > nextTime:
            timeTable[nextPoint1] = nextTime
            heapq.heappush(hq, (nextTime, nextPoint1))
    
    nextPoint2 = nowPoint + 1
    if nextPoint2 <= 100000:
        if timeTable[nextPoint2] > nextTime:
            timeTable[nextPoint2] = nextTime
            heapq.heappush(hq, (nextTime, nextPoint2))
            
'''            