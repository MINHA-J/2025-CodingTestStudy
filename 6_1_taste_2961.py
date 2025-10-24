# N개의 재료
# 신맛 S(곱), 쓴맛 B(합)
# 재료는 적어도 하나 사용
# 신맛과 쓴맛의 차이가 가장 작은 요리를 만들어라

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = 1000000000

temp_arr = []

def recur(startIdx, cur, total):
    global answer
    
    if (cur == total):
        temp_S = 1
        temp_B = 0
        for i in temp_arr:
            temp_S *= i[0]
            temp_B += i[1]
        if (abs(temp_S-temp_B) < answer):
            answer = abs(temp_S-temp_B)
        return
    
    for i in range(startIdx, N):
        temp_arr.append(arr[i])
        recur(i+1, cur+1, total)
        temp_arr.pop()

for num in range(1, N+1):
    recur(0, 0, num)

print(answer)


# 아니 미친!!
# 2가지 경우의 수를 다 담아준다고 생각하고
# 완전탐색적으로 잘 접근하니까 재귀 완전 깔끔하네 ...
'''
def recur(idx, dan, zzan, use):
    global answer
    if (idx == N): 
        if (use == 0): return 
        result = abs(dan - zzan)
        answer = min(answer, result)
        return

    # 해당 idx의 재료를 사용한 경우
    recur(idx+1, dan * arr[idx][0], zzan+arr[idx][1], use+1)

    # 해당 idx의 재료를 사용하지 않은 경우
    recur(idx+1, dan, zzan, use)

answer = 9999999999999
recur(0, 0, 1, 0)
'''