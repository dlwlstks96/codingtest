# -*- coding: utf-8 -*-

#n = int(input())

#  n=2
# [10, 9, 8, ... 1] = 55

# n=3
# [(10+9+...1), (9+8..1), (1)] = 220

# n=4
# [(55+45...1), (45+36...1), (1)] = 

 
#   0  1  2  3  4  5  6  7  8  9
# 0 0  0  0  0  0  0  0  0  0  0
# 1 1  1  1  1  1  1  1  1  1  1 = 20
# 2 1  2  3  4  5  6  7  8  9  10 = 55
# 3 1  3  6  10 15 21 28 36 45 55 = 220
# 4 1  4  10

n = int(input())

l = [[0 for i in range(10)] for j in range(n+1)]

for i in range(10):
    l[1][i] = 1 #한자릿수 라인 1로 전부 세팅

for i in range(2, len(l)):
    l[i][0] = 1
    for j in range(1, len(l[i])):
        l[i][j] = sum(l[i-1][0:j+1]) #윗 라인 0~자신 인덱스까지의 합
        
print(sum(l[n])%10007)