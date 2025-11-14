# 1149

N = int(input())
prices = [list(map(int, input().split())) for _ in range(N)]
# n번 집을 빨/초/파로 칠하는 비용

''' 첫 번째 풀이 방법
# RGB
result = 99999999999

# 첫 번째 집이 R / G / B 
for i in range(3):
    curPrices = prices[0][i]
    prior = i
    print(i, "번째 ", prior+1)
    
    for j in range(1, N):
        curPrices += min(prices[j][(prior+1)%3], prices[j][(prior+2)%3])
        
        if prices[j][(prior+1)%3] < prices[j][(prior+2)%3]:
            prior = (prior+1)%3
        else:
            prior = (prior+2)%3

        print(j, "번째 ", prior+1)
    print(curPrices)
    result = min(result, curPrices)

print(result)
'''

# 아 위는 당장 저렴한 색을 고르는 그리디 알고리즘인데,
# 해당 문제는 앞에서 어떤 색을 골랐는가? 에 따라 뒤에 올 수 있는 조합이 달라지니까
# DP로 풀어야 하는게 맞음

dp = list([0] * 3 for _ in range(N))
# idx 번 집까지의 최소 비용
dp[0][0] = prices[0][0]
dp[0][1] = prices[0][1]
dp[0][2] = prices[0][2]

for idx in range(1, N):
    for rgb in range(3):
        
        # 지금 해당 색으로 칠한다고 할 때, 이전이 날 제외하고 최소
        if rgb == 0:
            dp[idx][rgb] = min(dp[idx-1][1], dp[idx-1][2]) + prices[idx][rgb]
        if rgb == 1:
            dp[idx][rgb] = min(dp[idx-1][0], dp[idx-1][2]) + prices[idx][rgb]
        if rgb == 2:
            dp[idx][rgb] = min(dp[idx-1][0], dp[idx-1][1]) + prices[idx][rgb]

print(min(dp[N-1]))