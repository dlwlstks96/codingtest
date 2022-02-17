# -*- coding: utf-8 -*-

import math

#약수는 항상 대칭성의 원리를 만족함
#16의 약수 1, 2, 4, 8, 16은 중앙값 4를 중심으로 했을 때,
#2로 곱하고, 나누고를 통해서 만들 수 있기 때문
#나는 int(i)//2 까지 체크하면 될 거라 생각했는데
#사실 int(i)//2 값은 약수 중 가장 큰 수일 것이다
#내가 생각한 것을 제대로 구현한 것은 int(math.sqrt(int(i)))+1이 맞다

def solution(n, k):
    answer = 0
    
    tmp = ''
    
    while(n >= k):
        tmp = str(n % k) + tmp #나머지들 이어 붙이기
        n = n//k
    
    tmp = str(n) + tmp #마지막 나머지까지 붙이기, 진수 변환 완료
    #211020101011
    
    prime_list = tmp.split('0') #0을 기준으로 split
    
    #print(prime_list)
    
    for i in prime_list:
        if i == '1' or i == '': #예외 처리
            continue
        #print(math.sqrt(int(i)))
        for j in range(2, int(math.sqrt(int(i)))+1): #2부터 중앙값(제곱근)까지 체크
            
            if int(i) % j == 0:
                answer -= 1 #나중에 무조건 +1 해주기에 소수면 -1하고 반복 중지
                break
        answer += 1
        
    #print(answer)
    
    return answer

solution(437674, 3)