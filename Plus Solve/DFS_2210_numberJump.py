# 2210번, 숫자판 점프

# 5*5 크기의 숫자판, 0~9까지의 숫자
# 서로 다른 여섯 자리의 수들의 개수를 구하는 프로그램

import sys
sys.setrecursionlimit(900000)

array = [list(input().replace(" ", "")) for _ in range(5)]


dx = [0, 0, -1, +1]
dy = [-1, +1, 0, 0]

results = []
saved = [[[] for _ in range(5)] for _ in range(5)]
total = 0

# numStr 현재 좌표까지 만들어진 숫자열
# 현재 좌표 x, y. 
#   지금까지의 숫자열을 확인하고 (완성되었는지)
#   상하좌우로 이동한다
def recur(numStr, x, y):
    
    # 숫자판이 5*5라서, 메모리제이션 굳이 필요 없음
    #  들러봤다
    if (numStr in saved[y][x]):
        return 0
    else:
        saved[y][x].append(numStr)

    # 6자리 수가 다 모였다면
    if len(numStr) == 6:
        # set() 으로 중복만 제거할 수도 있겠네 아항..
        if not numStr in results:
            results.append(numStr)
            #print(numStr)
            return 1
        return 0

    canMake = 0    
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]

        # 좌표 범위 내에서 이동 가능하다면
        if 0 <= nx < 5 and 0 <= ny < 5:
            tempStr = numStr + array[ny][nx]
            canMake += recur(tempStr, nx, ny)

    return canMake

for y in range (5):
    for x in range (5):
        # 첫 입력 조건과 recur 조건 일치 잘 시켜주기
        total += recur(array[y][x], x, y)

print(len(results))
    
            
        
