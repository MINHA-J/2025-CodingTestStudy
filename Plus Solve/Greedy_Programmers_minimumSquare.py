# 프로그래머스
# 완전탐색 / 최소직사각형

# 모든 명함을 수납할 수 있는 가장 작은 지갑 만들기
def solution(sizes):
    inputList = sizes

    # x 가로, y 세로
    x_max = 0
    y_max = 0

    for l in inputList:
        if l[0] < l[1]:
            lx = l[0]
            ly = l[1]
        else:
            lx = l[1]
            ly = l[0]

        if lx > x_max : x_max = lx
        if ly > y_max : y_max = ly

    print(x_max, y_max)
    return x_max * y_max

# 2. 로컬 테스트를 위한 코드
if __name__ == "__main__":
    # 프로그래머스 문제의 예시 입력을 직접 변수에 할당
    test_sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]
    
    # 함수 실행 및 결과 출력
    result = solution(test_sizes)
    print(f"결과: {result}")

# case1
# 50 60
# 30 70
# 30 60
# 40 80

# 30 60
# 30 70
# 40 80
# 50 60


# case2
# 7 10
# 3  12
# 8 15
# 7 14
# 5 15

# 3 12
# 5 15
# 7 10
# 7 14
# 8 15


"""
이렇게 간략하게 표현할 수 있음

def solution(sizes):
    row = 0
    col = 0
    for a, b in sizes:
        if a < b:
            a, b = b, a
        row = max(row, a)
        col = max(col, b)
    return row * col
"""