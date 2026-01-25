# 로봇 청소기 / 골드5

# 방 크기 N * M, 벽 또는 빈칸
# 로봇 방향 (0북, 1동, 2남, 3서)
# (0, 0) ~ (N-1, M-1)

# 아놔 변수 명 주의!!!!


N, M = map(int, input().split()) # N이 y임
ry, rx, rd = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

#   [북, 동, 남  서]
dy = [-1, 0, +1, 0]
dx = [0, +1, 0, -1]

# 주변 네 개의 칸 중 청소가 가능한 상태인지 확인
def checkNear(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if (0 <= ny < N) and (0 <= nx < M):
            if room[ny][nx] == 0:
                return True
    else:
        return False            

def counterclockwise(n):
     return (n - 1) % 4

CleanMode = True
result = 0

while (CleanMode):
    
    # 현재 칸 청소 확인, 청소
    if room[ry][rx] == 0:
        room[ry][rx] = 2
        result += 1

    # 주변 4칸 탐색
    #   청소 되지 않은 빈 칸이 있는 경우
    if checkNear(rx, ry):
        rd = counterclockwise(rd)
        ty = ry + dy[rd]
        tx = rx + dx[rd]
        # 반시계로 회전 + 청소되지 않았으면 한 칸 전진
        if room[ty][tx] == 0:
            rx = tx
            ry = ty
    #   청소 되지 않은 빈 칸이 없는 경우
    else:
        # 한 칸 후진 가능한지 확인
        bd = counterclockwise(counterclockwise(rd))
        by = ry + dy[bd]
        bx = rx + dx[bd]
        if room[by][bx] == 1:
            CleanMode = False
        else:
            rx = bx
            ry = by

print(result)