# 2644 (실버2)
# 여러 사람들에 대한 부모 자식들 간의 관계
# 주어진 두 사람의 촌수는?

# 전체 사람의 수 n ( < 100)
# 촌 수를 계산해야하는 사람의 번호 A, B
# 부모-자식 간의 관계 개수 m
# 부모-자식 간의 관계 x, y
from collections import deque

numTotal = int(input())
targetA, targetB = map(int, input().split())
numFamily = int(input())
array = [list(map(int, input().split())) for _ in range(numFamily)]
# x 부모 번호, y 자식 번호
# 각 사람의 부모는 최대 한 명만 주어짐

result = -1 # 관계가 없으면 -1

graph = list([] for _ in range(101))
visited = [0]*101
distance = [0]*101

for idx in range(numFamily):
    p = array[idx][0]
    c = array[idx][1]

    graph[p].append(c)
    graph[c].append(p)


q = deque()
q.append(targetA)
result = -1

while (len(q) > 0):

    curr = q.popleft()
    if (curr == targetB):
        result = distance[curr]
        break
    if visited[curr] == 1: continue
    visited[curr] = 1

    for next in graph[curr]:
        q.append(next)
        distance[next] = distance[curr] + 1

#print(visited)
print(result)
