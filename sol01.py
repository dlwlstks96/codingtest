# -*- coding: utf-8 -*-

id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2


def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))]
    
    report_num_list = {}
    
    for i in id_list:
        report_num_list[i] = []
    
    for i in report:
        tmp = i.split(' ')
        report_num_list[tmp[1]].append(tmp[0])
        
    for i in report_num_list.keys():
        report_num_list[i] = set(report_num_list[i])
        report_num_list[i] = list(report_num_list[i])
       
    
    for i in id_list:
        if len(report_num_list[i]) >= k:
            for j in report_num_list[i]:
                idx = id_list.index(j)
                answer[idx] += 1

    return answer

solution(id_list, report, k)