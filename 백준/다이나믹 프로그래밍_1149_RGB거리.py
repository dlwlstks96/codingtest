# -*- coding: utf-8 -*-

n = int(input())

red = [0]
green = [0]
blue = [0]

for i in range(n):
    r, g, b = map(int, input().split())
    red.append(r)
    green.append(g)
    blue.append(b) #색깔 저장
    
for i in range(1, n+1):
    red[i] += min(green[i-1], blue[i-1])
    green[i] += min(red[i-1], blue[i-1])
    blue[i] += min(red[i-1], green[i-1])
    
print(min(red[n], green[n], blue[n]))
    
'''
    
minVal = 0 #각 진행별 최솟값
nextMinVal = 0 #각 진행별 최솟값 다음 값
prevColor1 = -1 #0, 1, 2 -> r, g, b
prevColor2 = -1

dp = [0 for i in range(n+1)]

if n == 1:
    print(min(red[1], green[1], blue[1]))
else:
    tmp = [red[1], green[1], blue[1]]
    tmp.sort() #오름차순
    minVal = tmp[0]
    nextMinVal = tmp[1]
    if tmp[0] == red[1]: #빨간 집이 최솟값이면
        prevColor1 = 1
    elif tmp[0] == green[1]:
        prevColor1 = 2
    else:
        prevColor1 = 3
    if tmp[1] == red[1] and prevColor1 != 1:
        prevColor2 = 1
    elif tmp[1] == green[1] and prevColor1 != 2:
        prevColor2 = 2
    else:
        prevColor2 = 3
    for i in range(2, n+1):
        nowColor = -1
        tmp = [red[i], green[i], blue[i]]
        tmp.sort() #오름차순 정렬
        if tmp[0] == red[i]: #지금 칠한게 빨강이면
            nowColor = 1
        elif tmp[0] == green[i]: #초록이면
            nowColor = 2
        else: #파랑이면
            nowColor = 3
        if prevColor1 == nowColor: #지금 칠한게 이전에 칠한 집과 같다면
            comp1 = nextMinVal + tmp[0] #바로 이전 두번째 최솟값과 지금 칠한 최솟값
            comp2 = minVal + tmp[1] #바로 이전 최솟값과 지금 두번째 최솟값
            if comp1 <= comp2:
                dp[i] = comp1
                minVal = comp1
                prevColor1 = nowColor
            else: #comp1 > comp2
                dp[i] = comp2
                minVal = comp2
                prevColor1 = prevColor2
        else: #지금 칠한게 이전에 칠한 집과 다르다면
            dp[i] = minVal + tmp[0]
            minVal = minVal + tmp[0]
            prevColor1 = nowColor
            
        print(minVal, nowColor)
                
print(dp[n])

'''