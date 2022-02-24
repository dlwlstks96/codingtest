# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

l = []

for i in range(n):
    tmp = int(sys.stdin.readline())
    l.append(tmp)
    
l.sort()

for k in l:
    print(k)