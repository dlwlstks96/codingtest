class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return nums.index(max(nums))
        
        left = 0 #왼
        right = len(nums) - 1 #오
        
        answer = 0
        while left < right:
            mid = (left + right) // 2 #중앙값
            
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]: #peak 값
                return mid
            
            if nums[mid + 1] > nums[mid - 1]: #오른쪽 값이 더 크다면
                answer = right
                left = mid + 1
            else: #왼쪽 값이 더 크다면
                answer = left
                right = mid - 1
                
        return answer
