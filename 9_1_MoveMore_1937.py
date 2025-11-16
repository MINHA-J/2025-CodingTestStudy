import sys
sys.setrecursionlimit(900000)

N = int(input())
table = [list(map(int, input().split())) for _ in range (N)]

# 자리를 옮기면 그 옮긴 지역에 그 전 지역보다 대나무가 더 많아야 함
# 이동할 수 있는 칸의 수의 최대값

dp = [[0] * N for _ in range (N)]

# 상 하 좌 우
dy = [+1, -1, 0, 0]
dx = [0, 0, -1, +1]
# for (dx, dy) in [ ... ]


def recur(x, y):

    # 메모리제이션 중요
    if dp[x][y] != 0:
        return dp[x][y]
    
    for d in range(4):
        _x = x+dx[d]
        _y = y+dy[d]

        if 0 <= _x < N and 0<= _y < N:
            if table[x][y] < table[_x][_y]:
                dp[x][y] = max(dp[x][y], recur(_x, _y) + 1)
    
    return dp[x][y]

for i in range (N):
    for j in range (N):
        recur(i, j)

print(max(map(max, dp))+1) 


# 모든 점을 방문한다
# 방문한 뒤에 이동할 수 있는 모든 경우의 수를 재귀로 구현
# 재귀로 구현한 뒤 DP로 바꿈