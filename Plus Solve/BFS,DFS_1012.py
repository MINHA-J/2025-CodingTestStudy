# 유기농배추 / 1012번 / 실버2

# 격자 그래프 위에서
# DFS 기반 Flood fill을 수행하여, connected components 개수를 세는 방식으로 풀었음

# 0 배추 심어져 있지 않음
# 1 배추 심어져 있음
# 배추를 보호하기 위해 필요한 최소의 배추흰지렁이 마리 수를 출력

import sys
sys.setrecursionlimit(10**7)

input = sys.stdin.readline # 속도향상

T = int(input()) # 테스트케이스 개수

dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

def recur(y, x):

    if visited[y][x] != -1: return 

    visited[y][x] = 1

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if (0 <= nx < M) and (0 <= ny < N):
            # 배추가 심어지지 않은 경우
            if (nx, ny) not in cabbages: 
                continue
            # 배추가 심어진 경우라면
            recur(ny, nx)

    return

for _ in range(T):
    # 가로 M, 세로 N, 배추 심어진 개수 K
    M, N, K = map(int, input().split())

    positions = [tuple(map(int, input().split())) for _ in range(K)]
    cabbages = set(positions)  # O(1) 조회용
    visited = [[-1 for _ in range(M)] for _ in range(N)]
    
    result  = 0
    for x, y in positions:
        if visited[y][x] == 1: 
            continue 

        result += 1
        recur(y, x)
    
    print(result)

