N, M = map(int, input().split())

arr = []
visited = []

def recur(start, number): 
    if (number == M):
        print(*arr)

        return
    
    for i in range(start, N+1):
        if (i in arr):
            continue
        arr.append(i)
        recur(i+1, number+1)
        # 아하.. 앞보다는 커야 하는데 이걸 어떻게 처리하나~ 했는데 
        # startIdx를 두고 하는구나
        arr.pop()

recur(1, 0)