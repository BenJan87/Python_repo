

def sliced(matrix, row, col): #i, j
    matrix = matrix[:row] + matrix[row+1:]
    new_m  = []
    for element in matrix:
        element = element[:col] + element[col+1:]
        new_m.append(element)
    return new_m


def det_mat(matrix):
    n = len(matrix)
    if n == 2:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
    elif n == 1:
        return matrix[0][0]
    # else:
    #     return sum([matrix[0][j]*((-1)**(2+j))*det_mat(sliced(matrix, 0, j)) for j in range(n)])   
    res = 0
    for j in range(n):
        res += matrix[0][j]*((-1)**(2+j))*det_mat(sliced(matrix, 0, j)) 
    return res

    










if __name__ == "__main__":
    matrix = [[1, 3, 5, 9], [1, 3, 1, 7], [4, 3, 9, 7], [5, 2, 0, 9]]
    print(det_mat(matrix))



