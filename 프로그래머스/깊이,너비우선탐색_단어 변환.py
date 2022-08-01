from collections import deque as dq

def diffOneWord(w1, w2): #한 글자 차이인지 확인하는 함수
    count = 0
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            count += 1
        if count == 2: #두 글자 이상 차이날 경우
            return False
    
    if count == 1: #두 단어가 한 글자만 다른 경우
        return True
    else: 
        return False
        
        
def solution(begin, target, words):
   
    if target not in words: #target으로 변환 불가한 경우
        return 0
    
    q = dq([])
    count = 0 #단계를 카운트
    q.append([begin, count])
    visit = [0 for _ in range(len(words))] #word 방문 처리
    
    while q:
        nowPop = q.popleft()
        nowWord = nowPop[0]
        nowCount = nowPop[1]
        
        if nowWord == target:
            return nowCount
        
        for i in range(len(words)):
            nextWord = words[i]
            if diffOneWord(nowWord, nextWord) == True: #두 단어가 한 글자 차이라면
                q.append([nextWord, nowCount + 1])
                visit[i] = 1
