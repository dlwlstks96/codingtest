def solution(q1, q2):
    answer = -2
    
    sum_q = sum(q1) + sum(q2)
    
    #모든 원소의 합이 홀수일 경우 -1 리턴
    if sum_q % 2 != 0:
        return -1
    
    half = sum_q // 2
    
    q = q1 + q2
    len_q = len(q)
    points = [0, len(q)//2] #q1의 포인터들 위치
    
    count = 0
    now_sum_q1 = sum(q[points[0]: points[1]])
    while True:
        if now_sum_q1 == half:
            return count
        
        if points[1] == len_q:
            points[1] = points[0]
            points[0] = 0
            now_sum_q1 = sum(q[points[0]: points[1]])
        
        if now_sum_q1 < half: #q1의 합이 절반보다 작을 경우
            now_sum_q1 += q[points[1]]
            points[1] += 1
        else: #q1의 합이 절반보다 클 경우
            now_sum_q1 -= q[points[0]]
            points[0] += 1
                
        count += 1
        
        if count == len_q**2:
            return -1
        
        
#q2 = [1, 2, 1, 2]
#q1 = [1, 10, 1, 2]
# [1, 2, 1, 2, 1, 10, 1, 2]

#q1 = [1, 2]
#q2 = [1, 4]

#q1 = [1, 1, 1, 1, 1]
#q2 = [1, 1, 1, 9, 1]

#q1 = [1 for _ in range(300000)]
#q2 = [1 for _ in range(299998)] + [599999, 1]
print(solution(q1, q2))

'''

모든 원소 합 30, 각 큐의 합 15로 만들어야 함
3, 2, 7, 2 / 14
4, 6, 5, 1 / 16

3, 2, 7, 2, 4 / 18
6, 5, 1 / 12

2, 7, 2, 4 / 15
6, 5, 1, 3 / 15

======

모든 원소 합 20, 각 큐 합 10으로 만들어야 함
1, 2, 1, 2 / 6
1, 10, 1, 2 / 14

1, 2, 1, 2, 1 / 7
10, 1, 2 / 13

1, 2, 1, 2, 1, 10 / 17
1, 2 / 3

2, 1, 2, 1, 10 / 16
1, 2, 1 / 4

1, 2, 1, 10 / 14
1, 2, 1, 2 / 6

2, 1, 10 / 13
1, 2, 1, 2, 1 / 7

1, 10 / 11
1, 2, 1, 2, 1, 2 / 9

10 / 10
1, 2, 1, 2, 1, 2, 1 / 10



3, 2, 7, 2, 4
6, 5, 1
'''
