A, B = map(int, input().split())
arr = list(map(int, input().split()))

# 누적합 배열
prefix = [ 0 for _ in range(A)]

prefix[0] = arr[0]
for i in range(1, A):
    prefix[i] = prefix[i-1] + arr[i]

print(prefix)

answer = []

for i in range(B, A):
    answer.append(prefix[i]-prefix[i-2])

print(answer)
print(max(answer))