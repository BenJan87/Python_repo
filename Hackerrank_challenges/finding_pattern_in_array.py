#checking pattern in given grid

def check(arr, pat, R, C, r, c):
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            if arr[i][j] == pat[0][0]:
                if com_check(arr, i, j, pat):
                    return "YES"
    return "NO"
                

def com_check(arr, i, j, pat):
    try:
        sliced = [el[j:len(pat[0])+j] for el in arr[i:i+len(pat)]]
    except IndexError:
        return False
    if sliced == pat:
        return True
    return False

def grid_input(R):
    arr = []
    for _ in range(R):
        tmp = []
        line = input()
        tmp[:0] = line
        arr.append(tmp)
    return arr

if __name__ == "__main__":
    # arr = [[1, 2, 3, 4], [5, 6, 7, 8], [8, 10, 11, 12], [13,14,15,16]]
    # pat = [[2, 4], [6, 7]]
    t = int(input())
    for _ in range(t):
        lst = list(map(int, input().split()))
        R = lst[0]
        C = lst[1]
        arr = grid_input(R)
        
        lst = list(map(int, input().split()))
        r = lst[0]
        c = lst[1]
        pat = grid_input(r)
        check(arr, pat)