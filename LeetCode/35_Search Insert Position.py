# -*- coding: utf-8 -*-

class Solution(object):
    def searchInsert(self, nums, target):
        answer = len(nums)
        
        for idx in range(len(nums)-1):
            if nums[idx] <= target and nums[idx+1] >= target:
                answer = idx + 1
                break
                
        print(answer)
        return answer
        
        
        
nums = [1, 3, 5, 6]
target = 0

#nums = [0, 1, 2, 2, 3, 0, 4, 2]
#val = 2

s = Solution()
s.searchInsert(nums, target)