# -*- coding: utf-8 -*-

class Solution:
     def maxRotateFunction(self, nums): #[4, 3, 2, 6]
        sum_nums = sum(nums)
        len_nums = len(nums)
        
        answer = 0
        for i in range(1, len_nums): #F(0)일 때
            answer += i * nums[i]
            
        cur = answer #직전 답 저장
        for idx in range(len(nums)):
            # F(n) = F(n-1) - sum(nums) + (len(nums)*nums[n-1])
            cur = cur - sum_nums + (len_nums * nums[idx])
            answer = max(answer, cur)
            
        return answer
        
        
        
nums = [4, 3, 2, 6]
s = Solution()
print(s.maxRotateFunction(nums))

'''
F(0) = 0*a0 + 1*a1 + 2*a2 + 3*a3
F(1) = 0*a1 + 1*a2 + 2*a3 + 3*a0..

F(1) - F(0) = -1*a1 -1*a2 -1*a3 + 3*a0
            = -(a1 + a2+ a3+ a0) + 4*a0
            
F(1) = F(0) - (a1 + a2 + a3 + a0) + 4*a0

F(n) = F(n-1) - (sum(nums)) + (len(nums) * nums[n-1])
'''
