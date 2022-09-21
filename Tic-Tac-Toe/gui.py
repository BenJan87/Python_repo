def graphic_m():
    matrix = [[" "]*7 for i in range(7)]
    for i in range(0, 7, 2):
        for j in range(0, 7, 2):
            matrix[i][j] = "+"
            try:
                matrix[i][j+1] = "-"
            except IndexError:
                pass
            try:    
                matrix[i+1][j] = "|"
            except IndexError:
                pass
    return matrix

def print_board(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()