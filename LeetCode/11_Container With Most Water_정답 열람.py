#투 포인터

class Solution:
    def maxArea(self, height: List[int]) -> int:       
        answer = 0
        con_L = 0 #왼쪽 슬라이드
        con_R = len(height) - 1 #오른쪽 슬라이드
        
        while con_L < con_R:
            answer = max(answer, min(height[con_L], height[con_R]) * (con_R - con_L)) #물 최대값 구하기
            
            #더 작은 쪽 슬라이드를 옮겨야 다음에 커질 가능성이 있다
            if height[con_L] <= height[con_R]: #왼쪽 슬라이드가 더 작으면
                con_L += 1 #왼쪽 슬라이드 +1 이동
            else:
                con_R -= 1 #오른쪽 슬라이드 -1 이동
                
        return answer
