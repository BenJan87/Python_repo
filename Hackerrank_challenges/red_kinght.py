#moving red knight in minimal moves


def even(s, t):
    return True if s % 2 == t % 2 else False
        
def sup_even(s, t):
    return True if s % 4 == t % 4 else False

def check_first(i_st, j_st, i_nd, j_nd):
    if not even(i_st, i_nd):
        print("Impossible")
        exit()
    if not even(j_st, j_nd) and sup_even(i_st, i_nd):
        print("Impossible")
        exit()
    if even(j_st, j_nd) and not sup_even(i_st, i_nd):
        print("Impossible")
        exit()

def min_move(a, b, p, q):
    #list priority 
    #UL, UR, R, LR, LL, L
    global count
    global res
    if p < a and q < b or p < a and b == q:
        count += 1
        res.append("UL")
        min_move(a-2, b-1, p, q)
    if p < a and q > b:
        count += 1
        res.append("UR")
        min_move(a-2, b+1, p, q)
    if a == p and q > b:
        count += 1
        res.append("R")
        min_move(a, b+2, p, q)
    if p > a and q > b or p > a and b == q:
        count += 1
        res.append("LR")
        min_move(a+2, b+1, p, q)
    if p > a and q < b:
        count += 1
        res.append("LL")
        min_move(a+2, b-1, p, q)
    if p == a and q < b:
        count += 1
        res.append("L")
        min_move(a, b-2, p, q)
    
        
if __name__ == "__main__":
    n = int(input()) #board size
    arr = list(map(int, input().split())) #i_st, j_st, i_nd, j_nd
    count = 0
    res = []
    i_st, j_st, i_nd, j_nd = arr[0], arr[1], arr[2], arr[3]

    check_first(i_st, j_st, i_nd, j_nd)
    min_move(i_st, j_st, i_nd, j_nd)
    print(count)
    print(*res)



