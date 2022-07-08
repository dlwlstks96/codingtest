from collections import deque as dq

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        visit = [99999999999 for i in range(n+1)] #방문 정보, 최소 시간을 구하기 위해 매우 큰 수 저장
        
        #times 정보들을 딕셔너리에 저장
        times_dic = {}
        for t in times:
            nowNode = t[0]
            destNode = t[1]
            nowTime = t[2]
            
            # [목적지 노드, 소요 시간] 구성으로 저장
            if nowNode in times_dic:
                times_dic[nowNode].append([destNode, nowTime])
            else:
                times_dic[nowNode] = [[destNode, nowTime]]
                
        #print(times_dic)
        
        q = dq([])
        time_count = 0
        visit[k] = 1
        q.append([k, time_count])
        
        #max_time = 0
        
        while q:
            nowPop = q.popleft()
            popNode = nowPop[0] #현재 노드
            now_time_count = nowPop[1] #현재 노드까지 오는데 시간
            #max_time = max(max_time, now_time_count) #총 최대 시간
            
            #현재 노드가 또 다른 목적지로 향한다면 큐에 삽입
            if popNode in times_dic:
                for dic_key in times_dic[popNode]:
                    #대신 다음 목적지 노드까지의 기존 방문 시간이 (현재 시간 + 소요 시간)보다 적을 때
                    if visit[dic_key[0]] > now_time_count + dic_key[1]:
                        q.append([dic_key[0], now_time_count + dic_key[1]])
                        visit[dic_key[0]] = min(visit[dic_key[0]], now_time_count + dic_key[1])
                        
        #print(visit)
        if 99999999999 in visit[1:]:
            return -1
        else:
            return max(visit[1:])
