import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

import heapq

# 정점의 개수 n, 간선의 개수 m
n, m = map(int, input().split())

# 시작 정점의 번호
k = int(input())

# 무한을 의미하는 INF
INF = int(1e9)

# 그래프 초기화
graph = [[] for _ in range(n+1)]
# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 간선 정보 입력
for _ in range(m):
    a, b, c = map(int, input().split())
    # a->b가 c비용
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

# 다익스트라 알고리즘을 수행
dijkstra(k)

# 모든 노드로 가기 위한 최단 거리를 출력
for i in range(1, n+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

'''
from collections import deque as dq

v, e = map(int, input().split())

start = int(input())

#노드 간 연결 정보를 담을 판
board = [[11 for i in range(v+1)] for j in range(v+1)]

#print(board)

# 노드 정보 받아오기
for i in range(e):
    tmp1, tmp2, w = map(int, input().split())
    board[tmp1][tmp2] = min(board[tmp1][tmp2], w)
    
visit = [-1 for i in range(v+1)] #방문 정보

q = []
q = dq(q)
q.append([start, start])
visit[1] = 0

while q:
    popNode = q.popleft()
    nowNode = popNode[0]
    prevNode = popNode[1]
    if visit[nowNode] == -1:
        visit[nowNode] = board[prevNode][nowNode] + visit[prevNode]
    else:
        visit[nowNode] = min(visit[nowNode], board[prevNode][nowNode] + visit[prevNode])
    for i in range(len(board[nowNode])):
        if 0 < board[nowNode][i] <= 10 and visit[i] == -1:
            q.append([i, nowNode])
            
#print(visit)

for i in range(1, len(visit)):
    if visit[i] == -1:
        print('INF')
    else:
        print(visit[i])
        
'''        
                