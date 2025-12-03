# 정수 삼각형, 1932번, 실버1

# 맨 위층부터 아래에 있는 수 중 하나를 선택.
# 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 프로그램
# 대각선 왼쪽 또는 대각선 오른쪽만 가능

n = int(input())
triangle = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(n)] for _ in range(n)]

# y는 층 수
# 왼쪽(+1,0) 오른쪽(+1, +1)
def recur(y, x):

    if y == n-1:
        return triangle[y][x]
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    if y+1 < n:
        dp[y][x] = recur(y+1, x) + triangle[y][x]   # 왼쪽으로 향하기
    if y+1 < n and x+1 <= y+1:
        dp[y][x] = max(dp[y][x],
                       recur(y+1, x+1) + triangle[y][x]) # 오른쪽으로 향하기

    return dp[y][x]

print(recur(0, 0))
#print(dp)
    
