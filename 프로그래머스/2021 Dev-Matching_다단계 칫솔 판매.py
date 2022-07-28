import math

def solution(enroll, referral, seller, amount):
    answer = []
    
    graph = {} #나의 추천인과 내 총액
    for nowE, nowR in zip(enroll, referral):
        
        if nowR == '-': #날 추천해준 사람 없다면
            graph[nowE] = ['center', 0]
        else:
            graph[nowE] = [nowR, 0]

    for nowS, nowA in zip(seller, amount):
        
        nowA = nowA * 100
        
        while True:
            if graph[nowS][0] == 'center': #다음 S가 center라면
                graph[nowS][1] += math.ceil(nowA*0.9)
                break
            elif (nowA/10) < 1: #10% 계산 금액이 1원 미만일 경우
                graph[nowS][1] += nowA
                break
            else: #내가 90% 가지고 추천인에게 10% 전달
                graph[nowS][1] += math.ceil(nowA*0.9)
                nowS = graph[nowS][0]
                nowA = int(nowA*0.1)
                
    for key, value in graph.items(): #총액 리스트에 저장
        answer.append(value[1])
    
    return answer
