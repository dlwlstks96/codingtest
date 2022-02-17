# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

l = []

for i in range(n):
    name, kor, eng, math = input().split(' ')
    name = str(name)
    
    l.append([name, int(kor), int(eng), int(math)])
    
l.sort(key = lambda x: (-x[1], x[2], -x[3], x[0]))

for i in l:
    print(i[0])