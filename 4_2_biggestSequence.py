N = int(input())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N)]
prefix[0] = arr[0]
for i in range(1, N):
    prefix[i] = prefix[i-1] + arr[i]

# 연속된 몇 개의 수를 선택해서 구할 수 있는 합 중,
# 가장 큰 합을 구하라

print(prefix)

#------ 1차 시도. 앞에서 최소값, 뒤에서 최대값 탐색하고 있었는데, 잘 안 된다. ------#
# min_value = prefix[0]
# max_value = prefix[N-1]

# min_try_index = 1
# max_try_index = N-2

# while (min_try_index < max_try_index and \
#        min_try_index < N and max_try_index > 0):

#     if prefix[min_try_index] < min_value:
#         min_value = prefix[min_try_index]
         
#     if prefix[max_try_index] > max_value:
#         max_value = prefix[max_try_index]

#     min_try_index += 1          
#     max_try_index -= 1

#------- 강의 풀이 ------#
# 누적합 연산하면서, 이득이 되는 방향이 아니면 더해주지 않는다. 오....
