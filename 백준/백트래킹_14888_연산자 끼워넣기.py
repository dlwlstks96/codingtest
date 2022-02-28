# -*- coding: utf-8 -*-

import itertools as it
from collections import deque as dq

# n = 6
# num = [3, 4, 5] #연산할 숫자들
# cal_num = [1, 0, 1, 0] #연산자의 갯수
n = int(input())
num = list(map(int, input().split()))
cal_num = list(map(int, input().split()))


cal_list = ['+', '-', '*', '/'] #연산자 종류

cal = [] #최종 연산자의 종류별 갯수

for i in range(len(cal_num)):
    for j in range(cal_num[i]):
        cal.append(cal_list[i])
        
#print(cal) #연산자 종류 및 갯수 획득

minAnswer = 1000000001 #가장 큰 수로 설정
maxAnswer = -1000000001 #가장 작은 수로 설정

iteration = set(it.permutations(cal, len(cal))) #연산자 모든 조합 획득, 중복 제거
for i in iteration:
    #print(i)
    q = []
    q = dq(q) #deque 선언
    for j in range(len(num)-1):
        q.append(num[j])
        q.append(i[j]) #num-1 인덱스까지 숫자, 연산자 순서로 집어넣기
    q.append(num[len(num)-1]) #마지막 숫자까지 집어넣기
    #print(q)

    tmp = q.popleft() #처음 숫자 집어넣기
    while q:
        nextCal = q.popleft() #다음 연산자
        nextNum = q.popleft() #그 다음 숫자
        if nextCal == '+':
            tmp += nextNum
        elif nextCal == '-':
            tmp -= nextNum
        elif nextCal == '*':
            tmp *= nextNum
        elif nextCal == '/':
            if tmp >= 0: #양수를 나눌때
                tmp = tmp // nextNum
            else: #음수를 나눌때
                tmp = -tmp #양수로 바꾸고
                tmp = tmp // nextNum #몫을 취하고
                tmp = -tmp #다시 음수로 바꾼다
    
    minAnswer = min(tmp, minAnswer)
    maxAnswer = max(tmp, maxAnswer)
                
print(maxAnswer)
print(minAnswer)
