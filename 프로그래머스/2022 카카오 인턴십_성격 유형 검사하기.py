def solution(survey, choices):
    answer = ''
    
    dic = {}
    dic["R"] = 0
    dic["T"] = 0
    dic["C"] = 0
    dic["F"] = 0
    dic["J"] = 0
    dic["M"] = 0
    dic["A"] = 0
    dic["N"] = 0
    
    for s, c in zip(survey, choices):
        if c == 4:
            continue
        elif c < 4:
            dic[s[0]] += (4 - c)
        else: #c > 4
            dic[s[1]] += (c - 4)
    
    #print(dic)
    
    count = 0
    tmp = []
    for d in dic.items():
        tmp.append(d)
        count += 1
        
        if count == 2:
            if tmp[0][1] == tmp[1][1]:
                answer += tmp[0][0]
            elif tmp[0][1] > tmp[1][1]:
                answer += tmp[0][0]
            else:
                answer += tmp[1][0]
            tmp = []
            count = 0
    
    return answer
