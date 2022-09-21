#counting the surface of the 3D object with definied heights (the heith is always positive)


def north(arr, i, j):
    if i - 1 != -1:
        if arr[i][j] > arr[i-1][j]:
            return arr[i][j] - arr[i-1][j]
        else:
            return 0
    else:
        return arr[i][j]      
      
def south(arr, i, j):
    try:
        if arr[i][j] > arr[i+1][j]:
            return arr[i][j] - arr[i+1][j]
    except:
        return arr[i][j]      
    return 0
    
def west(arr, i, j):
    if j - 1 != -1:
        if arr[i][j] > arr[i][j-1]:
            return arr[i][j] - arr[i][j-1]
        else:
            return 0
    else:
        return arr[i][j]

def east(arr, i, j):
    try:
        if arr[i][j] > arr[i][j+1]:
            return arr[i][j] - arr[i][j+1]
    except:
        return arr[i][j]    
    return 0

def surfaceArea(arr, h, w):
    count = 0
    for i in range(h):
        for j in range(w):
            count += north(arr, i, j)
            count += south(arr, i, j)
            count += west(arr, i, j)
            count += east(arr, i, j)
    
    return count + 2*h*w



if __name__ == "__main__":
    h = int(input())
    w = int(input())

    arr = [[0]*w for i in range(h)]
    for i in range(h):
        for j in range(w):
            arr[i][j] = int(input())

    for i in range(h):
        print("\n")
        for j in range(w):
            print(arr[i][j], end=" ")

    print("\n\n", surfaceArea(arr, h, w))

