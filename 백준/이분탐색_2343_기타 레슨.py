# -*- coding: utf-8 -*-

'''
1 2 3 50 60 -> 12350 60
2개
-> 116 / 2 -> 58
0 116 -> 58+116 -> 174/2 -> 8
'''

# n, m = 9, 3
# data = [1, 2, 3, 4, 5, 6, 7, 8, 9]

n, m = map(int, input().split())
data = list(map(int, input().split()))

answer = 0
start = 0
end = sum(data)

while start <= end:
    mid = (start + end) // 2
    
    check = True
    tmp = []
    blue = mid
    res = []
    for i in range(len(data)):
        if data[i] > blue: #영상 하나가 용량 초과일 경우
            check = False
        if sum(tmp) + data[i] <= blue: #용량 초과 아니면
            tmp.append(data[i])
        elif sum(tmp) + data[i] > blue: #용량 초과일 경우
            res.append(tmp) #지금까지의 영상들 저장
            tmp = []
            tmp.append(data[i]) #새로운 블루레이에 넣기
    
    if len(tmp) != 0: #마지막 추가 못한 영상이 있다면
        res.append(tmp)
            
    #print(res, mid, blue)
    
    if data[-1] not in res[-1]:
        check = False
    
    if len(res) <= m and check == True: #성공했다면
        #print('success!')
        end = mid - 1 #용량 줄여보기
        answer = mid #정답일 수 있으니 우선 저장
    else: #그 외에 용량이 부족해서 용량 더 늘려야할 경우
        start = mid + 1
    #print(' ====== ')
        
print(answer)
    
    