#!/bin/python3

from math import sqrt

#description below
#https://www.hackerrank.com/challenges/alice-and-bobs-silly-game/problem?h_r=internal-search

def is_prime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i <= int(sqrt(n))+1:
        if n % i == 0:
            return False
        i += 2
    return True
        


def sillyGame(n):
    tup = [i for i in range(1, n+1)]
    length = len(tup)
    count = 0
    for i in range(length):
        for i in range(length):
            if is_prime(tup[i]):
                temp = tup[i]
                count += 1
                flag += 1
            else:
                
        end = tup[-1]
        i = 2
        while temp < end:
            try:
                tup.remove(temp)
            except:
                break
            temp *= i  
            i += 1
    return count
        
        
if __name__ == '__main__':

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        print(sillyGame(n))