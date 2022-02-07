# -*- coding: utf-8 -*-

#정렬 후 for문을 통해 왼쪽부터 체크해나감과 동시에 오른쪽 요소들도 체크해 나아간다.
#이 때 중요한 점은 오른쪽 요소들 또한 -1, -2, -3 순으로 체크가 된다는 점
# 인덱스 -1이 못 타고 -2가 타는 경우는 없다.
def solution(people, limit):
    answer = 0
    
    check = [0 for i in range(len(people))] #구출했는지 체크
    
    people.sort(reverse = True) #몸무게 내림차순 정렬
    
    r_idx = 1 #오른쪽에서부터 카운트하는 idx 기준
    
    for i in range(len(people)):
        boat = 0
        if check[i] == 0: #아직까지 구출되지 않은 사람일 경우
            boat += people[i] #현 인원 탑승
            check[i] = 1 #탑승 체크
            for j in range(r_idx, len(people) - i):
                if (people[-j] + boat) <= limit and check[-j] == 0: #더 탈 수 있을 때
                    boat += people[-j]
                    check[-j] = 1
                    r_idx = j+1
                else: #더 탈 수 없을 경우
                    break
            answer += 1
        else:
            break
        
    return answer

solution([70, 50, 80, 50], 100) #80 70 50 50