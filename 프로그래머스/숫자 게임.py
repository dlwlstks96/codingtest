import heapq as hq

def solution(A, B):
    answer = -1
    
    q_a = []
    q_b = []
    
    #우선 순위 큐 삽입
    for a in A:
        hq.heappush(q_a, (-a, a))
    
    for b in B:
        hq.heappush(q_b, (-b, b))
    
    #꺼낸 A, B 값 / -1일 땐 비어 있단 뜻
    nowA = -1
    nowB = -1
    
    #B가 이겨서 획득한 포인트
    pointB = 0
    while True:
        
        #두 리스트 중 하나라도 빈 리스트가 있다면
        if len(q_a) == 0 or len(q_b) == 0:
            break
        
        #현재 A의 최댓값 꺼내기
        nowA = hq.heappop(q_a)[1]
        
        #pop된 B가 없는 상태라면
        if nowB == -1:
            nowB = hq.heappop(q_b)[1]
            
        if nowA < nowB: #B값이 더 크다면 점수 획득 / A, B값 둘 다 버리기
            pointB += 1
            nowA = -1
            nowB = -1
        else: #A값이 더 크거나 B값과 동일하다면
            nowA = -1 #해당 A값 버리기 / B값은 while문 돌아 다시 사용
            
    answer = pointB
    
    return answer
