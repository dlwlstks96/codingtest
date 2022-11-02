import heapq as hq

def solution(n, works):
    answer = 0
    
    q = []
    
    for work in works: #모든 작업들을 큰 work 먼저 나오게끔 우선순위 큐에 삽입
        hq.heappush(q, (-work, work))
        
    for _ in range(n):
        
        nowPop = hq.heappop(q) #가장 큰 work 꺼내기
        
        if nowPop[1] == 0: #현재 꺼낸 work가 0일 때 -> 모든 작업이 0이란 뜻
            break
            
        newWork = nowPop[1] - 1 #가장 큰 work - 1
        hq.heappush(q, (-newWork, newWork))
        
    for nowQ in q: #작업들 순회하며 제곱하여 합산
        answer += nowQ[1] * nowQ[1]
    
    return answer
