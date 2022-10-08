import copy
from collections import deque as dq

n, l, r = map(int, input().split())

board = [[-1 for _ in range(n+2)]]

for _ in range(n):
    tmp = list(map(int, input().split()))
    tmp = [-1] + tmp + [-1]
    board.append(tmp)
    
board.append([-1 for _ in range(n+2)])
    
visit = [[-1 for _ in range(n+2)] for _ in range(n+2)] #방문 체크

move = [[-1,0], [1,0], [0,-1], [0,1]]

answer = 0 #국경이동 횟수 카운트
while True:
    
    visitCount = 0 #현재 몇 번째 연합인지
    
    check = False #국경이동 여부 체크
    
    for y in range(1, len(board)-1):
        for x in range(1, len(board[0])-1):
            
            if visit[y][x] == -1: #미방문 국가이면
            
                q = dq([])
                q.append([y, x])
                visit[y][x] = visitCount #현재 연합 번호로 체크
                
                tmpArr = [] #연합 위치 넣을 리스트
                
                count = 1 #연합 내 국가 갯수
                sumVal = board[y][x] #연합 내 총 인구 수
                
                while q:
                    nowPop = q.popleft()
                    nowY = nowPop[0]
                    nowX = nowPop[1]
                    tmpArr.append([nowY, nowX]) #현재 국가를 연합 리스트에 삽입
                    
                    for m in move:
                        nextY = nowY + m[0]
                        nextX = nowX + m[1]
                        
                        #다음 위치와 인구 수 차이가 조건에 만족하고 미방문이며 보드판 범위 이내일때
                        if l <= abs(board[nowY][nowX] - board[nextY][nextX]) <= r and visit[nextY][nextX] == -1 and board[nextY][nextX] != -1:
                            check = True #인구 이동 발생 체크
                            q.append([nextY, nextX])
                            visit[nextY][nextX] = visitCount #현재 연합 번호로 체크
                            count += 1
                            sumVal += board[nextY][nextX]
                
                # !-- 인구 수 조정을 전체 보드판 돌며 진행했는데 그럴 경우 시간 초과 / 전체 보드판을 돌지 말자 -- !
                
                #연합군 내에 시작 국가 이외에 하나라도 더 들어갔다면
                if len(tmpArr) > 1:
                    for arr in tmpArr: #연합 리스트 하나씩 꺼내어 인구 수 조정
                        board[arr[0]][arr[1]] = sumVal // count
                    
            visitCount += 1 #연합군 번호 증가
                            
    #전부 미방문 처리로 초기화
    for y in range(1, len(visit)-1):
        for x in range(1, len(visit[0])-1):
            visit[y][x] = -1
        
    if check == False: #국가 이동 발생 안했을 시
        print(answer)
        break
    else: #국가 이동 발생했을 경우
        answer += 1
