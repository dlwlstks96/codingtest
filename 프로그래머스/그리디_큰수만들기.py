# -*- coding: utf-8 -*-


# number을 리스트로 받아 풀려하니 테스트 케이스 하나에서 시간초과가 계속 났다.
# 들어온 문자열 그대로 푸니 효율성이 2배정도 증가하였고 테스트 케이스를 통과할 수 있었다.

def solution(number, k):
    answer = ''
    
    cnt = 0 #골라서 제거한 횟수
    idx = 0 #시작 인덱스
    
    while(cnt < k):
        for i in range(idx, len(number)-1):
            #print(i, i+1, ' / ', number)
            if number[i] == '9':
                continue
            elif number[i] < number[i+1]: #i번째 숫자보다 그 다음 숫자가 더 클 경우
                number = number[0:i] + number[i+1:len(number)] #i번째 숫자만 제거
                cnt += 1
                idx = max(i-1, 0) #시작 인덱스 설정(0 혹은 한 칸 앞)
                break
            elif i == len(number)-2: #끝까지 다 탐색했음에도 위 if문 조건이 없을 경우
                while(cnt < k):
                    number = number[0:len(number)-1] #뒤에서부터 하나씩 제거
                    cnt += 1
                break
    
    answer = number
    
    return answer

solution("4177252841", 4)