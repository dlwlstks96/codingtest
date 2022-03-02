# -*- coding: utf-8 -*-

import math

#n = int(input())
# N = 8

# paper = [
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [1, 1, 0, 0, 0, 0, 1, 1],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [0, 0, 0, 0, 1, 1, 0, 0],
#     [1, 0, 0, 0, 1, 1, 1, 1],
#     [0, 1, 0, 0, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1],
#     [0, 0, 1, 1, 1, 1, 1, 1]
#     ]

import sys

N = int(sys.stdin.readline())
paper = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] 

result = []

def solution(x, y, N) :
  color = paper[x][y] #현재 인덱스의 색깔
  for i in range(x, x+N) : #지정된 크기만큼 모두 확인
    for j in range(y, y+N) :
      if color != paper[i][j] : #지정된 크기 안에 하나라도 색깔이 다를 경우
        solution(x, y, N//2) #한 변의 길이를 반으로 잘라 네등분 모두 재귀
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return
  if color == 0 : #여기까지 코드가 왔다는건 위의 if문을 통과했다는 것으로 결과 반영
    result.append(0)
  else :
    result.append(1)


solution(0,0,N)
print(result.count(0))
print(result.count(1))

'''아래가 내 풀이

squareListA = [[] for i in range(round(math.log2(n)))] #0으로 만든 비교안
squareListB = [[] for i in range(round(math.log2(n)))] #1로 만든 비교안

for i in range(len(squareListA)):
    tmp = [[0 for i in range(int(2**(i+1)))] for j in range(int(2**(i+1)))]
    squareListA[i] = tmp
    tmp2 = [[1 for i in range(int(2**(i+1)))] for j in range(int(2**(i+1)))]
    squareListB[i] = tmp2
    
    
zeroCnt = 0
oneCnt = 0

term = 2
while True:
    for i in range(0, len(board), term):
        for j in range(0, len(board), term):
            for y in range(len(squareListA)):
                for x in range(len())

'''