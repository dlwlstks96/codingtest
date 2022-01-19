# -*- coding: utf-8 -*-

#프로그래머스_완전탐색_카펫

brown = 50
yellow = 22

def solution(brown, yellow):
    answer = []
    
    #전체 타일의 갯수는 brown + yellow여야 한다.
    tmp = brown + yellow
    
    for i in range(1, tmp+1):
        if tmp % i == 0: #전체 타일 갯수의 약수
            x = i #가로 타일 갯수
            y = int(tmp/i) #세로 타일 갯수
            #brown이 두께 1로 yellow를 감싸고 있기에
            #가로-2*세로*2의 크기가 전체 yellow여야 한다.
            if (x-2)*(y-2) == yellow and x >= y:
                answer.append(x)
                answer.append(y)
    
    #print(answer)
        
    return answer

solution(brown, yellow)