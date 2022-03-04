# -*- coding: utf-8 -*-

k = int(input())

def move(N, start, to):
    global count, step
    count += 1
    step.append([start, to])
    #print(start, to)

def hanoi(N, start, to, via):
    if N == 1: #1개의 원반을 움직이게 되면 move 함수
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to) #제일 큰 원반 하나 빼고 이동
        move(N, start, to) #제일 큰 원반을 목표로 이동
        hanoi(N-1, via, to, start) #남은 원반들을 시작 지점으로 이동
        
count = 0 #몇번 이동하는지 카운트
step = []
hanoi(k, '1', '3', '2') #k개의 원반을 1에서 3으로, 2를 경유하여
print(count)
for i in step:
    print(i[0], i[1])
        

'''아래가 내 풀이

k = 3

# one = [i for i in range(1, k+1)]
# two = []
# three = []

top = [0, [i for i in range(k, 0, -1)], [], []]

stack = []
stack.append(top[1].pop())
for i in range(1, k+1):
    stack.append(i)

print(stack)
#while len(top[3]) != k:
    
'''