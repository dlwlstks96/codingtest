# -*- coding: utf-8 -*-

def solution(msg):
    answer = []
    
    data = [0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    idx = 0 #알파벳 포인터
    #이전에 성공한 단어(-1인 이유는 msg가 한 글자라 while문을 아예 돌지 않을때
    #msg[0]을 출력하기 위함
    prevIdx = -1
    while msg:
        try:
            nowA = msg[idx]        
            nextA = msg[idx+1]
            combA = nowA + nextA #현재 알파벳 + 다음 알파벳
            while combA in data: #combA가 data에 있다면
                idx += 1
                combA += msg[idx+1] #다음 알파벳 추가
            
            printW = combA[0:len(combA)-1] #마지막 알파벳 제외
            addW = combA #사전에 추가해야할 알파벳
            
            #print(printW, addW, idx)
            
            prevIdx = idx #이전에 어디까지 성공했는지 저장하기 위함
            
            answer.append(data.index(printW)) #인덱스 저장
            data.append(addW) #사전에 추가
            
            idx += 1
        except: #인덱스 이탈하게 되면
            printW = msg[prevIdx+1:] #이전 성공 위치+1부터 msg 끝까지
            answer.append(data.index(printW))
            #print(idx, printW)
            break
        
    #print(answer)
        
    return answer
    
#solution('KAKAO')

