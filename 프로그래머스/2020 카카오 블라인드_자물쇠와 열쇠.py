# -*- coding: utf-8 -*-

def check(new_lock):
    lock_length = len(new_lock) // 3
    for i in range(lock_length, lock_length*2):
        for j in range(lock_length, lock_length*2):
            if new_lock[i][j] != 1:
                return False  
    return True
                
                
def solution(key, lock):  
    length_key = len(key) #열쇠 한 변의 길이
    
    length_lock = len(lock) #자물쇠 한 변의 길이
    
    key_list = [] #네 방향으로 돌린 열쇠 저장소
    key_list.append(key) #첫 번째 열쇠
    
    for a in range(3): #3번 돌려야 하므로
        new_key = [[] for i in range(length_key)] #임시로 새로운 키 정보 담을 이차원 리스트
        for i in range(length_key):
            tmp_list = [] #키의 한줄씩 담을 리스트
            for j in range(length_key-1, -1, -1):
                tmp_list.append(key_list[a][j][i]) #2,0 1,0 0,0
                #print(tmp_list)
                new_key[i] = tmp_list #새로운 키
        key_list.append(new_key)
        
    #print(key_list) #네 방향으로 돌린 열쇠 모두 획득
    
    length_new_lock = length_lock*3 #자물쇠 올릴 판의 한 변의 길이
    
    new_lock = [[0 for i in range(length_new_lock)] for j in range(length_new_lock)]
    
    x, y = 0, 0
    for i in range(length_lock):
        for j in range(length_lock):
            #print(i, j)
            new_lock[i+length_lock][j+length_lock] = lock[x][y]
            y += 1
        x += 1
        y = 0
        
    #print(new_lock) #새로운 자물쇠 획득 (한 변의 길이 = 기존 자물쇠 한 변의 길이 * 3)
    
    for rotation in range(4):
        key = key_list[rotation]
        #print(key)
        #tmp_lock = new_lock
        for x in range(length_lock*2):
            for y in range(length_lock*2):
                #자물쇠에 열쇠 끼워 넣기
                for i in range(length_key):
                    for j in range(length_key):
                        new_lock[x+i][y+j] += key[i][j]
                #print(new_lock)
                #새로운 자물쇠가 열쇠에 잘 들어갔는지 검사
                if check(new_lock) == True:
                    return True
                for i in range(length_key):
                    for j in range(length_key):
                        new_lock[x+i][y+j] -= key[i][j]
    return False

solution([[0, 0, 0, 0], [1, 0, 0, 0], [0, 1, 1, 1], [1, 1, 0, 0]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]])

'''
<key>
000  010  110  001
100  100  001  001
011  100  000  010

<lock>
111
110
101

000000000
000000000
000000000
000111000
000110000
000101000
000000000
000000000
000000000


'''