# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#11726

s = [0,1,2]

for i in range(3, 1001):
    s.append(s[i-2] + s[i-1]) #n의 방법의 수는 n-2 + n-1
    
n = int(input())

print(s[n] % 10007) #n의 방법의 수를 리스트에서 골라 10007로 나누기