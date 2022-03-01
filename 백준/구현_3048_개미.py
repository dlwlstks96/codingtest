# -*- coding: utf-8 -*-

# len_n1, len_n2 = 3, 4
# n1 = ['J', 'L', 'A'] #C B A
# n2 = ['C', 'R', 'U', 'O']
# t = 3

len_n1, len_n2 = map(int, input().split())
tmp = str(input())
n1 = []
for n in tmp:
   n1.append(n)
   
tmp = str(input())
n2 = []
for n in tmp:
    n2.append(n)
    
t = int(input())

ant = {}
for i in range(len(n1)): #1번 그룹
    ant[n1[i]] = 1
    
for i in range(len(n2)): #2번 그룹
    ant[n2[i]] = 2

road = [] #개미들이 올라갈 길
n1.reverse() #n1 역순
road += n1
road += n2

#print(ant)

sum_ant = len(n1)+len(n2)
time = 0
while time < t:
    #몇번 개미들 움직였는지 체크
    moveCheck = [0 for i in range(sum_ant)]
    
    for i in range(sum_ant-1):
        #앞 개미가 1번 그룹이고 뒷 개미가 2번 그룹일 경우, 그리고 앞 개미가 움직인적 없다면
        if ant[road[i]] == 1 and ant[road[i+1]] == 2 and moveCheck[i] == 0:
            tmp = road[i]
            road[i] = road[i+1]
            road[i+1] = tmp #둘의 위치 바꾸기
            moveCheck[i] = 1
            moveCheck[i+1] = 1 #둘 다 움직인 것으로 표시
    
    #print(road)
    time += 1 #1초 증가
    
for i in road:
    print(i, end = '')