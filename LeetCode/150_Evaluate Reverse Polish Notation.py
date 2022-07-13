class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = []
        nums = [str(i) for i in range(-200, 201)] #문자열 형태의 숫자들
        
        for token in tokens:
            
            if token in nums: #token이 숫자라면
                stack.append(int(token))
            else:
                num1 = stack.pop()
                num2 = stack.pop()
                
                if token == "+":
                    stack.append(num2 + num1)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num2 * num1)
                else:
                    stack.append(int(num2 / num1))
        
        #마지막 남은 숫자 반환
        return stack[0]
