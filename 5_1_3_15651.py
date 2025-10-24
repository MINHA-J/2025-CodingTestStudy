# 같은 수를 여러 번 골라도 됨

N, M = map(int, input().split())

arr = []

def recur(number): 
    if (number == M):
        print(*arr)
        return
    
    for i in range(1, N+1):
        #if (i in arr):
        #    continue
        arr.append(i)
        recur(number+1)
        arr.pop()

recur(0)