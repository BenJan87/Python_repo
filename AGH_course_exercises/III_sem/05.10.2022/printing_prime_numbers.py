from math import sqrt
from sys import argv

def prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1 or n < 0:
        return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True
    
if __name__=="__main__":
    for number in argv:
        try:
            number = int(number)
            if prime(number):
                print(number)
        except:
            continue