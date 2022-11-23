def solution(topping):
    answer = 0
    
    dicA = {} #A가 가지고 있는 토핑
    dicB = {} #B가 가지고 있는 토핑
    
    for t in topping: #케이크의 모든 토핑을 우선 B에게 주기
        if t not in dicB:
            dicB[t] = 1
        else:
            dicB[t] += 1
            
    lenA = len(dicA) #현재 A의 토핑 종류 수
    lenB = len(dicB) #현재 B의 토핑 종류 수
    lenT = len(topping) #전체 롤케이크의 길이
    
    idxPoint = 0
    
    while idxPoint <= lenT - 2:
        
        nowT = topping[idxPoint] #현재 토핑
        
        if nowT not in dicA: #현재 토핑을 A가 가지고 있지 않다면
            dicA[nowT] = 1
            lenA += 1 #A가 가지고 있는 토핑 종류 수 +1
            
        dicB[nowT] -= 1 #B에게서 현재 토핑 -1
        if dicB[nowT] == 0: #B가 현재 토핑을 0개 가지고 있다면
            lenB -= 1 #B의 토핑 종류 수 -1
    
        if lenA == lenB: #두 사람의 가지고 있는 토핑 종류 수가 같다면
            answer += 1
            
        idxPoint += 1
    
    return answer
