# 물건의 수 A
# 베낭의 무게 B
A, B = map(int, input().split())

items = [list(map(int, input().split())) for _ in range(A)]
# {무게, 가치}

dp = [[0] * (B+1) for _ in range(A+1)]
# 앞에서부터 y개의 물건만 고려해서,
# 가방 허용 무게가 x일 때 얻을 수 있는 최대 가치

for _y in range(1, A+1):

    weight = items[_y-1][0]
    value = items[_y-1][1]

    for _x in range(1, B+1):

        # 물건을 담을 수 없다면
        if (_x < weight):
            dp[_y][_x] = dp[_y-1][_x] # 이전의 상태를 유지함
        else:
            # 물건을 담을 수 있을 때, 담을래 / 말래
            # 이전 개수의 물건까지 저장된 max 값 vs.
            # weight는 깎이지만 value 더해진 값
            dp[_y][_x] = max(dp[_y-1][_x], 
                           dp[_y-1][_x-weight]+value)

print(dp[A][B])


'''
def recur(num, weight):

    # 가방의 무게를 넘는 경우 return
    if weight > B:
        return -99999
    
    # A개의 물건이 다 담겼을 경우 return
    if num == A:
        return 0
    
    # 저장된 데이터가 있다면
    if dp[num][weight] != -1:
        return dp[num][weight]
    
    # 물건을 넣을 거야
    dp[num][weight] = max(recur(num+1, weight+items[num][0]) + items[num][1],
                          recur(num+1, weight))
    
    return dp[num][weight]
'''

