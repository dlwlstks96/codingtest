# -*- coding: utf-8 -*-

#s = '55-50+40'
#s = '10+20+30+40'
#s = '00009-00009'

s = str(input())

s = s.split('-') # -단위로 끊으면 최솟값을 만드는 괄호 단위로 묶게 된다

data = []
for i in s:
    if '+' not in i: # +가 없다면 해당 리스트는 순수 숫자 하나
        data.append(int(i))
    else: #+연산자가 단위 리스트 안에 있을 시 +로 구분하여 숫자들 총합
        i = i.split('+')
        i = map(int, i) #str을 int로 묶어 반환
        data.append(sum(i))
        
answer = data[0]
if len(data) > 1:
    for i in range(1, len(data)):
        answer -= data[i]
        
print(answer)