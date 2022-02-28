# -*- coding: utf-8 -*-

#import copy
import itertools as it
from collections import deque as dq

n, m = map(int, input().split())
# n, m = 7, 7

board = [[] for i in range(n)]

for i in range(n):
    tmp = list(map(int, input().split()))
    board[i] = tmp

def bfs(new_board, xy, visit):
    q = []
    q = dq(q) #큐로 선언
    q.append(xy)
    visit[xy[0]][xy[1]] = 1 #바이러스 시작 지점 방문 체크
    move = [[0, 1], [0, -1], [1, 0], [-1, 0]] #상하좌우 이동
    while q:
        nowXY = q.popleft()
        #visit[nowXY[0]][nowXY[1]] = 1 #방문한 위치 체크
        new_board[nowXY[0]][nowXY[1]] = 2 #보드판에 바이러스 표시
        for i in range(4):
            nextXY = [nowXY[0]+move[i][0], nowXY[1]+move[i][1]]
            try: #다음 좌표가 미방문이고 빈공간일때에만
                if visit[nextXY[0]][nextXY[1]] == 0 and new_board[nextXY[0]][nextXY[1]] == 0 and nextXY[0] > -1 and nextXY[1] > -1:
                    q.append(nextXY)
                    visit[nextXY[0]][nextXY[1]] = 1 #방문한 위치 체크
            except:
                continue 
            
    return new_board
        

zeroIdxList = [] #빈공간 저장
twoIdxList = [] #바이러스 저장
for i in range(len(board)):
    for j in range(len(board[i])):
        if board[i][j] == 0:
            zeroIdxList.append([i, j])
        elif board[i][j] == 2:
            twoIdxList.append([i, j])            
            
#print(zeroIdxList) #빈공간인 위치의 인덱스들 모두 저장
#print(twoIdxList) #바이러스 위치의 인덱스들 모두 저장

new_board = board
zeroCountMax = 0
res = it.combinations(zeroIdxList, 3)
for r in res: #저장한 빈공간 인덱스들 중 3개씩 뽑아 경우의 수 조합
    #new_board = copy.deepcopy(board) #보드판 카피
    for i in r:
        new_board[i[0]][i[1]] = 1 #뽑힌 세 위치에 벽 세우기
    
    visit = [[0 for i in range(m)] for j in range(n)] #방문한 위치 표시
    for xy in twoIdxList: #바이러스 위치에서부터 bfs 시작
        bfs(new_board, xy, visit)
        
    zeroCount = 0 #안전지역 카운트
    for i in range(len(new_board)):
        for j in range(len(new_board[i])):
            if new_board[i][j] == 0:
                zeroCount += 1
        
    for i in zeroIdxList:
        new_board[i[0]][i[1]] = 0 #기존의 빈 공간 다시 0으로 설정
    
    zeroCountMax = max(zeroCount, zeroCountMax)
    #print(zeroCountMax)
        
    #new_board.clear()
    
print(zeroCountMax)