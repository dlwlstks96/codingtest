import heapq as hq

n = int(input())

answer = []

leftHeap = []
rightHeap = []

for _ in range(n):
    
    inputNum = int(input())
    
    #길이가 같다면 중간 값의 기준이 되는 leftHeap에 수를 넣는다.
    if len(leftHeap) == len(rightHeap):
        hq.heappush(leftHeap, (-inputNum, inputNum)) #최대힙 사용 위해 -
    else: #길이가 다르다면 길이를 맞춰주기 위해 rightHeap에 수를 넣는다
        hq.heappush(rightHeap, (inputNum, inputNum)) #최소힙 사용
        
    #rightHeap에 값이 있고 만약 leftHeap의 루트가 rightHeap의 루트보다 크다면
    #leftHeap의 루트와 rightHeap의 루트를 바꿔준다.
    if rightHeap and leftHeap[0][1] > rightHeap[0][0]:
        minNum = hq.heappop(rightHeap)[0]
        maxNum = hq.heappop(leftHeap)[1]
        hq.heappush(leftHeap, (-minNum, minNum))
        hq.heappush(rightHeap, (maxNum, maxNum))
        
    answer.append(leftHeap[0][1])
    
for i in answer:
    print(i)
        
        
