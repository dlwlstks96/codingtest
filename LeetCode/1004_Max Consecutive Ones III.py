class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        #투포인터
        start = 0
        end = 0
        count = 0 #포인터 내부에 0의 갯수 카운트
        one_count = 0 #start에서 end 까지 0 -> 1로 치환하고 내부 1의 총 갯수
        
        if len(nums) == 1: #길이가 1일때의 예외 처리
            if nums[0] == 0 and k == 0:
                return 0
            else:
                return 1
        
        if nums[start] == 0: #시작점이 0인지
            count += 1
        
        while end < len(nums): #end가 마지막 인덱스 도달할 때까지
            
            # print('s = ', start,'e = ',  end,'c = ',  count,'oc = ',  one_count)
            # print(nums[start:end+1])
            # print('========================')
            
            try: #인덱스 넘어가는 것 방지  
                if count <= k: #end가 더 나아가도 될 때
                    end += 1 #더 나아가고
                    if nums[end] == 0: #0인지 판단
                        count += 1
                        
                else: #count > k로 start가 나아가야 할 때
                    if nums[start] == 0: #0인지 먼저 판단하고
                        count -= 1
                    start += 1 #나아가기
                
                if count <= k:
                    one_count = max(one_count, end - start + 1)
                    
            except:
               break
            
        return one_count
