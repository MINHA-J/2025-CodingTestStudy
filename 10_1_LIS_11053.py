# 가장 긴 증가하는 부분 수열, 11053

import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))

# DP key로 활용하는거 확인하기
dp = {}

# i까지
def recur(before, i):

    # 범위 제한
    if i == N:
        return 0
    
    # 메모이제이션
    key = (before, i)
    if key in dp:
        return dp[key]

    # 1) i를 고르지 않는 경우
    # 처음에 못 넣는 경우 그냥 return을 때려 버렸는데,
    # 그러면 연산이 진행이 안 되는구나!! 아쉽 .... 헷갈렸다
    best = recur(before, i + 1)

    # 2) 현재 i를 고르고 넘어가는 경우
    if before < sequence[i]:
        best = max(best, 1+ recur(sequence[i], i + 1))

    dp[key] = best
    return best

print(recur(-10**9, 0))





