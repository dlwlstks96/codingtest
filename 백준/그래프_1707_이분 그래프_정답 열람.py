# -*- coding: utf-8 -*-

### bfs
import collections
import sys
sys.setrecursionlimit(10 ** 6)
#input = sys.stdin.readline

for _ in range(int(input())):
    V, E = map(int, input().split())
    graph = [[] for i in range(V+1)] # 빈 그래프 생성
    visited = [0] * (V+1) # 방문한 정점 체크

    for _ in range(E):
        a,b = map(int, input().split())
        graph[a].append(b) # 무방향 그래프
        graph[b].append(a) # 무방향 그래프
        
    print(graph)


    q = collections.deque()
    group = 1
    bipatite = True
    for i in range(1, V+1):
        if visited[i] == 0: # 방문하지 않은 정점이면 bfs 수행
            q.append(i)
            visited[i] = group
            while q:
                print(visited)
                v = q.popleft()
                for w in graph[v]:
                    if visited[w] == 0: # 방문하지 않은 정점이면 큐에 삽입
                        q.append(w)
                        visited[w] = -1 * visited[v] # 현재 노드와 다른 그룹 지정
                    elif visited[v] == visited[w]: # 이미 방문한 경우, 동일한 그룹에 속하면 False
                        bipatite = False

    print('YES' if bipatite else 'NO')


''' 아래가 나의 풀이

k = int(input())

answerList = []

for i in range(k):
    v, e = map(int, input().split())
    
    node = {}
    nodeList = [] #인덱스로 노드 리스트 접근하기 위함
    for j in range(1, v+1):
        node[j] = set()
    
    for j in range(e):
        n1, n2 = map(int, input().split()) #간선의 끝 정보 입력
        node[n1].add(n2)
        node[n2].add(n1)
        nodeList.append(n1)
        nodeList.append(n2)
        
        
    noConnectV = 0        
    for j in range(1, v+1):
        if len(node[j]) == 0:
            noConnectV += 1
        
    nodeList = list(set(nodeList))
    nodeList.sort()
    
    #print(node)
        
    visit = [0] * (v+1)
    
    startNodeNum = nodeList[0]
    
    red = set()
    blue = set()
    red.add(startNodeNum)
    
    nowRed = False
    
    while True:
        stack = []    
        stack.append(startNodeNum)
    
        while stack:
            nowNodeNum = stack.pop()
            visit[nowNodeNum] = 1
            
            #print(nowNodeNum, red, blue)
        
            for adjNodeNum in node[nowNodeNum]: #인접 노드 저장(DFS)
                if visit[adjNodeNum] == 0:
                    stack.append(adjNodeNum)
                    if nowRed == True:
                        red.add(adjNodeNum)
                    else:
                        blue.add(adjNodeNum)
        
            nowRed = not nowRed
            
        for j in range(startNodeNum, len(nodeList)):
            if visit[j] == 0 and len(node[j]) != 0:
                startNodeNum = j
                if nowRed == True:
                    red.add(startNodeNum)
                else:
                    blue.add(startNodeNum)
                break
        
        if sum(visit) != (v-noConnectV):
            continue
        else:
            #print(red, blue)
    
            answer = 'YES'
    
            for j in range(1, v+1):
                if j in red and j in blue:
                    answer = 'NO'
                    break
        
            if (len(red) + len(blue)) != (v-noConnectV):
                answer = 'NO'
        
            answerList.append(answer)
            break
            
for i in answerList:
    print(i)
    
'''
        
        