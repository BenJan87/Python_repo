def minimumLoss(arr_price) -> int:
    min_loss = 10 ** 16 + 1
    n = len(arr_price)

    for i in range(n - 1):
        for j in range(i + 1, n):
            difference = arr_price[i] - arr_price[j]
            if difference < 0:
                continue
            min_loss = min(difference, min_loss)
 
    return min_loss 


if __name__ == '__main__':

    n = int(input().strip())

    price = list(map(int, input().rstrip().split()))

    result = minimumLoss(price)

    print(result)