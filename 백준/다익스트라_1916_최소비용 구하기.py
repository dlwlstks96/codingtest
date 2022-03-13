# -*- coding: utf-8 -*-

import heapq

INF = int(1e9)

#n = 5
#m = 8

n = int(input())
m = int(input())

graph = [[] for i in range(n+1)] #버스 정보 담을 그래프

for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

start, end = map(int, input().split())

hq = []
distance = [INF for i in range(n+1)] #최소 거리 갱신할 테이블

distance[start] = 0 #시작 지점은 거리 0

heapq.heappush(hq, (distance[start], start)) #시작 정보 push

while hq:
    nowDist, nowNode = heapq.heappop(hq) #pop
    
    if distance[nowNode] < nowDist: #이미 더 최소거리가 있다면 패스
        continue
    
    for nextNode, nextDist in graph[nowNode]:
        nextSumDist = nextDist + nowDist
        
        if nextSumDist < distance[nextNode]: #다음 거리가 더 작다면
            heapq.heappush(hq, (nextSumDist, nextNode))
            distance[nextNode] = nextSumDist

#print(distance)

print(distance[end])