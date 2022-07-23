def solution(s):
    answer = []
    
    s = s[2:len(s)-2]
    split_s = s.split('},{')
    #print(split_s)
    
    l = [0 for _ in range(len(split_s))]
    
    for now_s in split_s:
        if ',' not in now_s: #원소 하나 집합
            l[0] = [int(now_s)]
        else: #원소 두 개 이상 집합
            tmp_l = []
            now_s = now_s.split(',')
            for num in now_s:
                tmp_l.append(int(num))
            l[len(tmp_l)-1] = tmp_l
    
    #print(l)
    
    for nowL in l:
        for num in nowL:
            if num not in answer:
                answer.append(num)
                break
    
    return answer
