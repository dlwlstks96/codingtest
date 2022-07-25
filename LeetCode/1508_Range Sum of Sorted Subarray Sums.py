class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        arr = []
        for leftIdx in range(n):
            for rightIdx in range(leftIdx + 1, n + 1):
                #print(leftIdx, rightIdx)
                arr.append(sum(nums[leftIdx:rightIdx]))
                
        arr.sort()
                
        #print(max(arr))
        
        return (sum(arr[left-1: right]) % (10**9+7))
