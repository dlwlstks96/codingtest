def solution(n, s):
    answer = []
    
    if n > s: #집합을 만들 수 없을 때
        return [-1]
    elif n == s: #집합의 모든 원소가 1이어야만 할 경우
        return [1] * n
    
    div = s // n #몫
    remain = s % n #나머지
    
    for _ in range(n): #몫을 n개 깔아준다
        answer.append(div)
        
    for idx in range(remain): #나머지를 균등하게 +1 해준다
        answer[idx] += 1
        
    #이래야 모든 원소들이 가장 균등한 상태를 가지게 된다
    
    answer.sort()
    
    return answer
