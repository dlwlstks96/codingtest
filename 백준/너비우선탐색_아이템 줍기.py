from collections import deque as dq

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 1000000000
    
    #거리가 1 차이인 사각형 간의 변이 없을 경우에도 건너가는 것을 방지하기 위해 모든 좌표 거리 2배
    board = [[-1 for _ in range(104)]] #그래서 range(52)가 아닌 range(104)
    for _ in range(100):
        tmp = [-1]
        tmp += [0 for i in range(100)]
        tmp += [-1]
        board.append(tmp)
    board.append([-1 for _ in range(104)])
    
    for r in rectangle:
        leftX = r[0]*2
        leftY = r[1]*2
        rightX = r[2]*2
        rightY = r[3]*2
        
        for y in range(leftY+1, rightY): #변 좌표를 제외하고
            for x in range(leftX+1, rightX):
                board[y][x] = -2 #사각형 내부 진입 금지 처리
                
        for y in range(leftY, rightY+1):
            if board[y][leftX] == 0: #아무것도 안놓여져 있는 공간이라면
                board[y][leftX] = 1
            if board[y][rightX] == 0: #0인지 확인을 안하면 다른 사각형 내부에 선을 그리게 된다
                board[y][rightX] = 1
            
        for x in range(leftX, rightX+1):
            if board[leftY][x] == 0:
                board[leftY][x] = 1
            if board[rightY][x] == 0:
                board[rightY][x] = 1
                
    q = dq([])
    
    q.append([characterY*2, characterX*2, 0])
    board[characterY*2][characterX*2] = -2 #visit 처리
    
    move = [[-1, 0], [1, 0 ], [0, -1], [0, 1]]
    
    while q:
        
        nowPop = q.popleft()
        nowY = nowPop[0]
        nowX = nowPop[1]
        nowCount = nowPop[2]
        
        #print(nowPop)
        
        if nowY == itemY*2 and nowX == itemX*2:
            answer = min(answer, nowCount//2)
            continue
        
        for m in move:
            nextY = nowY + m[0]
            nextX = nowX + m[1]
            
            if board[nextY][nextX] == 1: #이동 가능 경로
                q.append([nextY, nextX, nowCount + 1])
                board[nextY][nextX] = -2
    
    return answer
