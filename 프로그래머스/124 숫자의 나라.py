def solution(n):
    
    answer = ''
    while n != 0:
        remainder = n % 3
        if remainder != 0:
            answer = str(remainder) + answer
            n = n // 3
        else:
            answer = '4' + answer
            n = (n // 3) - 1
            
    return answer
        
n = 10
print(solution(n))

'''
130(11211) -> 130/3 = 43 and 1
43/3 = 14 and 1
14/3 = 4 and 2
4/3 = 1 and 1
1/3 = 0 and 1

9(24) -> 9/3 = 3 and 0
2/3 = 0 and 2
=====> 100
144
24


40(1111) -> 40/3 = 13 and 1
13/3 = 4 and 1
4/3 = 1 and 1
1/1 = 0 and 1

17(122) -> 17/3 = 5 and 2
5/3 = 1 and 2
1/3 = 0 and 1

18(124) -> 18/3 = 6 and 0
5/3 = 1 and 2
1/3 = 0 and 1
=====> 200  244
124

6(14) -> 6/3 = 2 and 0
1/3 = 0 and 1
=====> 20
14
'''
