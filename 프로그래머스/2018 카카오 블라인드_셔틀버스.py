# -*- coding: utf-8 -*-

from collections import deque

def solution(n, t, m, timetable):    
    time = ''
    hour = 9 #9시
    miniute = 0 #0분
    
    bus_time = [[9, 0]] #첫 버스 도착 시간
    for i in range(1, n):
        miniute += t
        if miniute >= 60: #분 단위 초과시
            hour += 1
            miniute -= 60
        bus_time.append([hour, miniute]) #버스의 모든 도착 시간
    
    crew_time = [] #크루원들의 각 도착 시간
    for i in timetable:
        tmp = i.split(':') # ':' 기준으로 분리
        tmp = [tmp[0], tmp[1]]
        crew_time.append([int(tmp[0]), int(tmp[1])]) 
        
    crew_time.sort() #크루원 도착 시간 빠른 순부터
    crew_time = deque(crew_time)
    
    count = 0 #시간이 지남에 따라 버스에 태우는 인원 수
    bus = 0 #한 번 버스에 탑승 인원
    prev_crew = [0, 0] #이전에 탑승한 크루원 시간
    answer = [0, 0]   
    
    for now_bus_time in bus_time:
        bus = 0 #버스에 탑승하고 있는 인원
        if count == m*n: #하루에 태울 수 있는 인원 다 태우면
            break
        while crew_time:
            if bus == m: #버스 만원 시
                break #다음 시간대 버스 호출
            if count == m*n: #오늘 태울 사람 다 태운거라면
                break
            now_crew = crew_time.popleft() #현재 버스 시간과 비교해볼 크루원 시간
            if now_bus_time >= now_crew: #현재 버스보다 크루원이 빨리 도착했다면
                prev_crew = now_crew
                bus += 1
                count += 1
            else: #현재 버스보다 크루원 도착 시간이 늦다면, 버스 보내야함
                crew_time.appendleft(now_crew)
                bus = 0
                break
    #print(prev_crew, count, bus)
    
    last_bus = bus_time.pop() #버스 마지막 도착 시간
    
    if count < m*n: #오늘 태울 수 있는 인원을 다 못 태운 경우
        if bus == m: #마지막 버스가 만원일 경우
            answer = [prev_crew[0], prev_crew[1]-1]
        else: #마지막 버스에 공간이 남아있을 경우
            answer = last_bus
    elif count == m*n: #오늘 태울 수 있는 인원을 다 태운 경우
        if bus == m: #마지막 버스가 만원일 경우
            answer = [prev_crew[0], prev_crew[1]-1]
        else: #마지막 버스에 공간이 남아있을 경우
            answer = last_bus
            
    if answer[1] < 0: #분 단위 음수일 경우 처리
        answer[0] = answer[0] - 1
        answer[1] = 59
    
    #정답 출력을 위한 문자열 처리
    if answer[0] < 10:
        time += "0" + str(answer[0]) + ":"
    else:
        time += str(answer[0]) + ":"
        
    if answer[1] < 10:
        time += "0" + str(answer[1])
    else:
        time += str(answer[1])
        
    #print(time)
         
    return time

#solution(2, 10, 2, ["09:10", "09:09", "08:00"])
solution(1, 10, 1, 	["09:00", "09:18"])
#solution(1, 1, 5, ["08:00", "08:01", "08:02", "08:03"])
#solution(3, 10, 1, ["00:01", "00:01", "00:01", "00:01", "00:01"])
