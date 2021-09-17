# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

n,m = map(int, input().split())

board = [] #입력 받는 체스판
count = [] #뒤집어야할 갯수 정보를 담기 위한 리스트

for i in range(n):
    board.append(input())

for i in range(n-7):
    for j in range(m-7): #i, j로 전체 체스판에서 시작점을 잡기 위함
        start_white_check = 0 #'W'로 시작할 경우 바뀐 칸의 갯수 카운트
        start_black_check = 0 #'B'로 시작할 경우 바뀐 칸의 갯수 카운트
        for a in range(i, i+8):
            for b in range(j, j+8): #시작점에서부터 8x8 크기의 체스칸 확인하게 해줌
                #a, b 합이 짝수면 시작점의 색과 같아야하고 홀수의 경우 달라야 한다
                if (a+b) % 2 == 0:
                    if board[a][b] != 'W': #시작점이 'W'라는 뜻
                        start_white_check += 1 #'W'로 시작했을 경우의 변수 카운트
                    if board[a][b] != 'B': #시작점이 'B'라는 뜻
                        start_black_check += 1 #'B'로 시작했을 경우의 변수 카운트
                else:
                    if board[a][b] != 'B': #시작점이 'W'라는 뜻
                        start_white_check += 1 #'W'로 시작했을 경우의 변수 카운트
                    if board[a][b] != 'W': #시작점이 'B'라는 뜻
                        start_black_check += 1 #'B'로 시작했을 경우의 변수 카운트
        count.append(min(start_white_check, start_black_check))
        
print(min(count))                 