
arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
n = 3

def diagonalDifference(arr):
    global n
    le_ri = 0
    ri_le = 0
    for i in range(n):
        le_ri += arr[i][i]
        ri_le += arr[i][n-i-1]
    
    return abs(le_ri - ri_le)


print(diagonalDifference(arr))