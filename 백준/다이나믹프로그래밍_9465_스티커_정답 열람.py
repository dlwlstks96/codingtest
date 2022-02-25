# -*- coding: utf-8 -*-

t  = int(input())

for _ in range(t):
    n = int(input())
    data1 = list(map(int, input().split())) #윗줄
    data2 = list(map(int, input().split())) #아랫줄
    
    if n == 1:
        answer = max(data1[0], data2[0])
    elif n == 2:
        answer = max(data1[0] + data2[1], data1[1] + data2[0])
    else: # n > 2
        table = [[0 for i in range(n)], [0 for i in range(n)]]
        table[0][0] = data1[0]
        table[1][0] = data2[0]
        table[1][1] = data1[0] + data2[1]
        table[0][1] = data1[1] + data2[0]
        for i in range(2, n): #2번 인덱스부턴 본인이 i번째 일때 왼쪽 대각선 높이의 max(i-2, i-1) + 본인이다.
            table[0][i] = max(table[1][i-2], table[1][i-1]) + data1[i]
            table[1][i] = max(table[0][i-2], table[0][i-1]) + data2[i]
        answer = max(table[0][n-1], table[1][n-1])
        # print(data1, data2)
        # print()
        # print(table)
    print(answer)

'''

import sys

t = int(input())

for _ in range(t):
    # n = sys.stdin.readline()
    # n = int(n)
    # data1 = list(map(int, sys.stdin.readline().split())) #윗줄
    # data2 = list(map(int, sys.stdin.readline().split())) #아랫줄
    n = int(input())
    data1 = list(map(int, input().split())) #윗줄
    data2 = list(map(int, input().split())) #윗줄
    
    
    # tmp1 = [] #윗줄부터 시작한 대각선들 값
    # tmp2 = [] #아랫줄부터 시작한 대각선들 
    tmp1 = 0
    tmp2 = 0
    for i in range(n):
        if i % 2 == 0: #윗줄의 0, 2, 4번 인덱스..
            # tmp1.append(data1[i])
            # tmp2.append(data2[i])
            tmp1 += data1[i]
            tmp2 += data2[i]
        else: #윗줄의 1, 3, 5번 인덱스..
            # tmp1.append(data2[i])
            # tmp2.append(data1[i])
            tmp1 += data2[i]
            tmp2 += data1[i]
        
    #어느 대각선 방향의 원소들 합이 더 큰지 체크, 크면 메인으로 선정
    # if sum(tmp1) > sum(tmp2):
    #     mainLine = tmp1
    #     subLine = tmp2
    # else:
    #     mainLine = tmp2
    #     subLine = tmp1
    if tmp1 > tmp2:
        mainLine = 'UP'
        subLine = 'DOWN'
        answer = tmp1
    else:
        mainLine = 'DOWN'
        subLine = 'UP'
        answer = tmp2
        
    #answer = sum(mainLine)
        
    for i in range(n):
        nowSubMax = max(subLine)
        nSMIdx = subLine.index(nowSubMax)
        
        if nSMIdx >= 1 and nSMIdx <= n-2:
            compareSum = mainLine[nSMIdx] + mainLine[nSMIdx-1] + mainLine[nSMIdx+1]
        elif nSMIdx == 0:
            compareSum = mainLine[nSMIdx] + mainLine[nSMIdx+1]
        else: #nSMIdx >= n-1
            compareSum = mainLine[nSMIdx] + mainLine[nSMIdx-1]
            
        #print(answer, nowSubMax, nSMIdx, compareSum)
        
        if nowSubMax > compareSum: #만약 교체가 이루어져야 한다면
            answer -= compareSum
            answer += nowSubMax
            subLine[nSMIdx] = -1
        else:
            subLine[nSMIdx] = -1 #교체 필요 없으면 subLine 최대값을 -1
            
    print(answer)
    
'''  