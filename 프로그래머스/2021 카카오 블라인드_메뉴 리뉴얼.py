import itertools as it
import operator

def solution(orders, course):
    answer = []
    
    dic = {}
    
    for o in orders:
        o = list(o)
        o.sort() #주문 조합 내 알파벳 정렬
        
        for c in course:
            if c > len(o): #뽑아야 하는 갯수가 orders보다 크다면
                break
            
            pick = it.combinations(o, c) #1,2 / 1,3 / 1,4 / 2,3..
            for p in pick:
                
                str_p = ''.join(p) #선택된 리스트를 문자열로 합치기
                
                if str_p not in dic:
                    dic[str_p] = 1
                else:
                    dic[str_p] += 1
    
    #딕셔너리의 value 기준으로 내림차순 정렬
    sort_dic = sorted(dic.items(), key=operator.itemgetter(1), reverse=True)
    
    #print(sort_dic)
    
    #조합 갯수를 인덱스 삼아 최댓값 저장
    checkMax = [-1 for _ in range(max(course)+1)]
    
    for sd in sort_dic:
        k = sd[0]
        v = sd[1]
        
        if v == 1: #주문한 고객 수가 1명
            break
            
        if v >= checkMax[len(k)]: #현재 조합의 주문 수가 최댓값 이상이라면
            answer.append(k)
            checkMax[len(k)] = v
            
    answer.sort() #알파벳 순 정렬
    
    return answer
