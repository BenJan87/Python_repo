
def divisible_sum_pairs(n, k, arr) -> int:
    #return number of pairs
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if (arr[i] + arr[j]) % k == 0:
                count += 1

    return count





if __name__ == "__main__":

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = divisible_sum_pairs(n, k, arr)

    print(result)