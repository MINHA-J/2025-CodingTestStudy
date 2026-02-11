# 2667 / 단지번호붙이기 / 실버1
# 2026-02-11

# 정사각형 지도
# 1 집 있음 / 0 집 없음
# 상하좌우 >> 연결됨

from collections import deque

N = int(input())
Village = [list(map(int, input().strip())) for _ in range(N)]
Visited = [[0 for _ in range(N)] for _ in range(N)]

# 상 하 좌 우
dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]
answer = []

for y in range (N):
    for x in range (N):
        # 집이 있고, 아직 방문하지 않은 경우
        if Village[y][x] != 0 and Visited[y][x] != -1:
            num = 0
            d = deque()
            d.append([x, y])
            Visited[y][x] = -1
            
            while (len(d) > 0):
                tx, ty = d.popleft()
                num += 1 
                for i in range(4):
                    nx = tx + dx[i]
                    ny = ty + dy[i]
                    if 0 <= nx < N and 0 <= ny < N and Village[ny][nx] != 0 and Visited[ny][nx] != -1:
                        Visited[ny][nx] = -1
                        d.append([nx, ny])
            answer.append(num)

answer.sort()
print(len(answer))
print(*answer, sep='\n')
                
            
