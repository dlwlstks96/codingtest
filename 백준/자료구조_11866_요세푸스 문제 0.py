# -*- coding: utf-8 -*-

n, k = map(int, input().split())

circle = [i for i in range(1, n+1)] * n * 10

clear = [] #제거된 사람들 저장
count = 0 #몇번째인지 체크
clear_count = 0 #제거 횟수 체크
for i in circle:
    if i in clear:
        continue
    count += 1
    if count == k:
        clear.append(i)
        clear_count += 1
        count = 0
    if clear_count == n:
        break

print('<', end = '')
for i in range(len(clear)):
    if i != len(clear)-1:
        print(clear[i], end = ', ')
    else:
        print(clear[i], end = '')
print('>')

# print('=========')

#print(len(clear))

# print(circle)