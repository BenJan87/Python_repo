


def is_palindrome(s):
    n = len(s)
    for i in range(n//2):
        if s[i] != s[-i-1]:
            return False
    return True

def removing(s, i):
    n = len(s)
    str_list = []
    for k in range(n):
        if k != i:
            str_list.append(s[k])

    s = ""
    for element in str_list:
        s += element

    return s

def check(s):
    n = len(s)

    for i in range(n//2):
        if s[i] != s[-i-1]:
            if is_palindrome(removing(s, i)):
                return i
            if is_palindrome(removing(s, n-i-1)):
                return n - i - 1

    return -1

if __name__ == "__main__":
    a = "aaab"
    b = "baa"
    c = "aacbbccaa"

    for element in [a, b, c]:
        print(check(element))
    