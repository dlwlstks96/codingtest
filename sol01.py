# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 16:56:54 2021

@author: s_dlwlstks96
"""    

#1436

n = int(input())

find = True #while문 제어하기 위한 boolean
num = 0 #0부터 시작하여 비교할 숫자를 계속 제공하기 위함
cnt = 0 #666이 들어간 숫자가 몇번째인지 카운트하기 위함

while(find):
    num = str(num)
    #666이 현재 비교 숫자에 들어가 있으면 카운트 1 증가
    if '666' in num:
        cnt += 1
    #카운트가 입력한 n의 값과 일치하면 while문 중단
    if cnt == n:
        find = False
    #일치하지 않으면 비교 숫자 1 증가
    else:
        num = int(num) + 1
        
print(num)

# 666
# 1666
# 2666
# 3666
# 4666
# 5666
# .
# .
# 9666
# 10666
# 11666
# 12666
# .
# .
# 19666
# 20666
# 21666
# .
# .
# 16661