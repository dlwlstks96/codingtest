import math
import sys

sys.setrecursionlimit(15000)

def prime(num): #소수 찾기
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0: #소수가 아니라면
            return -1
    
    return 1 #소수라면
        

def dfs(num, n): #백트래킹, dfs
    
    if len(str(num)) == n: #n 자릿수 소수라면
        print(num)
        return 1
    
    for i in range(10):
        tmp = int(str(num) + str(i))
        
        if prime(tmp) == -1: #소수가 아니라면
            continue
        else: #소수라면
            dfs(tmp, n)
            
n = int(input())

for i in range(2, 10):
    if prime(i) == 1:
        dfs(i, n)
