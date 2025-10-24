
def main():
    total = int(input())

    possible = 0

    for a in range (0, total+1):
        for b in range (0, total+1):
             for c in range (0, total+1):
                 if (a+b+c == total) \
                 and (a - b >= 2) \
                 and (a != 0) and (b != 0) and (c != 0) \
                 and (c % 2 == 0):
                     possible = possible + 1
                     print("%d, %d, %d", a, b, c)

    print("정답: ")
    print(possible)
                     
if __name__ == "__main__":
    main()


