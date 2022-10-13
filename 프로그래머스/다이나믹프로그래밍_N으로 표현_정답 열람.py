def solution(N, number):
    answer = -1
    
    dp = []
    
    for i in range(1, 9):
        all_case = set()
        init_number = int(str(N)*i)
        #{N}, {NN}, {NNN}..
        all_case.add(init_number)
        
        for j in range(0, i-1):
            #j개를 사용해서 만든 값들
            for op1 in dp[j]:
                for op2 in dp[-j-1]:
                    #print(j, -j-1)
                    all_case.add(op1 - op2)
                    all_case.add(op1 + op2)
                    all_case.add(op1 * op2)
                    if op2 != 0:
                        all_case.add(op1 // op2)
                    
        if number in all_case:
            answer = i
            break
        
        dp.append(all_case)
        
    return answer
  
  ''' 유용한 링크
  https://school.programmers.co.kr/questions/25218 
  '''
