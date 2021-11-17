# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#10992

n = int(input())

for i in range(n):
    if i == 0:
        print(" "*(n-1)+"*")
    elif i == n-1:
        print("*"*(2*n-1))
    else:
        print(" "*(n-1-i)+"*"+" "*(2*i-1)+"*")