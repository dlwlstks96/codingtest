# -*- coding: utf-8 -*-

a, p = input().split()
a = str(a) #문자열로 받아 자릿수 쪼개기 위함
p = int(p)

history = [] #지금까지 나왔던 숫자들을 저장
history.append(int(a))

while True:
    nextNum = 0
    for n in a:
        tmp = (int(n))**p #각 자릿수(n)을 p제곱
        nextNum += tmp
    if nextNum not in history: #지금의 숫자가 이전에 안나왔었다면
        history.append(nextNum)
        a = str(nextNum) #다음에 처리할 문자로 저장
    else: #지금의 숫자가 이전에 나왔다면
        answer = history.index(nextNum)
        break
    #print(history)
    
print(answer)