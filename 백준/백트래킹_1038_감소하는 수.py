# -*- coding: utf-8 -*-

import sys
import heapq

n = int(input())
#n = int(sys.stdin.readline())

one, two, three, four, five, six, seven, eight, nine = 1, 2, 3, 4, 5, 6, 7, 8, 9
hq = []

find = False #찾았는지 bool

if n < 9:
    print(n) #그냥 n 출력하고 종료
    sys.exit()
else: #heapq에 1~9 넣어주기
    heapq.heappush(hq, one)
    heapq.heappush(hq, two)
    heapq.heappush(hq, three)
    heapq.heappush(hq, four)
    heapq.heappush(hq, five)
    heapq.heappush(hq, six)
    heapq.heappush(hq, seven)
    heapq.heappush(hq, eight)
    heapq.heappush(hq, nine)
    
    count = 0 #몇번째 감소하는 숫자인지
    
    while hq:
        nowNum = heapq.heappop(hq) #heapq 안의 작은 숫자부터 꺼내기
        if nowNum > 9876543210: #꺼낸 숫자가 감소하는 숫자의 최대치보다 클 경우
            print(-1)
            break
        count += 1 #정상적인 감소하는 수라면 카운트 증가
        if count == n: #찾는 순번의 감소 수라면 bool 처리하고 출력
            find = True
            print(nowNum)
            break
        
        for i in range(10): #현재의 숫자에 뒤에 0~9 붙여주기
            tmp = str(nowNum) + str(i)
            check = True
            for j in range(len(tmp)-1):
                if tmp[j] <= tmp[j+1]:
                    check = False #감소수 조건 위
                    break
            if check == False: #시간 효율을 위해 현 숫자에 더 안 붙인다
                break
            else: #붙였는데 감소 수라면 heapq에 삽입
                heapq.heappush(hq, int(tmp))
                
if find == False: #위 while문에서 순번의 감소 수를 찾지 못했다면 -1 출력
    print(-1)