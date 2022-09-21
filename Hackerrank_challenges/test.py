
# def fibonacci(n):
#     if n == 1:
#         return 1
#     if n == 0:
#         return 0
#     return fibonacci(n-1) + fibonacci(n-2)
#     # Write your code here.

# n = int(input())
# print(fibonacci(n))
    

# def factorial(n):
#     if n == 1 or n == 0:
#         return 1
#     return n*factorial(n-1)

# print(factorial(150))
arr = [ '+-++++++++',
        '+-++++++++',
        '+-++++++++',
        '+DELHI++++',
        '+-+++-++++',
        '+-+++-++++',
        '+++++-++++',
        '++LONDON++',
        '+++++-++++',
        '+++++-++++']

words = ['ICELAND', 'ANKARA']

def find_len_hor(crossword, l, i, j, word):
    count = 0
    a, b = i, j

    while a != 10:
        b = j
        while b != 10:
            if crossword[a][b] == '-' or crossword[a][b] == word[count]:
                count += 1
                if count == l:
                    return a, b - l + 1
            else:
                count = 0
            b += 1
        a += 1
    return None, None #increment i
    
def find_len_ver(crossword, l, i, j, word):
    count = 0
    a, b = i, j
    while a != 10:
        b = j
        while b != 10:
            if crossword[b][a] == '-' or crossword[b][a] == word[count]:
                count += 1
                if count == l:
                    return a - l + 1, b 
            else:
                count = 0
            b += 1
        a += 1
    return None, None # increment j

def insert(crossword, word, i, j, par):
    length = len(word)
    a, b = i, j
    if par == 0: #hor
        while b != length:
            if crossword[a][b] == '-' or crossword[a][b] == word[b - j]:
                b += 1
            else:
                return 1, crossword
        b = j
        
        while b - j != length:
            crossword[a][b] = word[b - j]
            b += 1
    else:
        while a - i!= length:
            if crossword[a][b] == '-' or crossword[a][b] == word[a - i]:
                a += 1
            else:
                return 1, crossword
        a = i
        while a != length:
            crossword[a][b] = word[a - i]
            a += 1    
    return 0, crossword
            



def crosswordPuzzle(crossword, words):
    for i in range(10):
        temp = []
        temp[:0] = crossword[i]
        crossword[i] = temp

    temp = crossword
    x, i, j = 0, 0, 0
    insert_count = 0
    while x != len(words):
        was_in = 0
        word = words[x]
        a, b = find_len_hor(temp, len(word), i, j, word)
        if a is not None:
            res, temp = insert(temp, word, a, b, 0)
            if res == 0:
                insert_count += 1
                was_in = 1
            else:
                i += 1
        else:
            c, d = find_len_ver(temp, len(word), i, j, word)
            if c is not None:
                res, temp = insert(temp, word, c, d, 1)
                if res == 0:
                    insert_count += 1
                    was_in = 1
                else:
                    j += 1
        if c is None and d is None:
            
        x += 1
        if insert_count == len(words):
            return temp
            



print(crosswordPuzzle(arr, words))




