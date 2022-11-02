def solution(cards):
    answer = 0
    
    visit = [0 for _ in range(len(cards))] #상자 방문 처리
    saveCount = [] #각 그룹의 상자 갯수 저장
    
    for idx, nowCard in enumerate(cards):
        
        if visit[idx] == 0: #아직 안 열어본 상자라면
            groupCount = 1 #상자 1개 카운트
            visit[idx] = 1 #현재 상자 방문 처리
            nextIdx = nowCard-1 #다음 열어볼 상자 인덱스
            
            while True:
                if visit[nextIdx] == 0: #다음 상자가 안 열어본 상자라면
                    groupCount += 1
                    visit[nextIdx] = 1
                    nextIdx = cards[nextIdx]-1 #새로 열어볼 다음 상자
                else: #다음 상자가 열어본 상자라면
                    break
                    
            saveCount.append(groupCount) #현재 그룹의 상자 갯수 저장
            
    saveCount.sort(reverse=True) #오름차순 정렬
    
    #print(saveCount)
    
    if len(saveCount) > 1: #그룹이 2개 이상이라면 
        answer = saveCount[0] * saveCount[1]
    else:
        answer = 0
    
    return answer
