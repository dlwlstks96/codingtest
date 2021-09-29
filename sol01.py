# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#1427

n = input()
arr = []

for i in range(len(n)):
    arr.append(int(n[i]))

arr.sort(reverse=True)

res = ""
for i in range(len(arr)):
    res += str(arr[i])
    
print(res)