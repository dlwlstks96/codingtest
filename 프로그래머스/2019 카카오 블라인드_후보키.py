# -*- coding: utf-8 -*-

import itertools as it

def solution(relation):
    answer = 0
    
    #유일성을 만족하는 모든 키를 저장
    keyList = []
    
    for num in range(1, len(relation[0])+1):
        comb = it.combinations(range(len(relation[0])), num)
        for now_comb in comb:
            tmp = [] #데이터 임시로 담을 리스트
            for data in relation:
                tmp_data = "" #인덱스 뽑아 데이터 묶을 문자열
                for data_idx in now_comb:
                    tmp_data += str(data[data_idx])
                tmp.append(tmp_data)
            #print(tmp)
            #print(now_comb)
            
            tmp_set = set(tmp) #중복 제거
            
            #중복이 하나도 없었다면 유일성 만족으로 keyList에 저장
            if len(tmp_set) == len(tmp):
                keyList.append(now_comb)
    
    #최소성 확인을 위한 리스트
    check = [0 for i in range(len(keyList))]
    
    #keyList를 순회하며 i번째 튜플의 원소들이
    #j번째 튜플에 모두 들어가 있다면 check[j] = 1로 변경
    for i in range(len(keyList)-1):
        for j in range(i+1, len(keyList)):
            count = 0
            for k in keyList[i]:
                if k in keyList[j]:
                    count += 1
                if count == len(keyList[i]):
                    check[j] = 1
                
    #check 값이 0인 원소들만 카운트
    answer = check.count(0)
    
    return answer

# solution([["100","ryan","music","2"],["200","apeach","math","2"],
#           ["300","tube","computer","3"],["400","con","computer","4"],
#           ["500","muzi","music","3"],["600","apeach","music","2"]])

solution([ ["a","1","aaa","c","ng"],
["a","1","bbb","e","g"],
["c","1","aaa","d","ng"],
["d","2","bbb","d","ng"]])