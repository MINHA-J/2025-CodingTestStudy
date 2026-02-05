# 섬의 개수 / 4963 / 실버2

# 1은 땅, 0은 바다

# 상 하 좌 우 
# 오위, 왼위, 오아, 왼아
dx = [0, 0, +1, -1, -1, +1, -1, +1]
dy = [-1, +1, 0, 0, -1, -1, +1, +1]

world = list([0 for _ in range(50)] for _ in range(50))
visited = list([0 for _ in range(50)] for _ in range(50))


def dfs(y, x):
    # 땅이라면
    if world[y][x] == 0:
        return 0
    
    # 이미 방문했다면
    if visited[y][x] == 1:
        return 0

    visited[y][x] = 1

    for i in range(8):
        ny = y + dy[i]
        nx = x + dx[i]
        if (0 <= ny < h) and (0 <= nx < w):
            dfs(ny, nx)

    return 1

while True:
    w, h = map(int, input().split())

    # Test case 종료 조건
    if w == 0 and h == 0: 
        break
    
    answer = 0
    for j in range(h):
        world[j] = list(map(int, input().split()))
        visited[j] = list(0 for _ in range(w))

    for i in range(w):
        for j in range(h):
            if world[j][i] != 0 and visited[j][i] != 1: 
                dfs(j, i)
                answer += 1

    print("정답: "+ answer)

