# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#2750

n = int(input())
res = []

for i in range(n):
    k = int(input())
    res.append(k)
    
res.sort()

for i in range(n):
    print(res[i])