class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        min_len = 99999999
        for i in strs:
            min_len = min(min_len, len(i))
        
        
        answer = ""
        idx = 0
        while True:
            if idx >= min_len:
                break
                
            now_tmp = strs[0][idx]
            check = True
            
            for word in strs:
                if word[idx] != now_tmp:
                    check = False
                    break
                    
            idx += 1
            
            if check == True:
                answer += now_tmp
            else:
                break
            
        return answer
            
            
                