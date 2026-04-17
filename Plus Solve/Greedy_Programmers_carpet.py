# 프로그래머스
# 완전탐색 / 카펫

# 노란색, 갈색으로 색칠된 격자의 개수
# 전체 카펫의 크기?


# 2
#   1, 2 > 2+4+4
# 1 > 2+2+4
# 24
#   6 4 > 8 6 4

def solution(brown, yellow):

    # 약수 탐색은 n 제곱근까지만 보면 충분함
    for y in range(1,  int(yellow**0.5) + 1):
        if yellow % y != 0: continue
        x = yellow//y

        if (x*2) + (y*2) + 4 == brown:
            return [x + 2, y + 2]