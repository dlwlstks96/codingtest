# -*- coding: utf-8 -*-


def solution(triangle):
    answer = 0
    
    for i in range(len(triangle)-1): #인덱스 에러를 막기 위한 범위
        tmp_list = [[] for r in range(i+2)] #다음 줄과의 계산 값을 모두 담을 리스트
        for j in range(len(triangle[i])): #현재 줄의 요소들을 하나씩 가져온다
            left = triangle[i][j] + triangle[i+1][j] #아랫줄 왼쪽 요소와의 계산값
            right = triangle[i][j] + triangle[i+1][j+1] #아랫줄 오른쪽 요소와의 계산값
            tmp_list[j].append(left) #왼쪽값, 오른쪽값 구분하여 tmp_list에 저장
            tmp_list[j+1].append(right)
            
        #print(tmp_list)
            
        for k in range(len(tmp_list)): #tmp_list 요소에 하나씩 접근
            tmp_list[k] = max(tmp_list[k]) #왼쪽, 오른쪽 총 두 개인 경우엔 최댓값 선택
            
        #print(tmp_list)
        
        triangle[i+1] = tmp_list[:] #최댓값들로만 고른 tmp_list를 기존 triangle에 저장
        
        #print(triangle)
        
    answer = max(triangle[len(triangle)-1]) #마지막 줄의 최댓값이 answer
    
    #print(answer)
    
    return answer

solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]])
