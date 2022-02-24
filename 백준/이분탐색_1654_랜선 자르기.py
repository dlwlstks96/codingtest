# -*- coding: utf-8 -*-

import sys

k, n = input().split(' ')

k = int(k)
n = int(n)

l = []

for i in range(k):
    tmp = int(sys.stdin.readline())
    #tmp = int(input())
    l.append(tmp) #각각의 랜선 길이 리스트에 저장
    
start = 1 #시작
end = max(l) #종료

while start <= end:
    mid = (start + end) // 2 #중간 지점
    lines = 0 #자른 랜선의 총 갯수
    for i in l:
        lines += i // mid
        
    #print('start = ', start,',end = ',  end,',mid = ',  mid,',lines = ',  lines)
        
    if lines >= n: 
        start = mid + 1 #start = mid 아닌 +1이 핵심
    else:
        end = mid - 1 #end = mid가 아닌 -1이 핵심
        
#모든 범위의 수를 탐색하기 위해선 start 혹은 end값을 세팅할때 mid 값에 +1 or -1을 해주는 것이 핵심

print(end)