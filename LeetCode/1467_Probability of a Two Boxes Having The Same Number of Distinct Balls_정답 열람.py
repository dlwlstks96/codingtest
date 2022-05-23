# -*- coding: utf-8 -*-

class Solution:
    def getProbability(self, balls: List[int]) -> float:
        N = len(balls)
        sumBalls = sum(balls)
 
        @lru_cache(None)
        def count(index, delta, ca):
            if index == N:
                if delta == 0 and ca * 2 == sumBalls:
                    return 1
                return 0
 
            total = 0
            for x in range(1, balls[index]):
                total += count(index+1, delta, ca+x) * math.comb(balls[index], x)
            total += count(index+1, delta+1, ca)
            total += count(index+1, delta-1, ca+balls[index])
            return total
 
        return count(0, 0, 0) / math.comb(sumBalls, sumBalls // 2)
          
        
#balls = [1,2,1,2]
#balls = [2, 1, 1]
balls = [6,6,6,6,6,6]
s = Solution()
s.getProbability(balls)
        


'''
k개의 고유한 색상의 2n개의 공이 주어집니다. 
당신은 크기가 k인 정수 배열 볼이 주어질 것입니다. 
여기서 볼[i]은 색상이 i인 볼의 수입니다.

모든 공은 무작위로 균일하게 섞인 다음 처음 n개의 공을 첫 번째 상자에 분배하고 
나머지 n개의 공을 다른 상자에 분배합니다(두 번째 예의 설명을 주의 깊게 읽으십시오).

두 상자는 다른 것으로 간주됩니다. 
예를 들어, 두 개의 색상 공과 [] 및 () 상자가 있는 경우 분포 [a](b)는 
분포 [b](a)와 다른 것으로 간주됩니다. 첫 번째 예는 신중하게).

두 상자에 동일한 수의 고유한 공이 있을 확률을 반환합니다. 
실제 값의 10-5 이내의 답변이 올바른 것으로 인정됩니다.
'''

'''
        answer = 0
        
        balls_list = []
        
        #balls 리스트 정보 이용해 실제 공 정보 저장
        for balls_idx in range(len(balls)):
            for ball_count in range(balls[balls_idx]):
                balls_list.append(balls_idx+1)
        
        #모든 경우의 수 뽑기
        picks = it.permutations(balls_list, len(balls_list))
        total_count = 0 #전체 경우의 수 카운트
        answer_count = 0 #조건을 만족하는 경우의 수 카운트
        
        check_double = []
        
        for p in picks:
            #이미 뽑은적 있는지 중복 체크
            if p in check_double:
                continue
            
            #뽑은적 없다면 check list에 저장
            check_double.append(p)
            
            total_count += 1
            tmp_list_A = p[0:len(p)//2] #반으로 나누기
            tmp_list_B = p[len(p)//2:]
            
            #중복 제거
            set_list_A = set(tmp_list_A)
            set_list_B = set(tmp_list_B)
            
            #각 상자에 동일한 갯수의 고유 색깔이 있다면
            if len(set_list_A) == len(set_list_B):
                answer_count += 1
            
        answer = answer_count / total_count
        answer = round(answer, 5)
        
        print(answer)
        
        return answer
'''