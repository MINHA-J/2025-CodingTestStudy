# N개의 물건
# K 무게
# 각 물건의 무게와 가치
# 배낭에 넣을 수 있는 물건들의 가치의 최댓값

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]

max_price = 0

def recur(idx, weight, price):
    global max_price

    if idx >= N or weight > K : return

    max_price = max(price, max_price)

    # 가방에 넣을 것
    recur(idx+1, weight+items[idx][0], price+items[idx][1])

    # 가방에 넣지 않고 다음으로
    recur(idx+1, weight, price)


recur(0, 0, 0)
print(max_price)

# 아 이렇게 풀면 통과는 안됨