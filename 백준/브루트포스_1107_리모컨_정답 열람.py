target = int(input())
ans = abs(100 - target) # ++ or -- 로 이동할 경우 -> 최댓값
M = int(input())
if M: # 고장난게 있을 경우만 인풋을 받음
    broken = set(input().split())
else:
    broken = set()

# 작은수에서 큰수로 이동할땐 500,000 까지만 보면 되지만
# 반대로 큰수에서 작은수로 내려올수도 있으므로 1,000,000 까지 봐야함
for num in range(1000001): 
    for N in str(num):
        if N in broken: # 해당 숫자가 번호를 눌러서 만들 수 없는 경우엔 스탑
            break
    else: # 번호를 눌러서 만들 수 있는 경우엔
    	# min(기존답, 번호를 누른 횟수 + 해당 번호로부터 타겟까지의 차이)
        ans = min(ans, len(str(num)) + abs(num - target))

print(ans)

'''

import sys

# n = map(int, sys.stdin.readline())
n = int(input())

m = int(input())
if m != 0:
    break_button = list(map(str, input().split()))
else:
    break_button = []
    
if n == 100:
    print(0)
    sys.exit(0)
    
button = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for b in break_button: #고장난 버튼을 버튼 전체 목록에서 제거
    button.remove(b) #0 1 2 3 4 5 9
    
near_num = ''
    
for i in range(len(str(n))):
    up_num = int(str(n)[i])
    down_num = int(str(n)[i])
    if str(n)[i] in button: #현재 누를까 하는 숫자가 고장 안났다면
        near_num += str(n)[i]
    else: #현재 누를까 하는 숫자가 고장 났다면
        while True:
            up_num += 1
            if up_num > 9:
                up_num = 0
                
            down_num -= 1
            if down_num < 0:
                down_num = 9
                
            if str(up_num) in button:
                near_num += str(up_num)
                break
            elif str(down_num) in button:
                near_num += str(down_num)
                break
            
print(near_num)

jump_way = (len(str(near_num)) + abs((int(near_num) - n)))
direct_way = abs(n - 100)

answer = min(jump_way, direct_way)

print(answer)

#==================================================
    
# #-1, +1 번갈아가며 확인해볼 숫자
# down_num = n
# up_num = n
# near_num = -1
# now_num = ['1', '0', '0']
# up_down_cnt = 0

# answer = 0

# if n == 100: #100번 입력했다면 0 출력 후 종료
#     print(0)
#     sys.exit(0)

# while True:
#     cnt = 0
#     for d in str(down_num):
#         if d in break_button: #고장난 버튼이 들어있다면
#             down_num -= 1
#             break
#         cnt += 1 #지금의 숫자가 고장난 버튼이 아닐 경우 카운트 증가
#     if cnt == len(str(down_num)): #모든 숫자를 탐색했음에도 고장난 버튼 없는 경우
#         near_num = down_num
#         break
    
#     cnt = 0
#     for u in str(up_num):
#         if u in break_button: #고장난 버튼이 들어 있다면
#             up_num += 1
#             break
#         cnt += 1
#     if cnt == len(str(up_num)): #모든 숫자 탐색했는데 고장난 버튼 없는 경우
#         near_num = up_num
#         break
    
#     up_down_cnt += 1
    
# answer += (len(str(near_num)) + up_down_cnt)
    
# print(near_num, answer)

'''
