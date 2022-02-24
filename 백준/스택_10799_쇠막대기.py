# -*- coding: utf-8 -*-

#스택 문제

#nowBar와 endBar를 나누어 처리해주는 것이 핵심이다

bracket = str(input())

answer = 0
idx = 0

nowBar = 0
endBar = 0

while(idx <= len(bracket)-1):
    if bracket[idx] == '(' and bracket[idx+1] == ')':
        answer += nowBar
        answer += endBar
        endBar = 0
        idx += 2
        #print(nowBar, endBar, answer)
    elif bracket[idx] == '(' and bracket[idx+1] == '(':
        nowBar += 1
        idx += 1
    elif bracket[idx] == ')':
        nowBar -= 1
        endBar += 1
        idx += 1

answer += endBar
    
print(answer)        