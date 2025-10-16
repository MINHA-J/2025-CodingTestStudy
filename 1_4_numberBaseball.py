TC = int(input())

hint = [list(map(int, input().split())) for _ in range(TC)]
result = 0

for a in range(1, 10):
    for b in range(0, 10):
        for c in range(0, 10):

            if (a==b or b==c or c==a):
                continue
            
            answerList = [a, b, c]
            answerCount = 0

            for arr in hint:
                number = arr[0]
                strike = arr[1] 
                ball = arr[2]

                numberList = [number//100, (number//10)%10, number%10]

                strike_count = 0
                ball_count = 0

                for i in range(3):
                    if numberList[i] == answerList[i]:
                        strike_count += 1
                    elif answerList.count(numberList[i]) > 0:
                        ball_count += 1

                if (strike_count == strike and ball_count == ball):
                    answerCount +=1

            if answerCount == TC:
                result += 1

print(result)


            



