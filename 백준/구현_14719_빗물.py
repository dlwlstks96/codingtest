h, w = map(int, input().split())

blocks = list(map(int, input().split()))

board = [[0 for _ in range(w)] for _ in range(h)]

for x in range(len(board[0])):
    for y in range(len(board)-1, h-blocks[x]-1, -1):
        board[y][x] = 1

answer = 0
for y in range(len(board)):
    
    check = False #현재 닫혀 있는 상태라면
    
    count = 0 #한 층의 빗물 수 카운트
    for x in range(len(board[0])):
        
        if board[y][x] == 0 and check == True: #벽을 한 번이라도 만나고 현재 빗물이 고인다면
            count += 1
            continue
        
        if board[y][x] == 1 and check == True: #현재 열려 있는데 벽을 만나면
            answer += count #지금 층의 빗물을 총합에 더 해주고
            count = 0
            continue
        
        if board[y][x] == 1 and check == False: #벽 한 번이라도 만나면 열어 주기
            check = True
            continue
        
print(answer)

'''

ㅁ       ㅁ
ㅁ       ㅁ
ㅁ    ㅁ ㅁ
ㅁ ㅁ ㅁ ㅁ

'''
