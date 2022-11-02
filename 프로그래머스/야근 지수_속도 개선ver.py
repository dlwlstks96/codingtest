from collections import Counter

def solution(n, works):
    
    #Counter 이용하여 원소가 몇 개씩 존재하는지 확인 -> dic으로 반환 -> 정렬까지
    work_remain_list = sorted(Counter(works).items())
    
    work_remain_list = [list(ele) for ele in work_remain_list]

    while n > 0 :
        
        time, amount = work_remain_list.pop() #가장 큰 work 꺼내기
        
        if n >= amount : #가장 큰 work의 갯수만큼 한 번에 처리할 수 있다면
            
            #빈 배열 아니고 그 다음 큰 work와 작업량이 1 차이 난다면
            if work_remain_list and work_remain_list[-1][0] == time -1:
                work_remain_list[-1][1] += amount #가장 큰 work 갯수만큼 증가
                
            else: #그 다음 큰 work와 작업량이 2 이상 차이 난다면
                work_remain_list.append([time-1,amount]) #가장 큰 work -1 해서 삽입
                
            n -= amount #전체 n에서 작업량 감소
            
        else: #현재 n으로 가장 큰 work의 갯수만큼 한 번에 처리할 수 없다면
            
            #빈 배열 아니고 그 다음 큰 work와 작업량이 1차이 난다면
            if work_remain_list and work_remain_list[-1][0] == time -1:
                work_remain_list[-1][1] += n #남은 n만큼만 작업량 수행
                
            else: #그 다음 큰 work와 작업량이 2 이상 차이 난다면
                work_remain_list.append([time-1,n]) #남은 n만큼만 작업량 수행
            
            #n번 작업량 모두 소진 후 가장 큰 work를 남은 횟수만큼 리스트에 삽입
            work_remain_list.append([time,amount-n])
            break
    
    #모든 작업이 0 이하일때
    if work_remain_list[-1][0] <=0: 
        return 0
    
    result = 0
    for time, amount in work_remain_list: #제곱해서 결과 도출
        result+= amount*time**2
        
    return result
