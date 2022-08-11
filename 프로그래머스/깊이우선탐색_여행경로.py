def solution(tickets):
    
    answer = []
    
    #여행 정보를 이용한 그래프 생성
    graph = {}
    for start, end in tickets:
        if start not in graph:
            graph[start] = [end]
        else:
            graph[start].append(end)
    
    #graph의 각 도착 정보 내림차순 정렬
    for g in graph.items():
        graph[g[0]] = sorted(g[1], reverse=True)
    
    stack = ["ICN"]
    
    #매번 여행 경로에서 다음 목적지가 없는 출발지를 찾는 것을 목표로 한다
    while stack:
        
        nowStart = stack[-1]
        
        #현재 출발지에서 더 이상 목적지가 없을 경우
        if nowStart not in graph or not graph[nowStart]:
            answer.append(stack.pop())
        else: #현재 출발지에서 다른 목적지가 있을 경우
            stack.append(graph[nowStart].pop())
        
    return answer[::-1]

tickets = [["ICN", "BOO"], ["ICN", "COO"], ["COO", "ICN"]]

print(solution(tickets))
