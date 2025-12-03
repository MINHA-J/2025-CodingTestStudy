# 1309번, 동물원, 실버1

# 2*n 배열에 사자를 배치하는 경우의 수가 몇가지 인지 출력
# 사자를 한마리도 배치하지 않는 경우의 수도 하나의 경우의 수

import sys
sys.setrecursionlimit(900000)

N = int(input())
# 최대 N 마리 배치 가능

answer = 1

# DP의 핵심 요소를 잘못 설정했었음
# 이번 열에 사자를 어떻게 둘 것 인가?
# 이전 열의 상태를 보고 결정하는 DP

# 여기에 메모이제이션 어떻게 할지 고민하고 추가해보기

def recur(idx, before): 
    if idx == N:
        return 1
    
    # 이미 파악된 경로인지 확인
    if memory[idx][before] != -1:
        return memory[idx][before]

    temp = 0
    # 이전 라인에 놓지 않았다면
    if before == 0:
        temp += recur(idx+1, 0)
        temp += recur(idx+1, 1)
        temp += recur(idx+1, 2)
        memory[idx][0] = temp%9901
    elif before == 1:
        temp += recur(idx+1, 0)
        temp += recur(idx+1, 2)
        memory[idx][1] = temp%9901
    elif before ==2:
        temp += recur(idx+1, 0)
        temp += recur(idx+1, 1)
        memory[idx][2] = temp%9901

    return temp%9901


idx = 0 # 동일한 리스트에서 idx만 증가시키면서 쓰려고
memory = list([-1 for _ in range(3)] for _ in range(N))

print(recur(0,0)%9901)
#print(memory)