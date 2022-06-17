# -*- coding: utf-8 -*-
class Solution(object):
    def numberOfSteps(self, num):
        answer = 0
        while num != 0:
            answer += 1
            if num % 2 == 0:
                num = num // 2
            else:
                num -= 1
                
        return answer
    
    
num = 16
s = Solution()
s.numberOfSteps(num)