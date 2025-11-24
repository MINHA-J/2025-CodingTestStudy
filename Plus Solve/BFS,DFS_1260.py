# 1260번, DFS와 BFS (실2)

# 정점 개수, 간선 개수, 탐색을 시작할 정점 번호
N, M, V = map(int, input().split())
M_list = [list(map(int, input().split())) for _ in range (M)]

# 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있음
# 입력으로 주어지는 간선은 양방향
# graph = [[]] * (M+1) #헐 이렇게 하면 얕은 복사라서 안되는구나!
graph = [[] for _ in range (N+1)]

for i in M_list:
    a = i[0]
    b = i[1]
    graph[a].append(b)
    graph[b].append(a)

# 다음 요소를 기준으로 정렬
for i in range(1, N+1):
    graph[i].sort()

def DFS(n, idx):
    if (visited[n] == idx):
        return
    
    visited[n] = idx
    dfs_result.append(n)
    
    for next in graph[n]:
        DFS(next, idx)
    
    
visited = [0] * (N+1)
dfs_result = []
DFS(V, 1)

from collections import deque
q = deque()
q.append(V)

visited = [0] * (N+1)
bfs_result = []

while (len(q) > 0):
    i = q.popleft()
    if visited[i] == 1: continue
    
    visited[i] = 1
    bfs_result.append(i)

    for next in graph[i]:
        if visited[next] != 0: continue
        q.append(next)

print(*dfs_result)
print(*bfs_result)

