from math import sqrt

def prime(n):
    if n == 2 or n == 5:
        print("Prime")
        return
    if n % 2 or n == 1:
        print("Not prime")
        return
    i = 3
    while i < sqrt(n):
        if n % i == 0:
            print("Not prime")
            return
        i += 2
    print("Prime")
        










if __name__ == "__main__":
    c = int(input())

    for _ in range(c):
        l = int(input())
        prime(l)
    