# 프로그래머스
# 완전탐색 / 전력망을 둘로 나누기

# n개의 송전탑
# 전선 하나를 끊어서 2개로 네트워크를 분할
# 이때 전력망이 비슷한 규모로 나누어지도록

# 전력망이 가지고 있는 송전탑 개수의 차이(절대값)

def solution(n, wires):
    visited = [0] * (n+1)
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    answer = n

    for i in range(len(wires)):
        cut_v1, cut_v2 = wires[i]

        def dfs(node):
            # 방문 처리는 Dfs 진입 시 한다
            # 그래프 탐색
            visited[node] = True
            count = 1

            for next in graph[node]:
                if (cut_v1 == node and cut_v2 == next) or (cut_v2 == node and cut_v1 == next): continue
                
                if not visited[next]:
                    count += dfs(next)

            return count

        size = dfs(1)
        diff = abs(size - (n - size))  
        answer = min(diff, answer)    

    return answer