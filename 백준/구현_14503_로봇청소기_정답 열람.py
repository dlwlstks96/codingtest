# -*- coding: utf-8 -*-

#https://wewinserv.tistory.com/173

import sys

input = sys.stdin.readline
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def clean(x, y, d):
    global ans
    if a[x][y] == 0:
        a[x][y] = 2
        ans += 1
    for _ in range(4):
        nd = (d + 3) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if a[nx][ny] == 0:
            clean(nx, ny, nd)
            return
        d = nd
    nd = (d + 2) % 4
    nx = x + dx[nd]
    ny = y + dy[nd]
    if a[nx][ny] == 1:
        return
    clean(nx, ny, d)


n, m = map(int, input().split())
x, y, d = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
clean(x, y, d)
print(ans)


'''아래가 내 풀이 / 아직 문제 이해가 안된다ㅠ
# n, m = 3, 3
# robot = [1, 1, 0]
# board = [
#     [1, 1, 1],
#     [1, 0, 1],
#     [1, 1, 1],
#     ]

# n, m = 9,7
# robot = [6, 2, 1]
# board = [
#     [1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1],
#     [1, 0, 1, 0, 1, 0, 1],
#     [1, 0, 1, 1, 1, 1, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 0, 0, 1, 1, 0, 1],
#     [1, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1],
#     ]


n, m = 11, 10
robot = [7, 4, 0]
board = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    ]
# board = [
#       0  1  2  3  4  5  6  7  8  9        
#    0 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#    1 [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
#    2 [1, 0, 0, 0, 1, 1, 1, 1, 0, 1],
#    3 [1, 0, 0, 1, 1, 0, 0, 0, 0, 1],
#    4 [1, 0, 1, 1, 0, 0, 0, 0, 0, 1],
#    5 [1, 0, 0, 2, 2, 0, 0, 0, 0, 1],
#    6 [1, 0, 2, 2, 2, 2, 0, 1, 0, 1],
#    7 [1, 2, 2, 2, 2, 2, 1, 1, 0, 1],
#    8 [1, 2, 2, 2, 2, 2, 1, 1, 0, 1],
#    9 [1, 0, 2, 2, 2, 2, 0, 0, 0, 1],
#    0 [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     ]


# n, m = map(int, input().split())
# robot = list(map(int, input().split()))
# board = [[] for j in range(n)]
# for i in range(n):
#     board[n] = list(map(int, input().split()))

nowDirection = [[-1, 0], [0, 1], [1, 0], [-1,0]] #현재 청소기가 바라보는 방향
viewDirection = [[0,-1], [-1,0], [0,1], [1,0]] #청소기가 바라보는 방향에 따라 왼쪽 탐색
clean = 0 #청소 지역 카운트

cleanHistory = []
loop = True
while loop:
    #청소기의 현재 위치
    nowY = robot[0]
    nowX = robot[1]
    print(nowY, nowX)
    
    if board[nowY][nowX] == 0: #현재 위치가 빈 공간으로 청소 가능 상태
        board[nowY][nowX] = 2 #청소 완료
        print('clean!!!!')
        cleanHistory.append([nowY,nowX])
        clean += 1
        
    for i in range(4):
        nextY = robot[0] + viewDirection[robot[2]][0] #탐색할 왼쪽 방향
        nextX = robot[1] + viewDirection[robot[2]][1]
        print(nowY, nowX, '/', nextY, nextX)
        print('======')
        
        if board[nextY][nextX] == 0: #왼쪽 방향이 청소하지 않은 공간이라면
            robot[2] -= 1 #회전해서 이동
            if robot[2] < 0:
                robot[2] = 3 #음수인 상황 예외 처리
            robot[0], robot[1] = nextY, nextX #해당 방향으로 이동
            break
        else: #왼쪽 방향에 청소할 공간이 없다면
            robot[2] -= 1 #그 방향으로 회전
            if robot[2] < 0: #음수인 상황 예외 처리
                robot[2] = 3
            if i == 3: #모든 방향을 다 탐색했음에도 왼쪽 방향에 공간이 없는 것
                print('back!!')
                backY = robot[0] - nowDirection[robot[2]][0] #후진할 방향
                backX = robot[1] - nowDirection[robot[2]][1]
                if board[backY][backX] == 1: #후진할 방향이 벽이라면
                    print(nowY, nowX, robot[2], backY, backX)
                    loop = False #작동 중지
                else: #후진할 방향이 있다면
                    robot[0] = backY
                    robot[1] = backX
                    break
        
    
print(clean)
print(cleanHistory)

'''