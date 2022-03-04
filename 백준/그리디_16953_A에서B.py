# -*- coding: utf-8 -*-


a,b = map(int,input().split())
r = 1
while(b!=a):
    r+=1
    temp = b
    if b%10 == 1: #b의 끝에 1이 있다면
        b//=10
    elif b%2 == 0: #b가 2로 나누어 떨어진다면
        b//=2
    
    if temp == b: #위 if문 어느것도 거치지 않았을때
        print(-1)
        break
else:
    print(r)




'''


import sys

a, b = map(int, sys.stdin.readline().split())
cnt = 1
while True:
    if b == a:
        break
    #b가 2로 나누어떨어지지 않는데 1의 자리가 1이 아닐 경우
    #혹은 b가 줄어들다 a보다 작아지는 경우
    elif (b % 2 != 0 and b % 10 != 1) or (b < a):
        cnt -= 1
        break
    else: 
        if b % 10 == 1: #b의 1의 자리가 1일 경우
            b //= 10
            cnt += 1
        else: #b가 2로 나누어질 경우
            b // 2
            cnt += 1
            
print(cnt)
'''


'''아래가 내 풀이


a, b = map(int, input().split())

data = []

cnt = b
while True:
    data.append(cnt)
    if cnt % 2 == 0:
        cnt = cnt//2
    else:
        break

print(data)

cnt = 0
num = a
while True:
    if num == b:
        print(cnt+1)
        break
    elif num > b:
        print(-1)
        break
    str_num = str(num) + '1'
    int_num = int(str_num)
    print(num, cnt, int_num)
    if int_num in data:
        num = int_num
    else:
        num *= 2
    cnt += 1
    
'''