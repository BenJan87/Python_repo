#checking if in the lsit of strings(defined by k) elements are repeatable

def check_prev(s):
    rep = []
    for el in s:
        if el not in rep:
            rep.append(el)
    res = ""
    for el in rep:
        res += el
    print(res)

def merge_the_tools(s, k):
    s_list = []
    n = len(s)
    for i in range(n//k):
        s_list.append(s[i*k:(i+1)*k])

    for el in s_list:
        check_prev(el)


if __name__ == "__main__":
    s = input()
    print(len(s))
    k = int(input())
    merge_the_tools(s, k)