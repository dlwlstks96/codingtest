def solution(stones, k):
    answer = 0
    
    if k == 1:
        answer = min(stones)
        return answer
    
    start = min(stones) #디딤돌 최솟값
    end = max(stones) #디딤돌 최댓값
    
    
    while start <= end:
        mid = (start + end) // 2 #중앙값, 이만큼 건넜다는 의미
        
        count = 0
        for stone in stones: #디딤돌 하나씩 가져와서
            if stone - mid <= 0: #디딤돌 한 칸당 이만큼 mid만큼 건넜다면
                count += 1 #1씩 증가시켜 연속된 점프 디딤돌 카운트
            else: #stone - mid > 0일 경우 연속된 점프 디딤돌 아니니 count 초기화
                count = 0
                
            if count >= k: #k개만큼 연속된 점프 디딤돌 나오면 중단
                break
            
        if count < k: #성공적으로 건넜으니 왼쪽 값 증가(mid 증가)
            start = mid + 1
        else: #성공적으로 건너지 못했으니 오른쪽 값 감소(mid 감소)
            end = mid - 1
            answer = mid #count == k가 될 때가 정답이 된다
            
    return answer

solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)