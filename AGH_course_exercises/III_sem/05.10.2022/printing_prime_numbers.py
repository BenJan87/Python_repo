from math import sqrt
from sys import argv


def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    i = 3
    sq_root = sqrt(n)
    while i <= sq_root:
        if n % i == 0:
            return False
        i += 2
    return True
    

if __name__=="__main__":
    for number in argv:
        if number.isdigit() and prime(int(number)):
            print(number)