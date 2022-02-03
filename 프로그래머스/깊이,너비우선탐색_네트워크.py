# -*- coding: utf-8 -*-

def solution(n, computers):
    answer = 0
    
    com_list = [0 for i in range(n)] #컴퓨터 갯수만큼 0으로 리스트 초기화
    
    cnt = 0 #그룹의 갯수 초기화
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            #두 컴퓨터 연결되어 있고 대각선 idx가 아닐 경우(ex.[1,1]X)
            if computers[i][j] == 1 and i != j:
                #두 컴퓨터 모두 속해 있는 그룹이 없을 경우
                if com_list[i] == 0 and com_list[j] == 0:
                    cnt += 1 #그룹 추가 생성
                    com_list[i] = cnt
                    com_list[j] = cnt
                else: 
                    if com_list[i] != 0 and com_list[j] != 0: #두 컴퓨터 모두 다른 그룹에 속해 있을 경우
                        tmp = com_list[j]
                        for k in range(len(com_list)):
                            if com_list[k] == tmp:
                                com_list[k] = com_list[i]
                    elif com_list[i] != 0: #i만 다른 그룹에 속한 경우
                        com_list[j] = com_list[j]
                    elif com_list[j] != 0: #j만 다른 그룹에 속한 경우
                        com_list[i] = com_list[j]
                        
    answer += com_list.count(0) #0 갯수만큼 독립적인 네트워크
    
    com_list = set(com_list) #중복 제거
    com_list = list(com_list)
    
    if 0 in com_list: #아까 체크해준 0이 있다면
        answer += len(com_list) - 1
    else: #0이 없을 경우
        answer += len(com_list)
                        
    #print(com_list, answer)
    
    return answer

solution(4, [[1, 1, 0, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 0, 1, 1]])