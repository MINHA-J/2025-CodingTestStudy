# 보물섬 2589 골드5

# 육지L 또는 바다W
# 이동은 상하좌우 육지만, 한 칸에 한 시간
# 같은 곳을 2번 이상 지나가거나, 멀리 돌아가서는 X

# 보물은 (서로 간에 최단 거리로 이동)하는데, (가장 긴 시간)이 걸리는 육지 2곳에 묻힘
# 보물이 묻혀 있는 두 곳 사이를 최단 거리로 이동하는 시간을 출력
from collections import deque
import sys
input = sys.stdin.readline

h, w = map(int, input().split())

world = []
for _ in range(h):
    world.append(str(input()))
# world = [list(input().rstrip()) for _ in range (h)]

# 모든 좌표에서 가장 먼 거리가 몇 인지 업데이트 (완전탐색적 사고 ...)
result = 0
visited = [[0 for _ in range(w)] for _ in range(h)]
bfs_id = 0
max_possible = h + w - 2


for y in range(h):
    for x in range(w):

        # 바다라면 카운팅 제외
        if (world[y][x] == 'W'): continue
        
        # 좌표 마다 보니까 초기화
        # visited = [[0 for _ in range(w)] for _ in range(h)]
        # dist = [[0 for _ in range(w)] for _ in range(h)]
        q = deque()
        q.append((y, x, 0))

        bfs_id += 1
        visited[y][x] = bfs_id

        while q:
            ey, ex, dist = q.popleft()

            # 네 방향을 탐색함
            for dy, dx in [[0, -1], [0, +1], [-1, 0], [+1, 0]]:
                nx = ex+dx
                ny = ey+dy

                # 격자 범위 내이고, 육지 인 경우만 보자
                if 0 <= nx < w and 0 <= ny < h:
                    if (world[ny][nx] == 'W'): continue
                    if (visited[ny][nx] == bfs_id): continue
                    visited[ny][nx] = bfs_id
                    currdist = dist + 1
                    result = max(result, currdist)
                    q.append((ny, nx, currdist))
        
        # 현재 result가 이론상 최대라면, 더 보지 않아도 됨
        # 아 이거 추가하니까 시간 괜찮네 ~
        if result == max_possible:
            break

print(result)

# 격자에서 어떤 좌표를 기준으로 다른 좌표의 거리를 어떻게 저장하는게 좋을까?
# 저장하는 거리가 다른 좌표 기준으로는 달라지니까 ...

# DFS는 주변 좌표를 가다보니까, 돌아가는 경우가 더 긴 거리로 잡힌다.(맞네..)
# 그래서 그래프 기반은 BFS로 풀어줘야함

# 아 그냥 매번 초기화 해주면서 풀면 되는구나... 아하아하
# 그러니까 시간 초과가 나서, bfs_id를 visited[]에 넣어서 방문 확인하는 방법으로 해봄



