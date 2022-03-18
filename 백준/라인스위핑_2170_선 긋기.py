# -*- coding: utf-8 -*-

import sys
import heapq

n = int(sys.stdin.readline())

data =[]

for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())
    heapq.heappush(data, (x, y))
    
nowLine = heapq.heappop(data) #첫 시작점
start = nowLine[0]    

answer = 0 #그어진 길이
while data:
    nextLine = heapq.heappop(data) #다음 선분
    if nextLine[1] <= nowLine[1]: #다음 선분이 현 선분 안에 포함일 경우
        continue
    elif nextLine[0] > nowLine[1]: #다음 선분이 현 선분을 아예 벗어날 경우
        answer += nowLine[1] - start #길이 추가
        nowLine = nextLine #다음 선분을 현 선분으로
        start = nowLine[0]
    elif nextLine[0] <= nowLine[1] and nextLine[1] > nowLine[1]: #다음 선분이 현 선분 걸쳐 있을 때
        nowLine = nextLine #다음 선분을 현 선분으로
    
answer += (nowLine[1] - start)
        
print(answer)