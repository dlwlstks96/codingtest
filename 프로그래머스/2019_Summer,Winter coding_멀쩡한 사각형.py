def solution(w,h):
    
    #전체 사각형
    total = w * h
    
    #최대 공약수 구하기
    common = -1
    for i in range(min(w, h), 0, -1):
        if w % i == 0 and h % i == 0:
            common = i
            break
    
    answer = total - (w + h - common)
    
    return answer
        


w = 8
h = 12

#w = 523
#h = 123

print(solution(w, h))
