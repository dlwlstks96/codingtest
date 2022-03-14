# -*- coding: utf-8 -*-

n = int(input())
m = int(input())
    
#print(graph)

parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]: #target 노드가 부모 노드이면 target 반환
        return target
    
    #target 노드 따라가면서 부모 노드 찾기, 부모 테이블 갱신
    parent[target] = find(parent[target])
    return parent[target]

def union(a, b):
    a = find(a) #a노드의 부모 찾기
    b = find(b) #b노드의 부모 찾기
    
    if a == b: #이미 동일한 집합이면 연결 시 순환 발생
        return 
    
    if a < b: #a의 부모가 b 부모보다 상위 루트이면
        parent[b] = a #b의 부모를 a의 부모로 변경
    else: #b의 부모가 a 부모보다 상위 루트이면
        parent[a] = b #a의 부모 변경
        


for i in range(1, n+1):
    maps = list(map(int, input().split())) #i번째가 어느 도시와 연결되어 있는지 정보
    for j in range(1, len(maps)+1): #i번째 도시 연결 정보 추출
        if maps[j-1] == 1: #i 도시와 j 도시가 연결되어 있다면
            union(i, j) #두 도시 결합
    
plan = list(map(int, input().split())) #여행 계획
result = [find(i) for i in plan] #plan 하나씩 불러와 부모 노드 찾

result = set(result) #중복 제거

if len(result) == 1: #모두 같은 부모 노드이면
    print('YES')
else: #모두 같은 부모 노드가 아닐 경우
    print('NO')
    