# -*- coding: utf-8 -*-

def solution(s):
    answer = 0
    
    data = []
    
    res = []
    
    if len(s) < 2:
        return 1
    
    for i in range((len(s)//2), 0, -1): #4, 3, 2, 1
        data = []
        start = 0
        end = i
        for j in range(len(s)//i):
            data.append(s[start:end])    
            #print(i, data)
            start = end
            end = end + i
        #print(i, data)
        
        prev = ''
        count = 1
        tmp = ''
        for j in data:
            if j == prev: #이번 문자가 저번 문자와 같을 때(반복)
                count += 1
            else: #이번 문자가 저번 문자와 다를 때(반복 x)
                if count > 1: #반복 횟수가 2 이상일때
                    tmp += str(count) + prev
                else: #반복 횟수가 2 미만일때(0 혹은 1)
                    tmp += prev
                prev = j
                count = 1
        if count > 1: #마지막 문자가 반복 횟수 2 이상으로 남아 있을 때
            tmp += str(count) + prev
        else:
            tmp += prev
        if len(s) % i != 0: #자른 구간 이외에 남은 문자열이 있는 경우
            tmp += s[len(s)-1: ((len(s)//i)*i)-1: -1]
            #print(len(s)-1, i)
            
        #print(tmp, len(tmp))
        res.append(len(tmp))    
    #print(min(res))
                
    answer = min(res)
    
    return answer

print(solution("a"))

'''
aabbaccc
2a2ba3c / 1 = 7

abcabcdede
2abcdede / 3 = 8

ababcdcdababcdcd
2ababcdcd / 8 = 9

abcabcabcabcdededededede
2abcabc2dedede / 6 = 14

xababcdcdababcdcd
xababcdcdaabbcdcd / x = 17

xababcdcdaabbcdcd
xababcdcdabadcdc




'''