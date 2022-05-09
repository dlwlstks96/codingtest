# -*- coding: utf-8 -*-

size = int(input())

arr = list(map(int, input().split()))

dp = [0 for _ in range(size)]

dp[0] = arr[0]

for i in range(1, size): 
    now_num = arr[i] #기준 숫자
    max_num = 0
    check = False #dp 테이블 값을 한 번이라도 사용했는지
    for j in range(0, i): #앞에서부터 비교할 숫자
        if now_num > arr[j]:
            max_num = max(max_num, dp[j] + now_num)
            check = True #dp 테이블 값 한 번이라도 사용함
    
    if check == True:
        dp[i] = max_num
    else: #now_num 자체가 dp 테이블에 반영 되어야 함
        dp[i] = now_num
    
#print(dp)
print(max(dp))