# -*- coding: utf-8 -*

# # c1 = [1,0,1,0,1,1,1,1] # 2, 6번 인덱스가 맞닿음
# # c2 = [0,1,1,1,1,1,0,1]
# # c3 = [1,1,0,0,1,1,1,0]
# # c4 = [0,0,0,0,0,0,1,0]

# c = [0, [1,0,1,0,1,1,1,1], [0,1,1,1,1,1,0,1], [1,1,0,0,1,1,1,0], [0,0,0,0,0,0,1,0]]

# c[1] = dq(c[1])
# c[2] = dq(c[2])
# c[3] = dq(c[3])
# c[4] = dq(c[4])
# #print(c)
# k = 2

from collections import deque as dq

c = [0]
for i in range(4):
    tmp = str(input())
    tmp2 = []
    tmp2 = dq(tmp2)
    for j in tmp:
        tmp2.append(int(j))
    c.append(tmp2)
    
k = int(input())

for i in range(k):
    cNum, direction = map(int, input().split())
    sideNum = [None] #현재 맞물려있는 바퀴들의 상태
    
    for j in range(1, 5): #현재 맞물려있는 바퀴들의 상태
        sideNum.append(c[j][6])
        sideNum.append(c[j][2])
    #print('sideNum = ', sideNum)
    #break
    
    c[cNum].rotate(direction) #본인 먼저 돌리기
    
    check = [0] * 5
    leftIdx = cNum
    leftDir = direction
    rightIdx = cNum
    rightDir = direction
    while leftIdx > 1: #왼쪽 방향들 탐색
        #왼쪽 바퀴와 인접한 극이 다르다면
        if sideNum[(2*leftIdx)-1] != sideNum[(2*(leftIdx-1))]:
            c[leftIdx-1].rotate(-leftDir)
        else: #왼쪽 바퀴가 돌지 않는다면 이후론 안돌림
            break
        leftIdx -= 1
        leftDir = -leftDir
        
    while rightIdx < 4: #오른쪽 방향들 탐색
        #오른쪽 바퀴와 인접한 극이 다르다면
        if sideNum[(2*rightIdx)] != sideNum[(2*rightIdx)+1]:
            c[rightIdx+1].rotate(-rightDir)
        else: #오른쪽 바퀴 돌지 않으면 이후론 안돌림
            break
        rightIdx += 1
        rightDir = -rightDir
        
    #print('nowC = ', c)
    
point = 1
answer = 0
for i in range(1, 5):
    if c[i][0] == 1:
        answer += point
    point *= 2
    
print(answer)