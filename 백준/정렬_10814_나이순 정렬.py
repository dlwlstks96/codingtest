# -*- coding: utf-8 -*-

n = int(input())

l = []

for i in range(n):
    age, name = input().split(' ')
    age = int(age)
    name = str(name)
    l.append([age, name])
    
l.sort(key =  lambda x: x[0])

for i in l:
    print(i[0], i[1])