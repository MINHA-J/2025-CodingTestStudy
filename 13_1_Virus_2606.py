# 2606 실버3

N = int(input())
M = int(input())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())

    graph[a].append(b)
    graph[b].append(a)


#--------- DFS ---------#
"""
visited = [0 for _ in range(N+1)]

def recur(node):
    visited[node] = 1

    for next in graph[node]:
        if visited[next] == 1:
            continue
        recur(next)

recur(1)
print(sum(visited)-1)
"""

#--------- BFS ---------#
visited = [0 for _ in range(N+1)]

from collections import deque

q = deque() #양방향 pop이 되는구만

# 위치에서 갈 수 있는 애들을 덱에 담는다.
q.append(1)

# 방문할 수 있는 것 다 방문하면 종료
while len(q) > 0:
    node = q.popleft()
    visited[node] = 1

    for next in graph[node]:
        if visited[next] == 1: continue
        q.append(next)

print(sum(visited)-1)
