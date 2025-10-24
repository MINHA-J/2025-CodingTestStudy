
def isPrime(num):
    for i in range(2, sprt(num)):
        if (num % i) == 0:
            print("NO")
            break
        
    print("YES")

def main():
    TC = int(input())

    for i in range(TC):
        target = int(input())
        isPrime(target)
