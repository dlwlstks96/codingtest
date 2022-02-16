# -*- coding: utf-8 -*-

# 아래는 구글링하여 찾은 정답

import sys


n, c = map(int, sys.stdin.readline().split())
house = []
for _ in range(n):
    house.append(int(sys.stdin.readline()))
house.sort() #집 좌표 정렬

min_gap = 1 #두 집 사이의 최소 거리
max_gap = house[-1] - house[0] #두 집 사이의 최대 거리
result = 0

while (min_gap <= max_gap): #탈출 조건
    gap = (min_gap + max_gap) // 2 #중간 값이 현재의 최대
    current = house[0] #첫번째 집
    count = 1 #설치
    for i in range(1, len(house)): #current와의 거리가 현재의 gap 이상이면
        if house[i] >= current + gap:
            current = house[i]
            count += 1
    if count >= c: #설치한 공유기 수가 입력받은 c보다 크거나 같으면
        min_gap = gap + 1 #gap 간격을 더 늘려 설치해본다
        result = gap #지금이 답일지 모르니 우선은 저장
    else: #설치한 공유기 수가 입력받은 c보다 작으면 무조건 gap 간격을 좁혀야 한다
        max_gap = gap - 1

print(result)


''' 아래는 내가 푼 오답, 시간이 다 되어 완성조차 못하였다

import sys

n, c = int(input())

homeList = []
checkList = [0 for i in range(n)]

for i in range(n):
    x = int(sys.stdin.readlint())
    homeList.append(x)
    
homeList.sort()

if (n / 2) <= c: #5집 중 3개 이상 공유기, 가장 멀리 설치하고 이분탐색 실시
    for i in range(c):
        if i == 0: #가장 처음 집 설치
            checkList[0] = 1
        elif i == 1: #가장 마지막 집 설치
            checkList[1] = 1
        else: #이후 이분 탐색
            
else: #5집 중 2개 이하 공유기, 1번 집부터 +2씩 설치하면 된다

'''
    