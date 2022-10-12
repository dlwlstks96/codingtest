from collections import deque as dq

n = int(input())

k = int(input())

graph = [[] for _ in range(n+1)]
visit = [0 for _ in range(n+1)]

for _ in range(k):
    com1, com2 = map(int, input().split())
    
    graph[com1].append(com2) #양방향 이동 가능
    graph[com2].append(com1) #추가하는 것이 핵심

q = dq([])
q.append(1)
visit[1] = 1

count = 0

while q:
    
    nowNum = q.popleft()
    
    for nextNum in graph[nowNum]:
        
        if visit[nextNum] != 1:
            q.append(nextNum)
            visit[nextNum] = 1
            count += 1
            
print(count)
