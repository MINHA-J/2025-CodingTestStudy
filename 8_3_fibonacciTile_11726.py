# 2*N 크기의 직사각형
# 1*2, 2*1 크기의 타일로 채우는 방법의 수

N = int(input())

result = 0

# 이걸 어떻게 DP로 풀지?

# 일단 기본적으로 1*2로 채울 수 있는데
# ( 2개의 2*1 ) 묶음으로 ( 2개의 1*2 )를 대체할 수 있고
# N - ( 2개의 1*2 )*? 사이에 ?개의 ( 2개의 2*1 ) 넣기 경우의 수가 발생함

# 뭔가 쪼개서 생각하면 될 것 같은데..

#dp[1] = 1
#dp[2] = 2 # dp[1]+1
#dp[3]. 1+1+1, 1+2, 2+1 > 3
#dp[4]. > 6
#dp[5]  > 8

array = [1] * (N+1)

for i in range(1, N):
    array[i+1] = ((i+1) * array[i])

#print(array)

# 2*1로 다 채우는 경우의 수
if N >= 1:
    result += 1

# 2*1 *2로 다 채우는 경우의 수 (짝수이면)
if N > 1 and N%2 == 0:
    result += 1

# 2*1 *2를 하나씩 증가시키면서 경우의 수 세기
setBlock = 1
while (N - setBlock*2 >= 1):

    # 경우의 수 계산하기
    leftBlock = N - setBlock*2
    cur = (array[setBlock+leftBlock] // (array[leftBlock] * array[setBlock])) % 10007
    result += cur
    #print("set block ", setBlock, "일 때, ", cur)
    
    setBlock += 1


print(result % 10007)

