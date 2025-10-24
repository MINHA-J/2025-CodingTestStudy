# N+1일에 퇴사할 것

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

max_money = 0

def recur(day, curr_money):
    global max_money

    if day >= N:
        max_money = max(curr_money, max_money)
        return
    
    max_money = max(curr_money, max_money)
    
    # 일 하는 것을 선택하는 경우
    next_day = day+arr[day][0]
    if (next_day <= N):
        recur(next_day, curr_money+arr[day][1])

    # 일 하지 않는 것을 선택하는 경우
    recur(day+1, curr_money)

recur(0, 0)
print(max_money)