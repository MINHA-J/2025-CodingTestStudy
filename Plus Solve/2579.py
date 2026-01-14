# 2579 / 계단오르기 / 실버3

# 1 또는 2 계단 오르기 가능
# 연속된 3개의 계단 오르기 불가능 (시작점은 계단x)
# 마지막 도착 계단은 반드시 밟아야

# 얻을 수 있는 총 점수의 최댓값

N = int(input())
stairs = list(0 for i in range(N+1))
for i in range(1, N+1):
    stairs[i] = int(input())

savePoints = list(0 for i in range(N+1))

def recur(i, stair_num):

    if stair_num == 3 or i > N:
        savePoints[i] = -99999999999
        return savePoints[i]
         
    if i == N:
        return stairs[i]
    
    # 한 칸 움직이기
    if i+1 <= N:
            savePoints[i] = max(savePoints[i], stairs[i]+ recur(i+1, stair_num+1))
    
    # 두 칸 움직이기
    if i+2 <= N:
        savePoints[i] = max(savePoints[i], stairs[i]+ recur(i+2, 1))

    return savePoints[i]

result = recur(0, 0)
print(*savePoints)
print(result)