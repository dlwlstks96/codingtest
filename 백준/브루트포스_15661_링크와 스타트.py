import itertools as it
import math

n = int(input())

board = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    
#print(board)

minVal = 9999999999 #두 팀의 능력치 차이 저장 / 최솟값 찾아야함

for pickCount in range(1, math.floor(n/2)+1):
    
    if minVal == 0:
        break
    
    pick = it.combinations(range(n), pickCount)
    for p in pick:
        p = list(p)
        
        linkSum = 0
        starSum = 0
        
        link = []
        star = []
        
        for linkMember in p: #link팀 멤버
            link.append(linkMember)
            
        for starMember in range(n): #star팀 멤버
            if starMember not in link:
                star.append(starMember)
        
        for i in range(len(link)-1): #link팀 능력치 합산
            for j in range(i+1, len(link)):
                linkSum += board[link[i]][link[j]]
                linkSum += board[link[j]][link[i]]
                
        for i in range(len(star)-1):
            for j in range(i+1, len(star)):
                starSum += board[star[i]][star[j]]
                starSum += board[star[j]][star[i]]
        
        minVal = min(minVal, abs(linkSum - starSum))
        
        # print(link, linkSum)
        # print(star, starSum)
        # print(minVal)
        # print('============', p)
        
        if minVal == 0:
            break
        
print(minVal)
