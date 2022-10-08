from collections import deque as dq

n = int(input())

l = [] #음수
r = [] #양수
zero = -1

for _ in range(n):
    tmp = int(input())
    
    if tmp < 0: #음수라면
        l.append(tmp)
    elif tmp > 0: #양수라면
        r.append(tmp)
    else: #0이 입력으로 들어 온다면
        zero = 1
        
l.sort()
r.sort()

l = dq(l)
            
answer = []

while l:
    if len(l) > 1: #음수가 아직 2개 이상 남아 있다면
        tmp1 = l.popleft()
        tmp2 = l.popleft()
        answer.append(tmp1*tmp2)
    else: #음수가 하나 남아 있다면
        if zero == 1: #입력으로 0이 하나 들어 왔다면
            l.popleft()
            continue #음수 하나를 0 곱해 0으로 만듬
        else: #입력으로 0이 없다면
            answer.append(l.popleft())
        
while r:
    if len(r) > 1: #양수가 아직 2개 이상 남아 있다면
        tmp1 = r.pop()
        tmp2 = r.pop()
        if tmp1 == 1 or tmp2 == 1: #두 숫자 중 1이 하나라도 있다면
            answer.append(tmp1)
            answer.append(tmp2)
        else:
            answer.append(tmp1*tmp2)
    else: #양수가 하나 남아 있다면
        answer.append(r.pop())
        
print(sum(answer))
    
    
# print(arr)

'''

-1000 ~ -1

0

1 ~ 1000

'''
