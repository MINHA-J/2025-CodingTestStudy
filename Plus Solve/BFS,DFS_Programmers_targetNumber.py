# BFS/DFS
# 타겟넘버

# n개의 정수 numbers
# 빼거나 더해서 타겟넘버 target를 만들자
# 타겟 넘버를 만드는 방법의 수

def solution(numbers, target):
    n = len(numbers)

    def dfs(idx, sum):
        answer = 0
        if idx == n:
            if sum == target:
                return 1
            else:
                return 0
        
        answer += dfs(idx+1, sum + numbers[idx])
        answer += dfs(idx+1, sum + (numbers[idx]*-1))

        return answer

    return dfs(0, 0)