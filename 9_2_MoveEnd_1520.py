# 내리막길(골드3)

import sys
sys.setrecursionlimit(900000)


M, N = map(int, input().split()) # 세로, 가로
world = [list(map(int, input().split())) for _ in range (M)]

dx = [+1, -1, 0, 0]   # 행 변화량
dy = [0, 0, -1, +1]   # 열 변화량

dp = [[-1] * N for _ in range (M)]

def recur(x, y):

    if x == M-1 and y == N-1:
        return 1

    # 모든 지점에서 계산이 한번이라도 되었다면 재사용한다
    if dp[x][y] != -1:
        return dp[x][y]

    dp[x][y] = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        if (0 <= nx < M and 0 <= ny < N):
            if (world[x][y] > world[nx][ny]):
                dp[x][y] += recur(nx, ny)

    return dp[x][y]


print(recur(0, 0)) 
#print(dp)
        