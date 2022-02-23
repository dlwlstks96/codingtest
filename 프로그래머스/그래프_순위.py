# -*- coding: utf-8 -*-

#순위

'''
같은 방향의 그래프로만 움직여 탐색
'''

# 플로이드-워셜 알고리즘

def solution(n, results):
    matrix = [[None for _ in range(n)] for _ in range(n)] #5x5 인접행렬
    for win, lose in results:
        matrix[win-1][lose-1] = True #이긴 정보
        matrix[lose-1][win-1] = False #패배 정보
    #print(matrix)
        
    for i in range(n):
        for j in range(n):
            for k in range(n):
                #i와 j가 [0,0], [1,1] 같은 경우면 None이 맞기에 생략
                if matrix[j][i] == None:
                    continue
                
                #비교할 j와 k의 승패 관계가 이미 None이 아닐 경우
                if matrix[j][k] != None or matrix[k][j] != None:
                    continue
                    
                # if j < i < k or j > i > k
                # for문의 기준점이 i, j, k 순서인데
                # i를 기준으로 j와 k를 먼저 검사하기에
                if matrix[j][i] == matrix[i][k]:
                    matrix[j][k] = matrix[j][i]
                    matrix[k][j] = not matrix[j][i]
                #print('=====================')
                    
    answer = 0
    for i in range(n):
        #print(matrix[i][:i] + matrix[i][i+1:])
        #[0,0], [1,1] 과 같은 대각선 인덱스 이외에 None이 있는지 체크
        if None in matrix[i][:i] + matrix[i][i+1:]:
            continue
        answer += 1
    return answer



''' 아래가 내 풀이
def dfs(graph, v, direction, check, cnt, visit, nodeLineCount):
    
    if check[v] == 0:
        check[v] = 1
        cnt += 1
        #print('arrived! = ', v)
        
    if sum(check) == len(graph):
        return cnt
    
    if len(graph[v][direction]) == 0: # 나아갈 방향에 노드가 없을 때
        return cnt 
    
    for nextNode in graph[v][direction]:
        if visit[nextNode] == 1:
            cnt = nodeLineCount[nextNode][0]
        else:
            cnt = dfs(graph, nextNode, direction, check, cnt, visit, nodeLineCount)
    
    return cnt

def solution(n, results):
    answer = 0
    
    graph = {}
    for i in range(1, n+1):
        graph[i] = [[],[]] #각 노드 생성(나간 방향, 들어온 방향)
        
    for r in results:
        winNode = r[0]
        loseNode = r[1]
        graph[winNode][0].append(loseNode)
        graph[loseNode][1].append(winNode)
        
    #print(graph)
    #print()
    
    nodeLineCount = [[0, 0] for i in range(n+1)]
    visit = [0 for i in range(n+1)]
        
    for i in range(1, n+1):
        if (len(graph[i][0]) + len(graph[i][1])) == n-1: #연결된 그래프 수만으로 순위가 확정될때(탐색 필요 x)
            answer += 1
            continue
        
        visit[i] == 1
        
        check = [0 for i in range(n+1)]
        cnt1 = 0
        for nextNode in graph[i][0]:
            if visit[nextNode] == 1:
                cnt1 = nodeLineCount[nextNode][0]
            else:    
                cnt1 = dfs(graph, nextNode, 0, check, cnt1, visit, nodeLineCount)
         
        #print(cnt1)
        #print('===============================')
            
        check = [0 for i in range(n+1)]
        cnt2 = 0
        for nextNode in graph[i][1]:
            if visit[nextNode] == 1:
                cnt2 = nodeLineCount[nextNode][1]
            else:
                cnt2 = dfs(graph, nextNode, 1, check, cnt2, visit, nodeLineCount)
            
        #print(cnt2)
        #print('-------------------------------')
        
        nodeLineCount[i] = [cnt1, cnt2]
        #print(cnt1, cnt2)
        
        if cnt1 + cnt2 == n-1:
            answer += 1
            
    #print(nodeLineCount)
        
    #print(answer)
        
    return answer'''

solution(5, [[4,3],[4,2],[3,2],[1,2],[2,5]])
#solution(5, [[2,1], [1,5], [2,5], [5,3], [4,5]])
























