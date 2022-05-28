# -*- coding: utf-8 -*-

from collections import deque as dq
import copy

class Solution(object):
    def check(self, nums):
        if len(nums) == 1:
            return True

        new_nums = copy.deepcopy(nums)
        new_nums = dq(new_nums)
        
        nums.sort()
        
        
        for _ in range(len(new_nums)):
            new_nums.rotate()
            if list(new_nums) == nums:
                print(new_nums, nums)
                print('True')
                return True
            
        return False
        
#nums = [3, 4, 5, 1, 2]
nums = [2, 1, 3, 4]
s = Solution()
s.check(nums)