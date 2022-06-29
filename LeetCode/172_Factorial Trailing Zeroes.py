class Solution:
    def trailingZeroes(self, n: int) -> int:
        sum_num = 1
        for num in range(1, n+1):
            sum_num *= num
            
        str_num = str(sum_num)
        list_num = list(str_num)
        count = 0
        for idx in range(len(list_num) - 1, -1, -1):
            if list_num[idx] == '0':
                count += 1
            else:
                break
                
        return count
