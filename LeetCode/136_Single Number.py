# -*- coding: utf-8 -*-

from collections import Counter as ct

class Solution(object):
    def singleNumber(self, nums):        
        for num, count in ct(nums).items():
            if count == 1:
                return num
        
        
nums = [2, 2, 1, 1]
        
s = Solution()
s.singleNumber(nums)