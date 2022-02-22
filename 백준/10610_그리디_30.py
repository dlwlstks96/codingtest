# -*- coding: utf-8 -*-

n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print(''.join(n))

# # import sys

# # n = sys.stdin.readline().rstrip()

# # n = list(map(int, n))

# n = list(map(int, input()))


# if 0 not in n:
#     print(-1)
# else:
#     answer = ''
    
#     zero_count = n.count(0)
    
#     n.sort(reverse = True)
    
#     for i in range(zero_count):
#         n.pop()
    
#     while len(n) > 0:
#         if sum(n) % 3 == 0:
#             break
#         else:
#             n.pop()
            
#     if len(n) < 1:
#         print(-1)
#     else:
#         for i in range(len(n)):
#             answer += str(n[i])
#         answer = answer + ('0'*zero_count)
#         print(int(answer))