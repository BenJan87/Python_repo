def find_st(arr, i):
    while i != n - 1:
        if arr[i] > arr[i+1]:
            return i
        i += 1
    return -1
    
def find_nd(arr, i):
    while i != n - 1:
        if arr[i] < arr[i+1]:
            return i
        i += 1
    return -1
    
def check_sort(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False
    return True

def almostSorted(arr):
    cp = [el for el in arr]
    st = find_st(arr, 0)
    if st == -1:
        print("yes")
        return
    nd = find_nd(arr, st)
    if nd == -1:
        print("no")
        return

    if nd - st == 1:
        cp[st], cp[nd] = cp[nd], cp[st]

        st_2 = find_st(arr, st)
        nd_2 = find_nd(arr, st_2)

        cp[st], cp[st_2] = cp[st_2], cp[st]
        if find_st(cp, 0) == -1:
            print("yes")
            print("swap",st+1,st_2+1)
            return
            
    if find_st(arr[:st] + list(reversed(arr[st:nd+1])) + arr[nd+1:]) == -1:
        print("yes")
        print("reverse",st+1,nd+1)
        return

    
            
            
        
    

    
    
    
        
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    almostSorted(arr)
