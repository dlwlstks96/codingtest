# -*- coding: utf-8 -*-

import heapq

INF = int(1e9)

n, m = map(int, input().split())

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
distance = [INF for _ in range(n+1)] #시작점에서 각 노드까지의 최소 비용

hq = []

start = 1
distance[start] = 0 #시작 지점까지의 비용은 0
heapq.heappush(hq, (distance[start], start))

while hq:
    nowDist, nowNode = heapq.heappop(hq)
    
    if nowDist > distance[nowNode]:
        continue
    
    for nextNode, nextDist in graph[nowNode]:
        sumDist = nextDist + nowDist
        
        if distance[nextNode] > sumDist:
            heapq.heappush(hq, (sumDist, nextNode))
            distance[nextNode] = sumDist

print(distance[n])