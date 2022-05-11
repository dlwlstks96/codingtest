# -*- coding: utf-8 -*-

size = int(input())

# '*'로 꽉 채워진 그래프
graph = [['*' for i in range(size)] for j in range(size)]

draw = 1 #공백 크기
while draw != size:
    for i in range(draw, size, draw*3):
        for j in range(draw, size, draw*3):
            for k in range(draw):
                for l in range(draw):
                    graph[i+k][j+l] = ' '
    draw *= 3


for i in range(size):
    for j in range(size):
        print(graph[i][j], end = '')
    print('')

'''
1,1 / 1,4 / 1,7 / 1,10 ..
4,1 / 4,4 / 4, 7 ..

3,3~3,5 / 3,12

'''
