# -*- coding: utf-8 -*-

class Solution(object):
    def minElements(self, nums, limit, goal):
        
        sum_nums = sum(nums) #nums 배열의 초기 총합
        
        if sum_nums == goal:
            return 0
        
        #초기 총합에서 goal까지의 거리
        dist_goal = abs(sum_nums - goal)
        
        tmp = dist_goal % limit
        if tmp == 0: #나머지가 없을 경우
            answer = (dist_goal//limit)
        else: #나머지가 있을 경우 한 번 더 count 해야 함
            answer = (dist_goal//limit) + 1
        
        #print(answer)
        
        return answer
        
#nums = [1, -1, 1]
#nums = [1, -10, 9, 1]
nums = [-1, 0, 1, 1, 1]
limit = 1
goal = 6
s = Solution()
s.minElements(nums, limit, goal)