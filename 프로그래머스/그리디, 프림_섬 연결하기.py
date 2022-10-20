import heapq as hq

def solution(n, costs): #그리디, 프림 알고리즘
    answer = 0
    
    graph = [[] for _ in range(n)]
    
    for c in costs: #양방향 그래프 연결
        graph[c[0]].append([c[1], c[2]])
        graph[c[1]].append([c[0], c[2]])
    
    visit = [0 for _ in range(n)] #방문 처리
    
    q = []
    
    hq.heappush(q, (0, 0)) #현재 간선 가중치 / 현재 노드
    
    while q:
        
        nowDist, nowNode = hq.heappop(q) #우선순위 큐 / 가장 거리가 짧은 간선 반환
        
        if visit[nowNode] == 1: #이미 방문한 노드라면
            continue
            
        answer += nowDist
        
        visit[nowNode] = 1 #방문 처리
        
        for nextNode, nextDist in graph[nowNode]:
            if visit[nextNode] == 0: #다음 노드가 미방문이라면
                hq.heappush(q, (nextDist, nextNode)) #다음 간선 가중치, 다음 노드 번호
            
    #print(answer)
    
    return answer
