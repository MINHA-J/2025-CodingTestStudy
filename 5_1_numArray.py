'''
자연수 N과 M이 주어졌을 때, 길이가 M인 수열을 모두 구하는 프로그램을 작성하세요.
- 1부터 N까지의 자연수 중에서 M개를 고른 수열
- 1부터 N까지의 자연수 중에서 중복 없이 M개를 고른 수열
- 1부터 N까지의 자연수 중에서 중복 없이 오름차순으로 M개를 고른 수열
- 1부터 N까지의 자연수 중에서 중복 없이 내림차순으로 M개를 고른 수열
'''

N, M = map(int, input().split())
arr = []

# for i in range(1, N+1):
#     for j in range(1, N+1):
#         for k in range(1, N+1):

def recur(num):
    if (num == M):
        print(*arr)
        return
    
    for i in range(1, N+1):
        arr.append(i)
        recur(num+1)
        arr.pop() # return하고 돌아올 때는 array 한번 비워줘야 하니까

recur(0)

# array에 중복 없이 들어가게 하려면?
# > 체크하는 array를 두고, 있으면 넘어가도록
# 아래와 같이 하면 되는구나 호.
# if i in arr:
#    continue