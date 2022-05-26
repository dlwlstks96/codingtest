# -*- coding: utf-8 -*-

class Solution(object):
    def longestConsecutive(self, nums):
       if len(nums) == 0:
           return 0
        
       nums.sort()
       
       count = 1
       max_count = 0
       for idx in range(len(nums)-1):
           if (nums[idx] + 1) == nums[idx+1]:
               count += 1
           elif nums[idx] == nums[idx+1]:
               continue
           else:
               max_count = max(max_count, count)
               count = 1
       
       max_count = max(max_count, count)
        
       #print(max_count)
       return max_count

#nums = [0]
nums = [0,3,7,2,5,8,4,6,0,1]
#nums = [100,4,200,1,3,2]
#nums = [1, 2, 0, 1]
#nums = []
s = Solution()
s.longestConsecutive(nums)