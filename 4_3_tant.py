N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort()
#print(arr)

# 텐트의 최대 높이 계산
max_idx = -1
max_height = -1
for i in range(N):
    if max_height < arr[i][1]: 
        max_idx = i
        max_height = arr[i][1]

# 앞에서부터~최대 높이까지
y_list = [0 for _ in range(N)]
max_try = 0
for idx in range(0, max_idx+1):
    if (max_try < arr[idx][1]):
        y_list[idx] = arr[idx][1]
        max_try = arr[idx][1]
    else:
        y_list[idx] = max_try
# 뒤에서부터~최대 높이까지
max_try = 0
for idx in range(N-1, max_idx, -1):
    if (max_try < arr[idx][1]):
        y_list[idx] = arr[idx][1]
        max_try = arr[idx][1]
    else:
        y_list[idx] = max_try
#print(y_list)

result = 1 * max_height
for idx in range(0, max_idx):
    x = (arr[idx+1][0] - arr[idx][0])
    y = y_list[idx]
    result += x*y
    #print("up: ", x, y)
for idx in range(N-1, max_idx, -1):
    x = (arr[idx][0] - arr[idx-1][0])
    y = y_list[idx]
    result += x*y
    #print("down: ", x, y)
print(result)




