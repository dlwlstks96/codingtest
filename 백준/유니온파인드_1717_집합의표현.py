# -*- coding: utf-8 -*-

import sys
sys.setrecursionlimit(100000)

n, m = map(int, input().split())

parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]: #target이 부모 노드이면 반환
        return target
    
    parent[target] = find(parent[target]) #부모 노드 재귀로 찾기
    return parent[target]
    
#    while target != parent[target]:
#        target = parent[target]
#        parent[target] = parent[parent[target]]
#    return target

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b: #부모 노드가 같다면 중단
        return
    
    if a < b: #a의 부모가 b보다 상위 루트이면
        parent[b] = a #b의 부모 노드를 a로 변경
    else: #b의 부모 노드가 a보다 상위 루트이면
        parent[a] = b #a의 부모 노드를 b로 변경

for i in range(m):
    cal, a, b = map(int, input().split())
    if cal == 0:
        union(a, b)
    elif cal == 1:
        a = find(a)
        b = find(b)
        if a == b:
            print('YES')
        else:
            print('NO')
        