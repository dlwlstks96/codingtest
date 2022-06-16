# -*- coding: utf-8 -*-

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        jewels = list(jewels)
        stones = list(stones)
        
        answer = 0
        for j in jewels:
            for s in stones:
                if j == s:
                    answer += 1
                    
        return answer
                
    
jewels = "aA"
stones = "aAAbbbb"
s = Solution()
s.numJewelsInStones(jewels, stones)