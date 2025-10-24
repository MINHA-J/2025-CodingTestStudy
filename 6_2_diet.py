# 19942
# N개의 식재료
#   단  탄  지  비
#   100 70  90  10    
# 조건을 만족하면서, 비용이 최소가 되는 경우

N = int(input())
mp, mf, ms, mv = map(int, input().split())
ingre = [list(map(int, input().split())) for _ in range(N)]

answerArr = []
tempArr = []
answerMoney = 100000000

def recur(idx):
    global answerMoney, answerArr

    if (idx == N):
        _mp = _mf = _ms = _mv = _mm = 0
        for t in tempArr:
            _mp += ingre[t][0]
            _mf += ingre[t][1]
            _ms += ingre[t][2]
            _mv += ingre[t][3]
            _mm += ingre[t][4]
        # 최소 영양소 조건 만족
        if _mp >= mp and _mf >= mf and _ms >= ms and _mv >= mv: 
            if _mm < answerMoney:
                answerMoney = _mm
                answerArr = tempArr[:]           # 갱신
            elif _mm == answerMoney:
                if not answerArr or tempArr < answerArr:  # 사전식 타이브레이크
                    answerArr = tempArr[:]
        return

    # 해당 인덱스 포함 노노
    recur(idx+1)

    # 해당 idx 사용
    tempArr.append(idx)
    recur(idx+1)
    tempArr.pop()
    
recur(0)

if (answerMoney == 100000000):
    print(-1)
else:
    print(answerMoney)
    print(*[x + 1 for x in answerArr])