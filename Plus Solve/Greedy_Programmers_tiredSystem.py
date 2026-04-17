# 프로그래머스
# 완전탐색 / 피로도 시스템
# 백트래킹

# 각 던전마다 "최소 필요 피로도", "소모 피로도"
# 유저가 탐험할 수 있는 최대 던전 수 


# def solution(k, dungeons):
#     answer = -1

#     def recur(health, visited, remain):
#         nonlocal answer

#         if visited:
#             answer = max(answer, len(visited))

#         for i in range(0, len(remain)):
#             if health >= remain[i][0]: 
#                 recur(health - remain[i][1], 
#                       visited + [remain[i]],
#                       remain[:i] + remain[i+1:])

#     recur(k, [], dungeons)

#     return answer


def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    answer = 0

    def dfs(health, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(n):
            need, cost = dungeons[i]
            if visited[i] == False and health >= need:
                visited[i] = True
                dfs(health-cost, count+1)
                visited[i] = False
                # 선택을 반영한 상태로 내려갔다가(가능한 모든 경우의 수를 끝까지 탐색)
                # 돌아오면 선택을 복구해서 다른 경우를 탐색한다
                # 순열, 조합, 백트래킹

    dfs(k, 0)
    return answer


