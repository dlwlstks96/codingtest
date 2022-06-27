class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        answer = ""
        answer_list = ['_' for i in range(len(indices))]
        
        for count in range(len(indices)):
            answer_list[indices[count]] = s[count]
            
        for char in answer_list:
            answer += char
            
        return answer
            
