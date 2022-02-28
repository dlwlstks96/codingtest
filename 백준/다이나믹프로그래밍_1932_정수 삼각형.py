# -*- coding: utf-8 -*-

n = int(input())

data = [[] for i in range(n)]

for i in range(n):
    data[i] = list(map(int, input().split()))
    
for i in range(1, n):
    for j in range(len(data[i])):
        if j == 0: #0번 인덱스
            data[i][j] += data[i-1][j]
        elif j == len(data[i])-1: #마지막 인덱스
            data[i][j] += data[i-1][j-1]
        else: #나머지 가운데 인덱스
            data[i][j] += max(data[i-1][j-1], data[i-1][j])
            
print(max(data[len(data)-1])) #끝줄에서 최대값 출력