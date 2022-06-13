# -*- coding: utf-8 -*-

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a = int(a, 2) # 10진수로 변환
        b = int(b, 2)
        a = a + b
        del b
        return bin(a)[2:] # 2진수로 변환('0b'가 앞에 무조건 붙음)