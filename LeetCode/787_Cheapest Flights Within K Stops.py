from collections import deque as dq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        visit = [0 for _ in range(n)] #방문 체크
        
        flights_dic = {} #모든 비행 정보를 딕셔너리에 저장
        for tmp_src, tmp_dst, tmp_price in flights:
            if tmp_src in flights_dic: #딕셔너리에 현재 출발지 정보가 있다면
                flights_dic[tmp_src].append([tmp_dst, tmp_price])
            else: 
                flights_dic[tmp_src] = [[tmp_dst, tmp_price]]
                
        #print(flights_dic)
        
        q = dq([])
        now_price = 0 #현재까지 비행 비용
        move_count = 0 #움직임 카운트
        q.append([src, now_price, move_count])
        visit[src] = 1
        
        while q:
            popQ = q.popleft()
            now_src = popQ[0]
            now_price = popQ[1]
            now_move_count = popQ[2]
            
            if now_move_count > k: #현재까지의 움직임이 k를 넘는다면 현재 pop 생략
                continue
            
            if now_src in flights_dic: #현재 출발지에서의 비행 정보가 딕셔너리에 있다면
                for next_info in flights_dic[now_src]:
                    #print(popQ, next_info)
                    next_src = next_info[0]
                    next_price = next_info[1]
                    
                    #다음 도착지가 미방문 혹은 더 저렴한 가격이라면
                    if visit[next_src] == 0 or visit[next_src] > now_price + next_price:
                        q.append([next_src, now_price + next_price, now_move_count + 1])
                        visit[next_src] = now_price + next_price
        
        if visit[dst] == 0:
            return -1
        else:
            return visit[dst]
