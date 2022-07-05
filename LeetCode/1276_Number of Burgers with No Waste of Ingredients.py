class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        
        if cheeseSlices > tomatoSlices // 2 or tomatoSlices % 2 != 0: #예외 처리
            return []
        elif cheeseSlices == 0 and tomatoSlices == 0:
            return [0, 0]
        elif cheeseSlices == 0 or tomatoSlices == 0:
            return []
        
        start = 0
        end = cheeseSlices
        
        print('===================')
        
        while start <= end:
            mid = (start + end) // 2
            jumbo = mid
            small = cheeseSlices - mid
            
            print(jumbo, small)
            
            nowValue = (4 * jumbo) + (2 * small)
            if nowValue == tomatoSlices:
                return [jumbo, small]
            
            if nowValue > tomatoSlices:
                end = mid - 1
            else:
                start = mid + 1
                
        return []
        
        
'''
        while small != 0:
            if (4 * jumbo) + (2 * small) == tomatoSlices: #조건 달성 시
                return [jumbo, small]
            
            jumbo += 1 #조건 미달성 시 jumbo 1개 증가
            small -= 1 #small 1개 감소
            
        return []
        
'''    
            
'''

[4, 0]
16 4

[2, 1]
10, 3 
0, 3 -> 1, 2 -> 2, 1 -> 3, 0

t: 3962, c: 1205
jumbo: 602, small:603 -> 3011


'''
