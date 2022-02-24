# -*- coding: utf-8 -*-

import sys

n = int(input())

data = []

for i in range(n):
    start, end = sys.stdin.readline().split(' ')
    #start, end = input().split(' ')
    start = int(start)
    end = int(end)
    data.append([start, end])
    
data.sort(key=lambda x: (x[1], x[0])) #끝나는 시간, 시작 시간 기준으로 정렬

#print(data)
   
nowTime = 0

idx = 0
answer = 0

while idx < len(data):
    if data[idx][0] >= nowTime: #지금 시간에 시작할 수 있다면
        nowTime = data[idx][1] #해당 회의 끝나는 시간으로 변경
        #print(data[idx])
        idx += 1
        answer += 1 #회의 갯수 카운트
    else: #idx 값의 시작 시간이 시작할 수 없다면
        idx += 1

print(answer)
    