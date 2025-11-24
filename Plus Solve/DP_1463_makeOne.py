# 1463. 1로 만들기. 실버3
# 연산 3가지로 1로 만들기
#   3으로 나누어지면, 3으로 나누기
#   2로 나누어지면, 2로 나누기
#   1 빼기
# 연산을 사용하는 횟수의 최솟값

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline # 속도향상
N = int(input())

dp = [-1] * 1000001

def recur(num):

    if num == 1:
        return 0

    if dp[num] != -1:
        return dp[num]

    a, b, c = 1000000, 1000000, 1000000

    a = recur(num-1) + 1

    if num % 3 == 0:
        b = recur(num // 3) + 1

    if num % 2 == 0:
        c = recur(num // 2) + 1 

    dp[num] = min(a, b, c)

    return dp[num]

print(recur(N))
#print (dp)