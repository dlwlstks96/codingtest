# -*- coding: utf-8 -*-

import sys

sys.setrecursionlimit(10000000) #재귀 횟수 제한

########그래프 만드는 과정#########

n, m, v = map(int, input().split(' '))

g = {}

for i in range(n):
    g[i+1] = []

for i in range(m):
    a, b = map(int, input().split(' '))
    g[a].append(b)
    g[b].append(a)
    
for i in range(len(g)):
    g[i+1].sort()

#########깊이 우선##########
    
def dfs(v):
    if check[v] == 0: #방문 처리
        check[v] = 1
        visit.append(v)
        
    if sum(check) == n: #모든 노드 다 방문했을 경우
        return 0
    
    for i in g[v]:
        if check[i] == 0:
            dfs(i) #연결되어 있는 애들 하나씩 dfs
            
########너비 우선##########

def bfs(v, cnt):
    if check[v] == 0:
        check[v] = 1
        if v not in visit:
            visit.append(v)
        
    for i in g[v]:
        if check[i] == 0 and i not in visit:
            visit.append(i) #연결되어 있는 애들 전부 다 방문 처리
            
    cnt += 1 #방문 기록 배열 visit의 인덱스
    
    if cnt == len(visit): #더 이상 방문할 노드가 없을 때
        return 0
    
    bfs(visit[cnt], cnt) #방문해서 연결된 애들 전부 다 처리할게 남았을 때
    
    return 0
    
############################

check = [0 for i in range(n+1)]
            
visit = []            
dfs(v)
for i in visit:
    print(i)

check = [0 for i in range(n+1)]

cnt = 0
visit = []
bfs(v, cnt)
for i in visit:
    print(i)