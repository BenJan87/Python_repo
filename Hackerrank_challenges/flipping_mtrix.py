#calculating the max sum in matrix (top right corner - size of n/2), when you can reverse the rows or columns


def best_of_4(matrix, i, j):
    n = len(matrix)
    return max(max(matrix[i][j], matrix[n-i-1][n-j-1]), max(matrix[i][n-j-1], matrix[n-i-1][j]))


def flippingMatrix(matrix):
    n = len(matrix) // 2
    count = 0
    for i in range(n):
        for j in range(n):
            count += best_of_4(matrix, i, j)
    
    return count


if __name__ == "__main__":
    matrix = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]

    print(flippingMatrix(matrix))