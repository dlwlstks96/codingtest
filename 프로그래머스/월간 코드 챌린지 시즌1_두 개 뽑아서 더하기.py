def solution(numbers):
    answer = []
    
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            sumNum = numbers[i] + numbers[j]
            if sumNum not in answer:
                answer.append(sumNum)
            
    answer.sort()
    
    return answer
