# -*- coding: utf-8 -*-

#n, l = 9, 4
#board = [
#        [4, 4, 3, 3, 3, 3, 2, 2, 2],
#        [4, 4, 3, 3, 1, 1, 2, 2, 3], 
#        [3, 3, 2, 2, 1, 1, 1, 1, 2], 
#        [1, 1, 1, 1, 1, 1, 1, 1, 1], 
#        [1, 1, 1, 1, 1, 1, 1, 1, 1 ],
#        [2, 2, 1, 1, 1, 1, 1, 1, 1 ],
#        [2, 2, 1, 1, 1, 1, 1, 1, 1 ],
#        [2, 2, 2, 2, 2, 2, 1, 1, 1 ],
#        [3, 3, 3, 3, 2, 2, 2, 2,1],
#       ]


n, l = map(int, input().strip().split())

board = [[] for i in range(n)]

for i in range(n):
    data = list(map(int, input().strip().split()))
    board[i] = data

#print(board)
roadList = board[0:n] #모든 길 후보
for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(board[j][i])
    roadList.append(tmp) #가로 세로 방향의 모든 길
#print(roadList)
    
'''    
prev = 1
print([prev]*2)
print(roadList[0][2:0:-1])
'''
answer = 0

for road in roadList:
    prev = road[0] #첫번째 지점 넣기
    check = [0] * n #경사로 놓는 지점 체크
    count = 1
    #print(road)
    for i in range(1, len(road)):
        if abs(road[i] - prev) > 1: #높이 차이가 1보다 클 경우
            break
        elif road[i] > prev: #다음 진행 방향이 더 높을 경우
            try: #지나온 길에 경사로를 놓을 수 없다면, 혹은 지나온 길에 이미 경사로가 놓여 있다면
                if road[i-l:i] != [prev]*l or 1 in check[i-l:i]:
                    break
                check[i-l:i] = [1]*l
            except: #인덱스 벗어나는 것도 조건 미달성
                break
        elif road[i] < prev: #다음 진행 방향이 더 낮을 경우
            try: #지나갈 길에 경사로를 놓을 수 없다면, 혹은 지나갈 길에 이미 경사로가 놓여 있다면
                if road[i:i+l] != [road[i]]*l or 1 in check[i:i+l]:
                    break
                check[i:i+l] = [1]*l
            except: #인덱스 벗어나는 것도 조건 미달성
                break
        prev = road[i]
        count += 1 #break를 모두 통과했다면
    #print(count, 'check = ', check)
    if count == n:
        answer += 1 #for문을 성공적으로 돌았을 경우
    
print(answer)
                    