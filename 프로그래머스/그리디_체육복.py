# -*- coding: utf-8 -*-

# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]

n = 5
lost = [1, 2, 3, 4]
reserve = [2, 4, 5]

def solution(n, lost, reserve):
    answer = 0
    
    lost.sort()
    reserve.sort()
    
    dic_lost = {}
    
    for i in lost:
        dic_lost[i] = 1 #잃어버린 상태
    
    for i in lost:
        if i in reserve: #잃어버린 사람이 본인 여벌이 있는 경우
            dic_lost[i] = 0
            reserve.remove(i)
    
    for i in lost:
        if i-1 in reserve: #i-1, i+1번째에서 빌려 받는 경우
            dic_lost[i] = 0
            reserve.remove(i-1)
        elif i+1 in reserve:
            dic_lost[i] = 0
            reserve.remove(i+1)
    
    cnt = 0
    
    for i in dic_lost.keys(): #여전히 value 값 1로 여벌 없는 경우
        if dic_lost[i] == 1:
            cnt += 1
            
    answer = n - cnt
    
    return answer

solution(n, lost, reserve)