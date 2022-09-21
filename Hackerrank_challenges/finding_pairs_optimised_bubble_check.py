#how many are there pairs with difference "k"

def pairs(k, arr):
    l = len(arr)
    i ,j, count = 0, 0, 0
    
    while i != l - 1:
        j = i + 1
        while j != l:
            if abs(arr[i] - arr[j]) == k:
                count += 1
            j += 1
        i += 1
    print(count)
    
if __name__ == '__main__':
    

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)