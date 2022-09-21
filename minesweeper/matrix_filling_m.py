from random import randint
def fill(mat, mode):
    n = len(mat)//2
    m = len(mat[0])//2

    if mode == 1:
        mines = 10
    elif mode == 2:
        mines = 40
    else:
        mines = 99

    bomb_count = 0
    bomb = u"\u058D"
    while bomb_count != mines:
        i = randint(0, n-1)
        j = randint(0, m-1)
        if mat[2*i+1][2*j+1] != bomb:
            mat[2*i+1][2*j+1]= bomb
            bomb_count += 1
    around_bomb_counting(mat, bomb)

    return mat, mines

def around_bomb_counting(mat, bomb):
    n = len(mat)//2
    m = len(mat[0])//2
    for i in range(1, n*2 + 1, 2):
            for j in range(1, m*2 + 1, 2):
                if mat[i][j] != bomb:
                    try:
                        if mat[i-2][j-2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i-2][j] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i-2][j+2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i][j-2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i][j+2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i+2][j-2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i+2][j] == bomb:
                            mat[i][j] += 1
                    except:
                        pass

                    try:
                        if mat[i+2][j+2] == bomb:
                            mat[i][j] += 1
                    except:
                        pass