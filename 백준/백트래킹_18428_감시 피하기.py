from collections import deque as dq
import itertools as it

'''
열심히 구현하면 그리 어려운 문제는 아니었다
다만 평소와 조금 다른 부분이 있다
보통 탐색 문제는 하나의 점으로부터 출발해서 4방향으로 뻗어나가며 탐색하기에
방문 정보를 저장해줬다. 그래야 무한 반복을 방지하고 효율적이기에..
그러나 이 문제는 여러 지점의 선생님 위치에서 각 방향으로만 직진하며 탐색한다.
즉 직진하기에 원점으로 되돌아 갈 일이 없기에 방문 정보를 저장할 필요가 없고
방문 정보를 저장할 시 다른 경로가 지나간 길을 지나칠 수 없기에 틀리게 된다.
평소 deque 이용해서 탐색할땐 10에 9 은 방문 처리해주는데 이런 신박한 경우도 있다.
'''

n = int(input())

board = [[] for _ in range(n+2)]

board[0] = [-1 for _ in range(n+2)]

for i in range(1, n+1):
    tmp = list(input().split())
    board[i].append(-1)
    for t in tmp: #빈 공간 0, 선생님 1, 학생 2, 장애물 3
        if t == 'X':
            board[i].append(0)
        elif t == 'T':
            board[i].append(1)
        elif t == 'S':
            board[i].append(2)
    board[i].append(-1)
        
board[-1] = [-1 for _ in range(n+2)]

zeroIdxList = [] #복도 위치 저장
teacherIdxList = [] #선생님 위치 저장

for i in range(1, n+1):
    for j in range(1, n+1):
        if board[i][j] == 0: #장애물 놓을 수 있는 복도라면
            zeroIdxList.append([i, j])
        elif board[i][j] == 1: #선생님의 위치라면
            teacherIdxList.append([i, j])

move = [[-1, 0], [1, 0], [0, -1], [0, 1]] #상하좌우

pick = it.combinations(zeroIdxList, 3)
for p in pick:
    
    for setIdx in p: #뽑힌 복도 공간에 장애물 놓기
        board[setIdx[0]][setIdx[1]] = 3
        
    q = dq([])
    
    for t in teacherIdxList: 
        for m in move: #선생님 이동 방향
            q.append([t, m]) #선생님 위치, 이동 방향 삽입 ([[], []])
        
    findStudent = False #학생 찾았는지 여부
    
    while q:
        
        nowPop = q.popleft()
        nowY = nowPop[0][0]
        nowX = nowPop[0][1]
        nextDir = nowPop[1] #다음 이동 방향
        
        nextY = nowY + nextDir[0]
        nextX = nowX + nextDir[1]
        
        #다음 방문 위치가 이동 가능한 인덱스이며 아직 방문하지 않았다면
        if board[nextY][nextX] == 0:
            q.append([[nextY, nextX], nextDir])
        elif board[nextY][nextX] == 2: #다음 위치가 학생이라면
            findStudent = True #학생 발견 체크
            break
            
    for setIdx in p: #뽑힌 복도 공간에 장애물 제거
        board[setIdx[0]][setIdx[1]] = 0
        
    if findStudent == False: #끝까지 학생 찾지 못했다면
        break
    else: #학생 찾았다면 다른 장애물 위치 조합으로 시도
        continue

if findStudent == False: #모두 숨을 수 있다
    print('YES')
else: #어떠한 경우에도 모두 숨을 수 없다
    print('NO')
