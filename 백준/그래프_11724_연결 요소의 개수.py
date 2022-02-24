# -*- coding: utf-8 -*-

n, m = map(int, input().split(' '))

node = {}
for i in range(n+1):
    node[i] = set() #노드에 연결되어 있는 정점 저장

for i in range(m): #연결 정보 받아와서 set함수에 저장
    u, v = map(int, input().split(' '))
    node[u].add(v)
    node[v].add(u)
    
#print(node)

visit = [0] * (n+1) #노드 방문 정보 확인

stack = []

count = 0

for nodeNum in range(1, len(node)):
    if visit[nodeNum] == 1:
        continue
    
    stack.append(nodeNum)
    
    while stack:
        nowNodeNum = stack.pop()
        if visit[nowNodeNum] == 1:
            continue
        else:    
            visit[nowNodeNum] = 1
            for adjNodeNum in node[nowNodeNum]:
                stack.append(adjNodeNum)
    
    count += 1
    
print(count)