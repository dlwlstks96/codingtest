# -*- coding: utf-8 -*-

import itertools as it

a, b = map(int, input().split())

cnt = 0
def solve(n):
    global cnt
    print(n)
    if n>b:
        return 0
    if a<=n<=b:
        cnt+=1
    solve(n*10+4)
    solve(n*10+7)
solve(4)
solve(7)
print(cnt)