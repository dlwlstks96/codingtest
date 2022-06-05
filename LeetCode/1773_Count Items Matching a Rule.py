# -*- coding: utf-8 -*-

class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        answer = 0
        
        if ruleKey == "type":
            idx = 0
        elif ruleKey == "color":
            idx = 1
        elif ruleKey == "name":
            idx = 2
            
        for item in items:
            if item[idx] == ruleValue:
                answer += 1
              
        #print(answer)
        return answer
        
items = [["phone","blue","pixel"],["computer","silver","lenovo"],
         ["phone","gold","iphone"]]
ruleKey = "color"
ruleValue = "silver"

s = Solution()
s.countMatches(items, ruleKey, ruleValue)