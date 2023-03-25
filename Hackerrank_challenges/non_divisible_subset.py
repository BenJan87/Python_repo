def nonDivisibleSubset(k: int, s: list) -> int:
    
    if k == 1 or len(s) == 1:
        return 1 # weird hackerrank assumption

    divisiors = [0]*k
    for el in s:
        divisiors[el % k] += 1

    if k == 2:
        if divisiors[0] > 0 and divisiors[1] > 0:
            return 2
        return 0 # same here as in first 'if'
    

    left = divisiors[1:int(k/2)+1] if k % 2 == 1 else divisiors[1:int(k/2)]
    right = list(reversed(divisiors[int(k/2)+1:]))

    len_subset = len(left)
    count_length = 0
    for i in range(len_subset):
        count_length += max(left[i], right[i])

    if divisiors[0]:
        count_length += 1

    if k % 2 == 0 and divisiors[int(k/2)]:
        count_length += 1

    return count_length


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
    print(result)
