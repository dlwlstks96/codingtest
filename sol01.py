# -*- coding: utf-8 -*-

#프로그래머스_정렬_가장큰수

#numbers = [0, 0, 0]
#numbers = [989, 98]
numbers = [3, 34, 32]
#numbers = [3, 30, 34, 5, 9, 999]

def solution(numbers):
    answer = ''
    
    #numbers의 요소들을 문자열로 변경
    numbers = list(map(str, numbers))
    
    #sort(reverse)로 내림차순 정렬
    #x*3의 이유는 numbers의 원소가 0 이상 1000이하이기에
    numbers.sort(key = lambda x: x*1, reverse = True)
    #66 22 1010
    
    print(numbers)
    
    #[0,0]의 경우 00이 나오기에 int로 변경 후 다시 str로
    return str(int(''.join(numbers)))

solution(numbers)