class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        
        sort_nums = sorted(nums) #오름차순 정렬
        
        start = 0
        for idx in range(len(sort_nums)): #정렬된 배열과 처음으로 다른 인덱스 탐색
            if sort_nums[idx] != nums[idx]:
                start = idx
                break
            
        end = 0
        for idx in range(len(sort_nums)-1, -1, -1):
            if sort_nums[idx] != nums[idx]: #정렬된 배열과 처음으로 다른 인덱스를 뒤에서부터 탐색
                end = idx
                break
            
        if start == 0 and end == 0: #변동이 없을 시
            return 0
        else:
            return end - start + 1
