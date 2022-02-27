# -*- coding: utf-8 -*-

import itertools as it

a, b = map(int, input().split())

len_a = len(str(a))
len_b = len(str(b))

answer = 0
#1, 1000이 입력되면 2~3자리의 금민수 숫자 탐색 가능
for i in range(len_a+1, len_b): #a, b 사이의 자릿수는 각 자릿수 * 제곱으로 계산 가능
    answer += 2**i

data = ['4', '7']

check = [] #찾은 금민수 숫자 저장

res = it.product(data, repeat = len_a)
for i in res:
    tmp = ''
    for n in i:
        tmp += n
    #print(tmp, answer)
    #지금의 숫자가 a와 b 사이의 숫자고 이전에 찾지 않았다면
    if int(tmp) >= a and int(tmp) <= b and tmp not in check:
        answer += 1
        check.append(tmp)
    
res = it.product(data, repeat = len_b)
for i in res:
    tmp = ''
    for n in i:
        tmp += n
    #print(tmp, answer)
    #지금의 숫자가 a와 b 사이의 숫자고 이전에 찾지 않았다면
    if int(tmp) <= b and int(tmp) >= a and tmp not in check:
        answer += 1
        check.append(tmp)
    #지금 숫자가 b보다 크면 그 뒤론 탐색 불필요
    elif int(tmp) > b:
        break

print(answer)