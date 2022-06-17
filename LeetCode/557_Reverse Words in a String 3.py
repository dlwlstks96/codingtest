# -*- coding: utf-8 -*-

class Solution(object):
    def reverseWords(self, s):
        answer = ""
        s = s.split(' ')
        for word in s:
            for idx in range(len(word)-1, -1, -1):
                answer += word[idx]
            answer += ' '
            
        #print(answer)
        return answer[:len(answer)-2]
        
s = "God Ding"       
c = Solution()
c.reverseWords(s)