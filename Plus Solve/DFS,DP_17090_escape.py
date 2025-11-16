# 크기가 N*M인 미로
# 적혀있는 문자에 따라서 다른 칸으로 이동 가능

# 탈출 가능한 칸의 개수
# 그 칸에서 이동을 시작해서 칸에 적힌대로 이동했을 때, 미로의 경계 밖으로 이동하게 되는 칸

import sys
sys.setrecursionlimit(10000000)

# 세로 N, 가로 M
N, M = map(int, input().split())
world = [list(input().strip()) for _ in range(N)]

dp = [[-1] * M for _ in range(N)]

def recur(x, y):

    # 탈출 성공
    if x < 0 or x >= M or y < 0 or y >= N:
        return 1
    
    # 무한 사이클 해결
    if (dp[y][x] == 0):
        return -9999
    
    # 이미 방문했다면, 재사용
    if dp[y][x] != -1:
        return dp[y][x]
    
    # 기본값 부여 > 또 방문하면 너 봤던 놈 ㅇㅇ.
    dp[y][x] = 0

    dx, dy = 0, 0
    if world[y][x] == 'U': dy = -1
    elif world[y][x] == 'R': dx = 1
    elif world[y][x] == 'D': dy = 1
    elif world[y][x] == 'L': dx = -1

    nx = x + dx
    ny = y + dy
    dp[y][x] = recur(nx, ny)
    
    return dp[y][x]

for y in range(N):
    for x in range(M):
        recur(x, y)

result = 0
for y in range(N):
    for x in range(M):
        if dp[y][x] == 1:
            result += 1

#print(dp)
print(result)