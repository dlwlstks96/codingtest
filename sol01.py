# -*- coding: utf-8 -*-

#프로그래머스_정렬_H-index

#citations = [3, 0, 6, 1, 5]
citations = [9, 7, 6, 2, 1]

def solution(citations):
    answer = 0
    
    citations.sort(reverse = True) #내림차순 정렬
    
    for i in range(len(citations)):
        #리스트의 i번째 값이 i+1 이상일 경우
        #요구 조건에 부합
        if citations[i] >= i+1:
            answer = i+1
    
    return answer

solution(citations)