# -*- coding: utf-8 -*-


n = int(input())

# 숫자는 0 ~ 9를 이용하고, 입력되는 n, 즉 자릿수는 1~100이므로
# dp의 예시는 아래와 같다
'''
            0  1  2  3  4  5  6  7  8  9 -> 각 자릿수에서 맨 뒤에 올 수 있는 숫자의 갯수
자리수(1)   0  1  1  1  1  1  1  1  1  1
자리수(2)   1  1  2  2  2  2  2  2  2  1
자리수(3)   1  3  3  4  4  4  4  4  3  2
'''
dp = [[0 for i in range(10)] for j in range(101)]

for i in range(1, 10):
    dp[1][i] = 1 #자리수(1) 라인의 1~9 칸을 1로 세팅
for i in range(2, n+1):
    for j in range(10):
        if j == 0: #dp[i][0]은 오른쪽 대각선 위의 숫자와 동일
            dp[i][j] = dp[i-1][1]
        elif j == 9: #dp[i][9]은 왼쪽 대각선 위의 숫자와 동일
            dp[i][j] = dp[i-1][8]
        else: #나머지 숫자들은 왼쪽 대각선 위, 오른쪽 대각선 위 숫자들의 합이다
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            
print(sum(dp[n]) % 1000000000)



#-------------아래는 내가 작성한 오답------------------


# import itertools as it

# l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# cnt = 0

# # for i in it.product(l, repeat=8):
# #     if i[0] != 0 and abs(i[0] - i[1]) == 1 and abs(i[1] - i[2]) == 1 and abs(i[2] - i[3]) == 1 and abs(i[3] - i[4]) == 1 and abs(i[4] - i[5]) == 1 and abs(i[5] - i[6]) == 1 and abs(i[6] - i[7]) == 1:
# #         #print(i)
# #         cnt += 1

# # print(cnt)

# for i in it.product(l, repeat=4):
#     if i[0] != 0 and abs(i[0] - i[1]) == 1 and abs(i[1] - i[2]) == 1 and abs(i[2] - i[3]) == 1:
#         print(i)
#         cnt += 1

# print(cnt)

'''

n=2 18-1 = 17
n=3 36-4 = 32
n=4 72-11 = 61
n=5 144-28 = 116
n=6 288-66 = 222
n=7 576-152 = 424
n=8 1152-339 = 813

-1 (3) -4 (7) -11 (17) -28 (38) -66 (86) -152


'''