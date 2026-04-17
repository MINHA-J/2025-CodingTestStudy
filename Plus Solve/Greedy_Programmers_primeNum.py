# 프로그래머스
# 완전탐색 / 소수찾기

# 종이조각으로 만들 수 있는 소수가 몇 개?

def IsPrimeNumber(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5) + 1):
        # ** 거듭제곱! 
        if n % i == 0: return False
    return True

def solution(numbers):
    memory = set()

    def recur(used, remaining):
        if used:
            memory.add(int(used))
            # 지금까지 만든 숫자, 하나의 후보이므로 저장하고 계속 붙여보자
            # 만약 여기에서 return 하면 한 자리 숫자만 만들고 끝내겠구나.
        
        for i in range(len(remaining)):
            recur(used+remaining[i],
                  remaining[:i] + remaining[i+1:])
    
    recur("", numbers)

    answer = 0
    for i in memory:
        if IsPrimeNumber(i): answer += 1
    # sum(1 for x in memory if IsPrimeNumber(x))
    return answer



