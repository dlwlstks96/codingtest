# -*- coding: utf-8 -*-

class Solution(object):
    def isPalindrome(self, x):
        str_x = str(x)
        
        for idx in range(len(str_x)//2):
            if str_x[idx] != str_x[len(str_x)-1-idx]:
                return False
        
        return True
        
x = 121
s = Solution()
print(s.isPalindrome(x))