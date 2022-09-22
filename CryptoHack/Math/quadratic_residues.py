def check_quadratic(a, p):
    for i in range(p):
        if i**2 % p == a:
            return i
    return None

if __name__ == "__main__":
    p = 29
    ints = [14, 6, 11]
    for el in ints:
        res = check_quadratic(el, p)
        if res:
            print(res)