from collections import deque as dq

n, m = map(int, input().split())

graph = [[] for i in range(n+1)] #선수 과목 연결 정보
branch = [0 for i in range(n+1)] #간선 갯수 저장
dp = [1 for i in range(n+1)] #현재 수업을 듣기까지 필요한 학기 수 저장

for _ in range(m):
    a, b = map(int, input().split())
    
    graph[a].append(b)
    
    branch[b] += 1
        
# print(graph)
# print(branch)

q = dq([])

for i in range(1, n+1): #선수 과목 없는 과목들 큐에 저장
    if branch[i] == 0:
        q.append(i)
        
while q:
    
    nowStudy = q.popleft() #현재 과목
    
    for nextStudy in graph[nowStudy]:
        
        branch[nextStudy] -= 1 #현재 과목 들었으니 다음 과목 간선 하나 삭제
        dp[nextStudy] = max(dp[nextStudy], dp[nowStudy] + 1)
        
        if branch[nextStudy] == 0: #다음 과목의 선수 과목이 더 없을 때
            q.append(nextStudy)
            
#print(dp[1:])
for d in dp[1:]:
    print(d, end=' ')
