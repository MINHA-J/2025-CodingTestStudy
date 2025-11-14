# N+1일에 퇴사할 것

'''
N = int(input())
interview = [list(map(int, input().split())) for _ in range(N)]

# idx일부터 끝까지의 최대 수익
def recur(idx):
    global answer

    if idx == N-1:
        return 0
    if idx > N-1:
        return -9999999999999
    if dp[idx] != -1: # 이미 저장되었다면
        return dp[idx]
    
    # 상담을 받거나 / 받지 않거나
    # 둘 중에서 더 큰 값을 기억한다
    dp[idx] = max(recur(idx+interview[idx][0]) + interview[idx][1], 
                  recur(idx+1))
    
    return dp[idx]
    

dp = [-1 for _ in range(N+1)]
# i일차부터 마지막 날까지 벌 수 있는 최대 수익
recur(0)
print(dp[0])
'''

N = int(input())

table = [[] for _ in range(N)]
for i in range(N):
    a, b = map(int, input().split())
    table[i] = [a, b]

dp = [0 for _ in range(N+1)]


for idx in range(N)[::-1]:
    # 작업 일이 출근 가능 날짜를 넘기는 경우
    if idx + table[idx][0] > N:
        dp[idx] = dp[idx+1]
    # 그렇지 않다면
    else:
        # 해당 일을 해서 얻을 수 있는 수익 + 이후 날짜에 저장된 최대 수익
        # 그 다음 날짜에 저장된 최대 수익을 얻는 것 중
        # 더 큰 것을 선택한다.
        dp[idx] = max(dp[idx+table[idx][0]] + table[idx][1],
                      dp[idx+1])

print(dp)
print(dp[0])




