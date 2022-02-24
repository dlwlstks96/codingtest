# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline())

l = []

for i in range(n):
    x, y = map(int, sys.stdin.readline().split(' '))
    l.append([x, y])

l.sort(key = lambda x: (x[1], x[0]))

for i in l:
    for j in i:
        print(j, end=(' '))
    print()