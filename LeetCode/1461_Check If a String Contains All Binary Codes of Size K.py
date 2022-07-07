class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        max_k = (2**k) - 1 #길이가 k인 이진 코드의 최댓값
        
        #딕셔너리에 모든 이진 코드 저장
        binary_dic = {}
        for i in range(max_k, -1, -1):
            now_binary_code = "{0:b}".format(i).zfill(k)
            binary_dic[now_binary_code] = 1
        
        #문자열 s 순회하며 딕셔너리에 저장된 이진코드 체크
        count = 0
        for i in range(len(s) - k + 1):
            now_window = s[i:i+k]
            if binary_dic[now_window] == 1:
                binary_dic[now_window] = 0
                count += 1
            
            if count == 2**k:
                return True
            
        if count != 2**k:
            return False
