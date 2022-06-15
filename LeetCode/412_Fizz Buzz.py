# -*- coding: utf-8 -*-

class Solution(object):
    def fizzBuzz(self, n):
        answer = []
        for num in range(1, n+1):
            if num % 15 == 0:
                answer.append("FizzBuzz")
            elif num % 5 == 0:
                answer.append("Buzz")
            elif num % 3 == 0:
                answer.append("Fizz")
            else:
                answer.append(str(num))
                
        return answer
        
n = 3        

s = Solution()
s.fizzBuzz(n)