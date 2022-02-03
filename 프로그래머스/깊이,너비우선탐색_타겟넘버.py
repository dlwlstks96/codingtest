# -*- coding: utf-8 -*-

import itertools as it

def solution(numbers, target):
    answer = 0
    
    for i in range(len(numbers)+1):
        tmp = it.combinations(range(len(numbers)), i) #0~len(numbers)만큼 뽑
        
        for j in tmp: #tmp에서 튜플 하나씩 꺼내기
            tmp_numbers = numbers[:] #numbers 원본 복사
            for k in j: #튜플에서 값 하나씩 꺼내기
                tmp_numbers[k] = -tmp_numbers[k] #해당 인덱스 음수
                
            sum_nums = sum(tmp_numbers)
        
            if sum_nums == target: #tmp_numbers의 총합이 target일 경우
                #print(tmp_numbers)
                #print('==============')
                answer += 1
        
    print(answer)
    
    return answer

solution([1, 1, 1, 1, 1], 3)