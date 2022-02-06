# -*- coding: utf-8 -*-

# BBBBAAAAAB 10
# BBBBAAAABA 12
#위와 같이 뒤로 먼저 한 칸 갔다가 다시 앞에서부터 시작하는게 빠른 경우
#위에서 두번째 케이스 포함하기가 너무 어렵다

def solution(name):
    answer = 0
    
    # 방문 여부를 체크할 리스트
    check_list = [0 for i in range(len(name))]
    
    #A 위치는 0, 아닌 위치는 1
    for i in range(len(check_list)):
        if name[i] != 'A':
            check_list[i] = 1
    
    idx = 0
    r_idx = idx
    l_idx = idx
    cnt = 0
    
    while(sum(check_list)!=0): #리스트의 모든 요소가 0일때까지
        if check_list[idx] != 0: #현재 idx의 요소가 A가 아닐 경우
            up = abs(ord(name[idx]) - ord('A')) #A-B-C- 순
            down = abs(ord(name[idx]) - ord('Z')) + 1 #A-Z-Y-X- 순
            cnt += min(up, down) #두 조작 방식 비교
            check_list[idx] = 0 #방문 표시
            #print(up, down)
        
        r_idx = idx
        l_idx = idx
        
        while(r_idx < len(name)): #우로 이동
            if check_list[r_idx] != 0: #A아닌 알파벳 만날 경우
                break
            else:
                r_idx += 1
                
        while(l_idx >= -(len(name))): #좌로 이동
            if check_list[l_idx] != 0:
                break
            else:
                l_idx -= 1
                
        if sum(check_list) != 0:
            if abs(idx-r_idx) == abs(idx-l_idx) and 'A' in name: #좌우 거리 같을때
                tmp_r_idx = r_idx
                tmp_l_idx = l_idx
                while(tmp_r_idx < len(name) or tmp_l_idx >= -(len(name))):
                    tmp_r_idx += 1 #양옆으로 한칸씩 더 조사
                    tmp_l_idx -= 1
                    if check_list[tmp_r_idx] != 0 and check_list[tmp_l_idx] == 0: #그 다음 오른쪽만 A가 아닐 경우
                        cnt += abs(idx-l_idx)
                        idx = l_idx
                        break
                    elif check_list[tmp_l_idx] != 0 and check_list[tmp_r_idx] == 0: #그 다음 왼쪽만 A가 아닐 경우
                        cnt += abs(idx-r_idx)
                        idx = r_idx
                        break
            elif abs(idx-r_idx) < abs(idx-l_idx): #우로 이동이 더 가까울 경우
                cnt += abs(idx-r_idx)
                idx = r_idx
            else: #좌로 이동이 더 가까울 경우
                cnt += abs(idx-l_idx)
                idx = l_idx
            
        #print('cnt = ', cnt)
        
        #print('check_list = ', check_list, r_idx, l_idx)
        
        #break
        
    answer = cnt
        
    #print(answer)
    
    return answer

solution("BBBBAAAABA")