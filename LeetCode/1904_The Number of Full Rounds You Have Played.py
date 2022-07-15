class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        split_login = loginTime.split(":")
        login_h = int(split_login[0])
        login_m = int(split_login[1])
        
        split_logout = logoutTime.split(":")
        logout_h = int(split_logout[0])
        logout_m = int(split_logout[1])
        
        #print(login_h, login_m)
        #print(logout_h, logout_m)
        
        #분 단위로 환산
        min_login = (login_h * 60) + login_m
        min_logout = (logout_h * 60) + logout_m
        
        #print(min_login, min_logout)
        
        now_start_time = 0
        now_end_time = 15
        
        count = 0
    
        if min_login < min_logout: #로그아웃 시간이 더 크다면
            while True:
                if now_start_time < min_login: #아직 로그인 전이라면
                    now_start_time += 15
                    now_end_time += 15
                #현재 로그인 시간과 로그아웃 사이이며 그 사이에 15분의 텀이 있다면
                elif min_login <= now_start_time <= min_logout and min_login <= now_end_time <= min_logout:
                    count += 1
                    now_start_time += 15
                    now_end_time += 15
                #현재 시간 + 15분이 로그아웃 시간을 넘어버린다면
                elif min_logout < now_end_time:
                    break
                
        #로그아웃 시간이 더 작다면 즉 자정을 지난 경우
        elif min_login > min_logout:
            while True:
                #현재 시간과 현재 시간 + 15분이 로그아웃 시간 이전이라면
                if now_start_time <= min_logout and now_end_time <= min_logout:
                    count += 1
                    now_start_time += 15
                    now_end_time += 15
                #현재 시간과 현재 시간 + 15분이 로그인 시간 이후라면
                elif min_login <= now_start_time and min_login <= now_end_time:
                    count += 1
                    now_start_time += 15
                    now_end_time += 15
                else: #현재 시간이 로그아웃 시간 ~ 로그인 시간 사이라면
                    now_start_time += 15
                    now_end_time += 15
                
                #00:00 부터 24:00까지 다 탐색했을 경우
                if now_start_time == (24 * 60): #현재 시각이 자정이라면
                    break
        
        return count
