class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        
        if len(nums) == 1: #예외 처리
            return nums
        
        nums_sort = sorted(nums) #정렬한 nums 리스트 새로 반환
        if len(nums) % 2 == 0: #길이가 짝수
            mid_val = len(nums)//2
        else: #길이가 홀수
            mid_val = len(nums)//2 + 1
            
        nums_left = nums_sort[0:mid_val] #작은 숫자들 왼쪽 리스트에 저장
        nums_right = nums_sort[mid_val:len(nums)] #큰 숫자들 오른쪽 리스트에 저장
        
        #print(nums_left, nums_right)
        
        count_idx = 0 #left, right 리스트 인덱스
        
        if max(nums_left) == min(nums_right): #nums 리스트의 중앙값이 겹친다면 left, right 내림차순으로 변경
            nums_left.sort(reverse = True)
            nums_right.sort(reverse = True)
        
        #nums 리스트에 접근하여 두 개 단위로 left, right 리스트의 값들로 치환
        for i in range(0, len(nums), 2):
            
            if count_idx < len(nums_left):
                nums[i] = nums_left[count_idx]
            if count_idx < len(nums_right):
                nums[i+1] = nums_right[count_idx]
            
            count_idx += 1
        
        #print(nums)
        
        return nums
