# 1로 만들기 (골드 5)

# 3으로 나누어 떨어지면 3으로 나누고
# 2로 나누어 떨어지면 2로 나누고
# 1은 빼고

# 연산을 사용하는 횟수의 최솟값을 출력하시오

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline # 속도향상

# 1 <= N <= 1000000
N = int(input())

memory = [-1 for _ in range(N+1)] #연산 횟수 값을 저장하는 배열
choice = [-1 for _ in range(N+1)] #경로를 위한 다음 숫자

def recur(num):
    
    if (num == 1):
        return 0
    
    # 해당 수에 방문 한 상태라면,
    if (memory[num] != -1):
        return memory[num]
    
    
    memory[num] = recur(num-1) + 1
    choice[num] = num - 1

    if num % 3 == 0:
        temp = recur(num//3) + 1
        if temp < memory[num]:
            memory[num] = temp
            choice[num] = num//3
            
    if num % 2 == 0:
        temp = recur(num//2) + 1
        if temp < memory[num]:
            memory[num] = temp
            choice[num] = num//2

    return memory[num]

if N==1:
    print(0)
    print(1)
else:
    numList = []
    numList.append(N)
    result = recur(N)

    print(result)
    path = []
    now = N
    while now != -1:
        path.append(now)
        now = choice[now]
    print(*path)

    #print(*before[:result+1])