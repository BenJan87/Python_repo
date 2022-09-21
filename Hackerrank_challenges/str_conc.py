def into_stack(a):
    stack = []
    for el in a:
        stack.append(el)
    return stack

def conc(a, b):
    res = ""
    len_min = min(len(a), len(b))
    a, b = into_stack(a), into_stack(b)
    
    while len(a) and len(b) > 0:
        if a[0] == b[0]:
            tmp_a = [el for el in a]
            tmp_b = [el for el in b]
            for i in range(len_min):
                tmp_a, tmp_b = tmp_a[1:], tmp_b[1:]
                try:
                    if tmp_a[0] == tmp_b[0]:
                        continue
                except:
                    if len(tmp_b) > 0:
                        res += b[0]
                        b.pop(0)
                        break
                    res += a[0]
                    a.pop(0)
                    break
                if tmp_a[0] < tmp_b[0]:
                    res += a[0]
                    a.pop(0)
                else:
                    res += b[0]
                    b.pop(0)
                break
        elif a[0] < b[0]:
            res += a[0]
            a.pop(0)
        else:
            res += b[0]
            b.pop(0)

    while len(a) > 0:
        res += a[0]
        a.pop(0)
    while len(b) > 0:
        res += b[0]
        b.pop(0)
    
    return res

def check(a, b):
    for i in range(len(a)):
        if a[i] != b[i]:
            return i
    return "noice"

if __name__ == "__main__":
    file = open('C:/Users/benja/OneDrive/Pulpit/Lol/input01.txt', 'r')
    n = int(file.readline()[:-1])
    for i in range(n):
        if i != n - 1:
            a = file.readline()[:-1]
            b = file.readline()[:-1]
        else:
            a = file.readline()[:-1]
            b = file.readline()
        print(conc(a, b))


    # n = int(input())
    # for _ in range(n):
    #     a = input()
    #     b = input()
    