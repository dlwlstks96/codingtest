from collections import deque as dq
import copy

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        
        #그래프 그리기
        graph = [[-1 for _ in range(n + 2)]]
        for i in range(m):
            tmp = [-1]
            for j in range(n):
                tmp.append(0)
            tmp.append(-1)
            graph.append(tmp)
        graph.append([-1 for _ in range(n + 2)])
        
        print(graph)
        
        visit = copy.deepcopy(graph)
        
        q = dq([])
        q.append([1, 1])
        graph[1][1] = 1
        visit[1][1] = 1
        
        while q:
            nowXY = q.popleft()
            nowY = nowXY[0]
            nowX = nowXY[1]
            if graph[nowY][nowX + 1] != -1:
                graph[nowY][nowX + 1] += graph[nowY][nowX]
            if graph[nowY + 1][nowX] != -1:
                graph[nowY + 1][nowX] += graph[nowY][nowX]
                
            if visit[nowY][nowX + 1] == 0:
                q.append([nowY, nowX + 1])
                visit[nowY][nowX + 1] = 1
            if visit[nowY + 1][nowX] == 0:
                q.append([nowY + 1, nowX])
                visit[nowY + 1][nowX] = 1
                
        return graph[m][n]
