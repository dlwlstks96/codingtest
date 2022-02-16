# -*- coding: utf-8 -*-

#입국심사

def solution(n, times):
    answer = 0
    
    times.sort()
    
    start = 1 #최소 시간
    end = n*max(times) #최대 시간
    cnt = 0 #중간 시간 걸릴때 검사할 수 있는 사람의 수    
    while start <= end:
        mid = (start+end)//2 #걸린 시간(중간값, 기준)
        
        cnt = 0 #중간 시간 걸릴때 검사할 수 있는 사람의 수
        
        for t in times:
            cnt += (mid//t) #한 심사관이 검사한 사람의 수
            
        print(start, mid, end, cnt, answer)
            
        if cnt >= n: #만약 검사한 사람의 수가 n보다 많다면
            end = mid - 1 #검사 시간을 줄여본다
            answer = mid #그럼에도 방금까지의 걸린 시간이 정답일지 모르니 저장
        else: #검사한 사람의 수가 n보다 적다면, 정답이 절대 될 수 없으니
             start = mid + 1 #검사 시간을 늘려본다
    
    return answer
                   
               
print(solution(7, [7, 10]))

'''

6, [7, 10]

7, 10, 14, 20, 21, 28, 30, 35, 40, 42...

0 70 -> 35 36 70
36 70 -> 53 36 52
36 52 -> 44 -> success


n=3, 21 -> 3, 2
start = n -> 3+6 -> mid=4 -> 28 -> 4, 2
start = 4, end = 

5, [7, 10]

0 50 25 -> 3, 2
26 50 38 -> 5, 3
26 37 31 -> 4, 3
26 30 28 -> 4, 2
26 27 26 -> 3, 2
27 27 27 -> 3, 2
28 27 

'''