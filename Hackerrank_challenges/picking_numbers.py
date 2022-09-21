#pick the longest subarray, where abs value from any of the numbers in subarray is <= 1

from collections import Counter





def pickingNumbers(arr):
    arr = sorted(Counter(arr).most_common(), key=lambda x: (-x[1], x[0]))
    
    best = 0
    i = 0
    while i != len(arr) - 1:
        j = i + 1
        while j != len(arr):
            if abs(arr[i][0] - arr[j][0]) == 1:
                best = max(best, arr[i][1] + arr[j][1])
            j += 1
        i += 1
    return max(best, arr[0][1])
    









if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    # arr = [1, 1, 1, 5, 5, 4, 4, 7, 0]

    res = pickingNumbers(arr)
    print(res)


