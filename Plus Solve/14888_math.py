# 백준 14888 실버1 연산자 끼워넣기


N = int(input())
numbers = list(map(int, input().split()))
# 덧셈 / 빨셈 / 곱셈 / 나눗셈
operators = list(map(int, input().split()))

result_min = 1000000000
result_max = -1000000000


def recur(plus, minus, multiply, division, idx, result):
    
    global result_min, result_max
    # 인덱스
    if idx >= N: 
        result_min = min(result_min, result)
        result_max = max(result_max, result)
        return

    num = numbers[idx]

    if plus < operators[0]:
        recur(plus+1, minus, multiply, division, idx+1, result+num)
    if minus < operators[1]:
        recur(plus, minus+1, multiply, division, idx+1, result-num)
    if multiply < operators[2]:
        recur(plus, minus, multiply+1, division, idx+1, result*num)
    if division < operators[3]:
        if result < 0: d = (result * -1) // num * -1
        else: d = result // num
        recur(plus, minus, multiply, division+1, idx+1, d)

recur(0, 0, 0, 0, 1, numbers[0])

print(result_max)
print(result_min)