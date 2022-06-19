class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        
        answer = [nums[0]]
        for i in range(1, len(index)):
            nowIdx = index[i] #넣어야 할 위치
            if nowIdx == len(answer): #가장 끝에 넣는 경우
                answer.append(nums[i])
            else: #제일 앞 혹은 중간에 넣는 경우
                answer.insert(nowIdx, nums[i])
                
        return answer
