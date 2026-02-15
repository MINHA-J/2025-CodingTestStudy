# 3273번 / 두수의 합 / 실버3
# 투포인터와 정렬

N = int(input())
numArr = list(map(int, input().split()))
target = int(input())

head = 0
tail = N-1

numArr.sort()

answer = 0
while (head < tail):

    head_num = numArr[head] 
    tail_num = numArr[tail]
    
    # 더하는 숫자가 target 보다 클 수는 없으므로
    if tail_num >= target:
        tail -= 1
        continue
    
    if head_num + tail_num == target:
        head += 1
        tail -= 1
        answer += 1
    elif head_num + tail_num < target:
        head += 1
    elif head_num + tail_num > target:
        tail -= 1

print(answer)
