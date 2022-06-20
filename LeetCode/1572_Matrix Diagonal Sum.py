class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        if len(mat) == 1 and len(mat[0]) == 1: #하나의 요소만 담겨 있을 때
            return mat[0][0]
        
        answer = 0
        upDown = 0
        leftRight = 0
        rightLeft = len(mat[0]) - 1
        while upDown < len(mat):
            answer += mat[upDown][leftRight]
            answer += mat[upDown][rightLeft]
            
            upDown += 1
            leftRight += 1
            rightLeft -= 1
            
        if len(mat) % 2 != 0: #한 변의 길이가 홀수일 때, 중앙값을 두 번 합하므로
            answer -= mat[len(mat)//2][len(mat)//2]
            
        return answer
