# -*- coding: utf-8 -*-

import sys

n = sys.stdin.readline()
n = int(n)
#n = 2

data = list(map(int, sys.stdin.readline().strip().split()))
#data = [1000, -1000000]
new_data = sorted(data) #원본 유지해야 입력 순서대로 결과 출력 가능

dic = {}
for i in new_data:
    dic[i] = 0 #카운트 담을 dic

#new_data.sort() #오름차순 정렬
#print(data) 

count = 0
prevNum = -1000000001
for i in new_data:
    if prevNum != i: #이전과 동일한 숫자가 아니라면 카운트 증가
        dic[i] = count
        prevNum = i
        count += 1
    
#print(dic)

for i in data:
    print(dic[i], end=' ')