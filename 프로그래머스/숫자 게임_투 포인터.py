def solution(A, B):
    answer = -1
    
    A.sort(reverse = True)
    B.sort(reverse = True)
    
    #두 개의 인덱스 포인터
    idxA = 0
    idxB = 0
    point = 0 #B가 이겨 획득하는 점수
    while True:
        
        #두 포인터 중 하나라도 배열을 벗어나게 된다면
        if idxA == len(A) or idxB == len(B):
            break
        
        nowA = A[idxA]
        nowB = B[idxB]
        
        if nowB > nowA: #B가 더 크다면
            point += 1
            idxA += 1
            idxB += 1
        else: #A가 B보다 크거나 같다면
            idxA += 1 #A값 버리기 / B는 while문 돌아 다음에 다시 사용
            
    answer = point
    
    return answer
