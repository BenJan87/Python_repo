def graphic_m(n, m):
    matrix = [[0]*(2*m+1) for _ in range(2*n+1)]
    for i in range(0, 2*n+1, 2):
        for j in range(0, 2*m+1, 2):
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
    print("  1", end="")
    for j in range(len(mat[0])//2 - 1):
        pass
    print()
    for i in range(len(mat)):
        # if i % 2 == 0:
        #     print("  ", end=" ")
        # else:
        #     if i//2 + 1 < 10:
        #         print(i//2 + 1, "", end = " ")
        #     else:
        #         print(i//2 + 1, end = " ")
        for j in range(len(mat[0])):
            print(mat[i][j], end=" ")
        print()