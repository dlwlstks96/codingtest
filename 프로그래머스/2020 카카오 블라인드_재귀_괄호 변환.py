def dfs(p):
    
    #입력이 빈 문자열인 경우, 빈 문자열 반환
    if p == "":
        return ""
            
    left = 0 #왼쪽 방향으로 열린 괄호 ")"
    right = 0 #오른쪽 방향으로 열린 괄호 "("
    u = ""
    v = ""
    for idx, nowP in enumerate(p):
        if nowP == ")":
            left += 1
        elif nowP == "(":
            right += 1
        
        if left == right: #현재까지 인덱스가 균형 잡힌 괄호 문자열이라면
            u = p[0:idx+1]
            v = p[idx+1:]
            break
            
    # print(u, v)
    
    #u가 "균형 잡힌 괄호 문자열"인데 양 끝이 닫히지 않고 "올바른 괄호 문자열"일 순 없다.
    if u[0] != "(" or u[-1] != ")": #u가 올바른 괄호 문자열이 아니라면
        
        tmp = "(" + dfs(v) + ")"
        
        tmpU = "" #임시 u
        for nowU in u[1:len(u)-1]: #u의 첫 번째, 마지막 문자 제거하고 나머지 괄호 방향 뒤집기
            if nowU == ")":
                tmpU += "("
            elif nowU == "(":
                tmpU += ")"
        
        tmp += tmpU
        return tmp
    
    else: #u가 올바른 괄호 문자열이었다면
        tmpP = dfs(v)
        return u + tmpP

def solution(p):
    answer = ''
    
    answer = dfs(p)
            
    return answer
