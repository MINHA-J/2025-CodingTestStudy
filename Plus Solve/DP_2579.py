# 2579번 / 계단 오르기 / 실버3 

# 계단은 하나 다음 또는 2개 다음으로 오르기 가능
# 연속 3개 계단 밟기 불가능

N = int(input())
stairs = list(0 for _ in range(N+1))
for i in range (1, N+1):
    stairs[i] = int(input())


dp = list(0 for _ in range(N+1))

dp[1] = stairs[1]
# dp[2]
#   stairs[1] + stairs[2] 연속 두번
#   stairs[0] + stairs[2] 뛰어 넘기

if N > 1:
    dp[2] = stairs[1] + stairs[2]
    # dp[3] = max(
    #     dp[1] + stairs[3],
    #     dp[0] + stairs[2] + stairs[3]
    # )


    for idx in range(3, N+1):
        dp[idx] = stairs[idx] + max(dp[idx-2], dp[idx-3] + stairs[idx-1])

print(dp[N])
