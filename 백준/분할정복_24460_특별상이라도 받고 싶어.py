# -*- coding: utf-8 -*-

# n = 4

# data = [
#         [15, 7, 13, 5],
#         [4, 2, 1, 9],
#         [0, 10, 8, 12], 
#         [3, 11, 14, 6]
#         ]

# n = 2
# data = [
#         [2, 0],
#         [3, 1]
#         ]

n = int(input())
data = [[] for i in range(n)]
for i in range(n):
    data[i] = list(map(int, input().split()))

def divide(data, x, y, n):
    if n > 2: #2x2 배열을 조사하는게 아닐 경우
        tmp = [] #결과를 담을 리스트, 아래에 한 변의 길이를 2등분해 4조각으로 나눠 재귀 실행
        tmp.append(divide(data, x, y, n//2))
        tmp.append(divide(data, x+n//2, y, n//2))
        tmp.append(divide(data, x, y+n//2, n//2))
        tmp.append(divide(data, x+n//2, y+n//2, n//2))
        tmp.sort()
        return tmp[1]
    elif n == 2: #2x2 배열을 조사하는 재귀 차례이면
        tmp = []
        for i in range(y, y+n):
            for j in range(x, x+n):
                tmp.append(data[i][j]) #4개의 원소들을 담아
        tmp.sort() #정렬 후 2번째로 작은 값 반환
        return tmp[1]
    
if n == 1:
    print(data[0][0])
else:    
    answer = divide(data, 0, 0, n)
    print(answer)
        