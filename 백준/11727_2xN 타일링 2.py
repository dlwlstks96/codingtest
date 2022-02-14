# -*- coding: utf-8 -*-

#백준_11727_2xN 타일링 2

# 1번 방법 -> 1x2로 채우기 -> 사실상 3-1 느낌
# 2번 방법 -> 2x1로 채우기
# 3번 방법 -> 2x2로 채우기

#f(n) = f(n-1) + 2f(n-2) -> 본 문제의 점화식

# def recursion(n): #재귀
    
#     if n > 2:
#         return recursion(n-1) + 2*recursion(n-2)
#     elif n == 2:
#         return 3
#     elif n == 1:
#         return 1

#print(recursion(n)%10007)

n = int(input())

answer = []

for i in range(n):
    if i == 0:
        answer.append(1)
    elif i == 1:
        answer.append(3)
    else:
        answer.append(answer[i-1]+2*answer[i-2])
        
print(answer[n-1]%10007)
    
'''

n = 1

- 2

answer = 1

n = 2

- 1
- 2,2
- 3

answer = 3

n = 3

- 1, 2
- 2, 2, 2
- 3, 2
- 2, 3
- 2, 1

answer = 5

n = 4

- 1, 1
- 1, 2, 2
- 1, 3
- 2, 1, 2
- 2, 3, 2
- 2, 2, 1
- 2, 2, 3
- 3, 1
- 3, 2, 2
- 3, 3

answer = 10

n = 8, answer = 171

'''