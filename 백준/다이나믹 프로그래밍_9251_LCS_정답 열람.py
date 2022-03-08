# -*- coding: utf-8 -*-

#https://happylsm76.tistory.com/entry/%EB%B0%B1%EC%A4%80-9251%EB%B2%88LCS-with-Python

import sys

A = sys.stdin.readline().strip().upper()
B = sys.stdin.readline().strip().upper()

lcs = [[0] * (len(A)+1) for _ in range(len(B)+1)]

for i in range(1,len(B)+1) : #2차원 배열을 통한 규칙성
  for j in range(1,len(A)+1) :
    if B[i-1] == A[j-1] :
      lcs[i][j] = lcs[i-1][j-1] + 1
    else :
      lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])

'''아래가 내 풀이(시간초과)

import itertools as it
import sys

data1 = str(input())
data2 = str(input())

len_data = len(data1)
while len_data > 0:
    res = it.combinations(data1, len_data)
    res2 = list(it.combinations(data2, len_data))
    for r in res: #순열 조합 뽑기
        for r2 in res2:
            if r == r2:
                print(len(r))
                sys.exit()
        
    len_data -= 1
    '''