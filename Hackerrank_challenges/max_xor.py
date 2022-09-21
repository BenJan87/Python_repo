def to_binary(n):
    temp = []
    if n != 0:
        while True:
            if n == 1:
                temp.append(1)
                break
            temp.append(n % 2)
            n = n // 2
    while len(temp) != 30:
        temp.append(0)
    x = ''.join(str(i) for i in temp)
    return x

def to_decimal(temp):
    integ = 0
    for i in range(30):
        if temp[i] == '1':
            integ += 2**i
    return integ

def xor(a, b):
    temp=''
    for i in range(30):
        if a[i] == b[i]:
            temp += '0'
        else:
            temp += '1'
    return temp

def max_xor(arr, q):
    for i in range(len(arr)):
        arr[i] = to_binary(arr[i])
    for i in range(len(q)):
        q[i] = to_binary(q[i])
    
    for i in range(len(q)):
        temp = 0
        for j in range(len(arr)):
            x = to_decimal(xor(q[i], arr[j]))
            temp = max(x, temp)
        print(temp)




if __name__ == "__main__":
    
    n = input()
    arr = list(map(int, input().split()))
    m = int(input())
    
    q = [0]*m
    for i in range(m):
        q[i] = int(input())

    max_xor(arr, q)
