# -*- coding: utf-8 -*-

#프로그래머스_힙_디스크 컨트롤러

import heapq as hq

jobs = [[0, 3], [1, 9], [2, 6]]

def solution(jobs):
    answer = 0
    
    jobs_len = len(jobs)
    
    hq.heapify(jobs) #힙 이용해 jobs 정렬
    
    time = 0
    now_task_finish_time = 0 #현재 작업의 종료 예정 시간
    now_task = [0, 0] #현재 진행중인 작업
    wait_task = [] #대기중인 작업 목록
    task_time_list = [] #각 요청부터 종료까지의 시간 목록
    
    while(True):
        
        if len(jobs) > 0 and min(jobs)[0] <= time: #지금 시간에 요청 들어온 작업이 있는 경우
                #min으로 받아오는 이유는 현재 진행과 대기 중인 작업이 없을 경우엔
                #가장 요청이 빠른 작업을 받아 오기 위함
                tmp = min(jobs)
                idx = jobs.index(tmp)
                jobs.pop(idx)
                tmp.reverse()#wait_task를 힙으로 정렬해 최소값을 가져오기 위해 순서 바꿈
                hq.heappush(wait_task, tmp)
        elif len(jobs) == 0 and len(wait_task) == 0:
            break

                
        if time >= now_task_finish_time: #진행중이던 작업이 끝난 경우
            if len(wait_task) >= 1: #대기중인 작업 1개 이상
                now_task = hq.heappop(wait_task) #소요시간 최소 작업을 가져옴
                now_task_finish_time = now_task[0] + time
                task_time_list.append(now_task_finish_time - now_task[1])
                time += 1
            elif len(wait_task) < 1: #대기중인 작업 X
                time += 1
                       
        else: #아직 작업중일때
            time = time + 1

    answer = int(sum(task_time_list) / jobs_len)
    return answer

solution(jobs)