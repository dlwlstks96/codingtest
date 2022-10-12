t = int(input())

for _ in range(t):
    p = input()
    n = int(input())
    arr = input()
    
    if arr != '[]':
        arr = arr[1:len(arr)-1]
        arr = list(map(int, arr.split(',')))
    else:
        arr = []
    
    #print(arr)
    
    leftP = 0 #왼쪽 포인터
    rightP = len(arr) - 1 #오른쪽 포인터
    checkLeft = True #포인터 위치
    checkError = False #에러 유무
    arrCount = len(arr) #초기 원소 갯수
    
    for nowCommand in p:
        
        #print(nowCommand, leftP, rightP, checkLeft)
        
        if nowCommand == 'R': #뒤집어라
            if checkLeft == True: #포인터 위치 반대로
                checkLeft = False
            else:
                checkLeft = True
                    
        elif nowCommand == 'D': #하나를 버려라
            if arrCount == 0: #배열이 비어 있을 경우
                checkError = True
                break
            
            if checkLeft == True: #현재 왼쪽 포인터라면
                leftP += 1
            elif checkLeft == False: #현재 오른쪽 포인터라면
                rightP -= 1
                
            arrCount -= 1
    
    answer = []
    if checkError == False: #에러가 난 경우가 아니라면
        if checkLeft == True: #왼쪽 포인터라면
            if rightP == 0: #오른쪽 포인터가 안움직였다면
                answer = arr[leftP:]
            else:
                answer = arr[leftP:rightP+1]
        elif checkLeft == False: #오른쪽 포인터라면
            if leftP == 0: #왼쪽 포인터가 안움직였다면
                answer = arr[rightP::-1]
            else:
                answer = arr[rightP:leftP-1:-1]
        
        print('[', end = '')
        for idx, a in enumerate(answer):
            if idx != len(answer)-1:
                print(a, end = '')
                print(',', end = '')
            else:
                print(a, end = '')
        print(']')
        
    elif checkError == True: #에러가 난 경우라면
        print('error')
