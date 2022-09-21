def sub(a, b):
    a, b = max(a, b), min(a, b)
    a_l, b_l = [], []
    len_a = len(str(a))
    for i in range(len_a):
        a_l.insert(0, get_digit(i+1, a))
        b_l.insert(0, get_digit(i+1, b))

    res, ten = [], 0
    for i in range(len_a):
        tmp = a_l[-i-1] + b_l[-i-1] + ten
        if tmp > 9:
            if i == len_a - 1:
                res.insert(0, tmp)
                break
            ten = 1
        else:
            ten = 0
        res.insert(0, tmp % 10)
    return list_into_num(res)

def list_into_num(lst):
    lst = list(map(str, lst))
    new = ""
    for element in lst:
        new += element
    return int(new)   

def get_digit(i, n):
    a = n % (10**i)
    res = a - a % (10**(i-1))
    res //= (10**(i-1))
    return res

def multi(a, b):
    a, b = max(a, b), min(a, b)
    a_l, b_l = [], []
    len_a = len(str(a))
    for i in range(len_a):
        a_l.insert(0, get_digit(i+1, a))
        b_l.insert(0, get_digit(i+1, b))

    to_add = []
    for i in range(len(str(b))):
        temp_list = []
        ten = 0
        for j in range(len(str(a))):
            tmp = a_l[-j-1] * b_l[-i-1] + ten
            if tmp > 9:
                if j == len(str(a)) - 1:
                    temp_list.insert(0, tmp)
                    break
                ten = get_digit(2, tmp)
            else:
                ten = 0
            temp_list.insert(0, tmp % 10)
        to_add.append((list_into_num(temp_list)) * (10**i))
    
    
    return adding_in_list(to_add)
        
def adding_in_list(arr):
    if len(arr) == 2:
        return sub(arr[0], arr[1])
    elif len(arr) == 1:
        return arr[0]

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]
    return sub(adding_in_list(left), adding_in_list(right))    

def factorial(a):
    if a == 0 or a == 1:
        return 1
    return multi(a, factorial(a-1))

if __name__ == "__main__":
    print(factorial(int(input())))