# -*- coding: utf-8 -*-

#프로그래머스_힙_이중우선순위큐

operations = ["I 7","I 5","I -5","D -1"]
#operations = ["I 16","D 1"]

def solution(operations):
    que = []
    
    for ele in operations:
        if ele[0] == 'I': #원소 삽입
            num = int(ele[2:])
            que.append(num)
        elif ele[0] == 'D': #원소 삭제
            if ele[2] == '1' and len(que) > 0: #최대값 삭제
                max_idx = que.index(max(que))
                que.pop(max_idx)
            elif ele[2] == '-' and len(que) > 0: #최소값 삭제
                min_idx = que.index(min(que))
                que.pop(min_idx)
                
    if len(que) == 0:
        answer = [0,0]
    elif len(que) > 1: #min, max를 쓸 땐 해당 리스트에 대한 길이를 확인해줘야함
        min_num = min(que)
        max_num = max(que)
        answer = [max_num, min_num]
    
    return answer

solution(operations)