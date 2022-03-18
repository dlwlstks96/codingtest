# -*- coding: utf-8 -*-

n = int(input())

# data = [
#         [0, 0, 0, 1, 1, 1, -1, -1, -1],
#         [0, 0, 0, 1, 1, 1, -1, -1, -1],
#         [0, 0, 0, 1, 1, 1, -1, -1, -1],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0],
#         [1, 1, 1, 0, 0, 0, 0, 0, 0],
#         [0, 1, -1, 0, 1, -1, 0, 1, -1],
#         [0, -1, 1, 0, 1, -1, 0, 1, -1],
#         [0, 1, -1, 1, 0, -1, 0, 1, -1]
#         ]

data = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    data.append(tmp)

answer = []
def devide(data, x, y, n):
    color = data[y][x]
    if n == 1:
        answer.append(color)
        return
    
    check = True
    for i in range(n):
        for j in range(n):
            if data[y+i][x+j] != color:
                check = False
                break
        if check == False:
            break
        
    if check == True:
        answer.append(color)
        return
    
    if check == False:
        devide(data, x, y, n//3)
        devide(data, x+n//3, y, n//3)
        devide(data, x+(n//3)*2, y, n//3)
        devide(data, x, y+n//3, n//3)
        devide(data, x+n//3, y+n//3, n//3)
        devide(data, x+(n//3)*2, y+n//3, n//3)
        devide(data, x, y+(n//3)*2, n//3)
        devide(data, x+n//3, y+(n//3)*2, n//3)
        devide(data, x+(n//3)*2, y+(n//3)*2, n//3)
            
devide(data, 0, 0, n)
print(answer.count(-1), answer.count(0), answer.count(1))