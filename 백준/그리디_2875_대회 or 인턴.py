# -*- coding: utf-8 -*-

import math

n, m, k = map(int, input().split())

girl = n // 2
boy = m // 1
intern = k

max_team = min(girl, boy) #인턴쉽 고려 x, 만들 수 있는 최대 팀

girl_tmp = n - (2*max_team) #최대 팀 만들고 남은 여자
boy_tmp = m - (1*max_team) #최대 팀 만들고 남은 남자

intern -= (girl_tmp + boy_tmp) #남아 있는 인원 수 먼저 인턴쉽으로 차출(팀 구성 방해 안하게)

#print(girl_tmp, boy_tmp, max_team, intern)

if intern < 1: #해체 되는 팀 없단 의미
    print(max_team)
else:
    intern = math.ceil(intern / 3) #인턴 차출로 인해 해체되는 팀의 갯수
    max_team -= intern
    print(max_team)