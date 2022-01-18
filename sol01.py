# -*- coding: utf-8 -*-

#프로그래머스_완전탐색_소수찾기

numbers = "12345"

import itertools as it

def solution(numbers):
    answer = 0
    
    tmpNumList = [] #조합된 숫자들을 담기 위함(중복 확인)
    
    #1개부터 numbers의 총 갯수만큼 뽑아 조합
    #itertools 라이브러리 이용
    for i in range(1, len(numbers)+1):
        it_list = it.permutations(numbers, i)
        
        for j in it_list:
            tmpNum = ''
            for k in j:
                tmpNum += k #리스트의 요소들을 문자열로 합침
                
            tmpNum = int(tmpNum) #str을 int로 바꿔줌
            
            if tmpNum not in tmpNumList: #소수 확인 과정이 중복된 숫자인지 확인
                for k in range(1, tmpNum): #1부터 숫자-1까지 다 나눠본다
                    if tmpNum % k == 0 and k != 1: #1이 아닌 숫자로 나누어 떨어지는지 확인
                        break 
                    elif k == tmpNum - 1: #1이 아닌 숫자로 나누어 떨어지지 않을 경우
                        answer += 1
                tmpNumList.append(tmpNum)
    
    return answer

solution(numbers)