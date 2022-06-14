# -*- coding: utf-8 -*-

class Solution(object):
    def containsDuplicate(self, nums):
        
        set_nums = set(nums) #중복 제거
        if len(set_nums) != len(nums):
            return True
        else:
            return False
        
        
nums = [1, 2, 3, 1]        

s = Solution()
s.containsDuplicate(nums)