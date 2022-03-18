# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())
#n = int(input())

parent = [i for i in range(n+1)]

def find(target):
    if target == parent[target]: #내가 루트 노드라면
        return target
    
    parent[target] = find(parent[target]) #재귀로 끝까지 파고 들어가 루트 노드 반환
    return parent[target]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a == b: #부모 노드가 이미 같다면
        return 
    
    if a < b: #a 부모 노드가 더 상위 노드라면
        parent[b] = a
    else:
        parent[a] = b
        
firstGroup = 0
for i in range(n-2):
    n1, n2 = map(int, input().split())
    union(n1, n2)

for i in range(1, n):
    tmp1 = find(parent[i])
    tmp2 = find(parent[i+1])
    if tmp1 != tmp2:
        print(i, i+1)
        break