# D-Day, 실버5
# 25년 12월 10일

# 오늘로부터 캠프가 끝날 때까지 며칠이나 남았는가

# 연수 % 4 == 0 이라면 윤년
# 100으로 나누어 떨어지는 해는 평년
# 400으로 나누어 떨어지는 해는 다시 윤년

# 만약 캠프가 1000년 이상 지속된다면, gg 출력
# 오늘이 2월 29일인 경우는 없음 X

ny, nm, nd = map(int, input().split())
fy, fm, fd = map(int, input().split())

leftDays = 0

commonYear = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if fy-ny > 1000:
    print("gg")
elif fy-ny == 1000 and fm >= nm and fd >= nd:
    print("gg")
else:
    sy, sm = ny, nm
    while sy <= fy:
        
        if (sy == fy) and (sm == fm):
            break

        temp = 0
        if (sy % 4 == 0 and sy % 100 != 0) or (sy % 400 == 0):
            temp = leapYear[sm] # 윤년
        else:
            temp = commonYear[sm] # 평년
        
        leftDays += temp
        #print(sy, sm, temp)
        sm += 1

        if sm > 12:
            sy += 1
            sm = 1

    # 시작한 달 날짜 빼주기
    leftDays -= nd
    # 끝나는 달 날짜 더해주기
    leftDays += fd
    print(f"D-{leftDays}")

