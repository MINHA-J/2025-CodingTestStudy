# 같은 수를 여러 번 골라도 됨
# 수열이 비내림차순 이어야 함

N, M = map(int, input().split())

arr = []

def recur(start, number): 
    if (number == M):
        print(*arr)
        return
    
    for i in range(start, N+1):
        #if (len(arr) > 0 and i > arr[-1]):
        #    continue
        arr.append(i)
        recur(i, number+1)
        arr.pop()

recur(1, 0)