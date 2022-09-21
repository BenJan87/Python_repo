#encrypting by transforming the matrix with words
from math import sqrt, floor, ceil

def row_col(n):
    f, c = floor(sqrt(n)), ceil(sqrt(n))
    if f*c < n:
        return c, c
    return f, c

def splitting(s):
    s = s.replace(" ", "")
    r, c = row_col(len(s))
    
    str_list = []
    for i in range(r):
        str_list.append(s[i*c:(i+1)*c])
    tmp = s[(r)*c:]
    if len(tmp) > 0:
        str_list.append(tmp)

    return str_list, r, c

def rotate_print(arr, r, c):
    for j in range(len(arr[-1])):
        word = ""
        for i in range(r):
            word += arr[i][j]
        print(word, end=" ")

    for j in range(len(arr[-1]), c):
        word = ""
        for i in range(r-1):
            word += arr[i][j]
        print(word, end=" ")




    

if __name__ == '__main__':

    s = input()

    arr, r, c = splitting(s)
    print(arr) #debug
    rotate_print(arr, r, c)