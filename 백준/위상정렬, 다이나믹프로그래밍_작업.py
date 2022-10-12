from collections import deque as dq

n = int(input())

branch = [0 for i in range(n+1)] #간선 갯수 확인
time = [0 for i in range(n+1)] #소요 시간 저장
dp = [0 for i in range(n+1)] #각 작업이 시작할 때의 최대 시간
dic = {}

for i in range(1, n+1):
    tmp = list(map(int, input().split()))
    
    dic[i] = []
    time[i] = tmp[0] #i번째 작업의 소요 시간
    
    if tmp[1] != 0: #이 작업 이전에 선행 작업이 있다면
        for j in tmp[2:]:
            dic[j].append(i)
            branch[i] += 1

answer = 0

q = dq([])

for idx, b in enumerate(branch):
    if idx != 0 and b == 0: #내 앞에 선행 작업이 없는 노드라면
        q.append(idx)

while q:
    
    nowNum = q.popleft()
    nowTime = time[nowNum] + dp[nowNum] #현재 작업 완료 시간
    
    #print(nowNum, ' / ', q, ' / ', branch, ' / ', dp)
    
    answer = max(nowTime, answer)
    
    for nextNum in dic[nowNum]: #내 다음 작업들의 목록을 불러온다
    
        branch[nextNum] -= 1 #간선 갯수 -1
        
        dp[nextNum] = max(dp[nextNum], nowTime) #지금 내 작업이 nextNum 선행 작업들 중 최대 시간인지
        
        #print(nowPop, ' / ', branch, ' / ', visit)
        
        if branch[nextNum] == 0: #nextNum의 선행 작업이 더 없다면
            q.append(nextNum)
    
            
print(answer)
