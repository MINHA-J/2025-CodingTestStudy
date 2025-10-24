TC = int(input())
hint = [list(map(int, input().split())) for _ in range(TC)]

answer = []
result = 0

def find_answer(number):
    global result

    # 숫자 3개 다 모이면
    if (number == 3):
        for h in hint:
            hintNum = [h[0]//100, (h[0]//10)%10, h[0]%10]
            strikeNum = 0
            ballNum = 0
            # check number of strike and ball
            for i in range(3):
                if hintNum[i] == answer[i]:
                    strikeNum += 1
                elif hintNum[i] in answer:
                    ballNum += 1
            if strikeNum != h[1] or ballNum != h[2]:
                return
        result += 1
        #print(*answer)
        return
        
    for i in range(1, 10):     
        if (i in answer):
             continue
        answer.append(i)
        find_answer(number+1)
        answer.pop()

find_answer(0)
print(result)

# 아하.. 힌트를 돌면서 
# 힌트 index를 주고 현재 숫자랑 맞춰서 통과하면, 다음 힌트로
# 마지막 힌트라면, 한번 올리기.
# 아니면 index 처음으로 돌아가고, 현재 숫자 +1