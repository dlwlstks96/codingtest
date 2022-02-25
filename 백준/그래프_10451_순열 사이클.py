# -*- coding: utf-8 -*-

from collections import deque

t = int(input())

resList = []
for _ in range(t):    
    n = int(input())
    #0을 0번 인덱스에 집어 넣기 위한 deque 선언
    graph = deque(map(int, input().split()))
    graph.appendleft(0)
    
    visited = [0] * (n+1) #노드 방문 체크
    group = 1 #그룹의 갯수 카운트
    
    for i in range(1, n+1): #다음 노드가 하나씩 밖에 없기에 DFS 진행
        stack = []
        if visited[i] == 0: #아직 방문하지 않았다면
            stack.append(i) #노드 번호 스택에 삽입
            #visited[i] = group
            while stack:
                nowNodeNum = stack.pop() #스택에서 꺼냄
                visited[nowNodeNum] = group #그룹에 추가
                nextNodeNum = graph[nowNodeNum] #다음 노드 번호 
                
                if visited[nextNodeNum] == 0: #다음 노드 아직 미방문이면
                    stack.append(nextNodeNum)
                    
            group += 1 #다음 그룹 여부 체크를 위함
            
    resList.append(max(visited)) #정답 저장
    
for answer in resList:
    print(answer)