arr = [list(map(int, input().split())) for _ in range(4)]
x1, y1, x2, y2 = map(int, input().split())

prefix = [[0 for _ in range(4)] for _ in range(4)]

for i in range(4):
    for j in range(4):
        prefix[i][j] += arr[i][j]
        if (i-1 >= 0):
            prefix[i][j] += prefix[i-1][j]
        if (j-1 >= 0):
            prefix[i][j] += prefix[i][j-1]
        if (i-1 >= 0 and j-1 >= 0):
            prefix[i][j] -= prefix[i-1][j-1]

print(prefix)

# 구간의 합
result = prefix[x2-1][y2-1] - prefix[x2-1][y1-2] - prefix[x1-2][y2-1] + arr[x1-2][y1-2]
print(result)