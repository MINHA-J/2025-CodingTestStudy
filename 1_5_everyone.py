
# 1번 아이디어. 완전 탐색
'''
N = int(input())

positionList = [list(map(int, input().split())) for i in range(N)]

min_x = 0
min_y = 0

min_distance = 1000001

for try_x in range(1000001):
    for try_y in range(1000001):

        try_distance = 0
        for arr in positionList:
            x = arr[0]
            y = arr[1]

            try_distance += (abs(x-try_x) + abs(y-try_y))

        if (min_distance > try_distance):
            min_x = try_x
            min_y = try_y
            min_distance = try_distance

# N명 학생의 최소 거리 계산하기
for arr in positionList:
    x = arr[0]
    y = arr[1]

    print(abs(x-min_x) + abs(y-min_y))
'''

# 2번 아이디어
# 한 곳에서 모일 때, 비용을 최소화하기 위해서는
# 우리의 집 중 한 곳에서 모여보면 됨

# 3번 아이디어
# 최소 거리를 계산하고 싶다. 2명이 모여야한다
# 4명의 거리를 구한 뒤에, 가까운 순서대로 더한다 ??? 
# 짱구가 3명의 집에서 한 곳에 모일건데, 그 집에서 가장 가까운 2명을 불러서 놀겠다....

# 아 아이디어는 이해했는데, 구현이 아직 매끄럽지 못함 ...

N = int(input())

homeList = [list(map(int, input().split())) for _ in range(N)]

totalList = list()

for i in range(N):
    # 모일 집의 기준을 잡는다
    standard_x = homeList[i][0]
    standard_y = homeList[i][1]
    #print(standard_x, standard_y)

    # 기준으로부터의 거리 계산
    distanceList = list()
    for arr in homeList:
        x = arr[0]
        y = arr[1]
        distance = int(abs(standard_x-x) + abs(standard_y-y))
        distanceList.append(distance)

    totalList.append(distanceList)

print(totalList)

# 오름차순 정렬
totalList.sort()

# 1~N명씩 집에 모인다
answerList = [0, ]
for i in range(2, N+1):

    minDistance = 1000000

    for arr in totalList:
        tempDistance = 0
        for j in range(i):
            tempDistance += arr[j]
        if (minDistance > tempDistance):
            minDistance = tempDistance
    
    answerList.append(minDistance)

print(answerList)

# 백준에서 첫 케이스가 안 맞음
# 뭔가 더 이후에 한번 더 도전해보자