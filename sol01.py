# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#11650

import sys

#stdin.readline은 한번에 읽어와 버퍼에 저장하기에
#하나씩 입력할 때마다 데이터를 버퍼에 보관하는 input()보다
#처리 속도가 빠르다
n = int(sys.stdin.readline())

arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([x, y])
    
s_arr = sorted(arr)

for i in range(n):
    print(s_arr[i][0], s_arr[i][1])