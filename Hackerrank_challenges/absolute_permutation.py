#creating the list form 1 to n (started on 1 index) and find if there is any arr where |arr[i]-i| = k 

def absolutePermutation(n, k):
    arr = set([i+1 for i in range(n)])
    cp = []
    i = 1
    while i != n + 1:
        if i - k in arr:
            arr.remove(i-k)
            cp.append(i-k)
            i += 1
        elif k + i in arr:
            arr.remove(k+i)
            cp.append(k+i)
            i += 1
        
        else:
            print("-1")
            return
    
    print(*cp) 
    
        
if __name__ == '__main__':

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        absolutePermutation(n, k)
