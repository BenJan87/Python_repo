from operator import mod


def op_check(best, num):
    dif = abs(best - num) % 5
    if dif == 0:
        return 0
    if dif == 1 or dif == 2:
        return 1
    return 2

def op_between_num(a, greater):
    count = 0
    while greater - a >= 5:
        count += 1
        a += 5
    return count + op_check(greater, a)


def equal(n, arr):
    i, count = 0, 0
    arr.sort()
    while True:
        if arr[i] == arr[i+1]:
            i += 1
        else:
            greater, less = max(arr[i], arr[i+1]), min(arr[i], arr[i+1]) 
            count += op_between_num(less, greater)





if __name__ == "__main__": 
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        print(equal(n, arr))
