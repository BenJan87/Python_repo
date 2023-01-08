

def biggerIsGreater(w):
    ls = []
    for el in w:
        ls.append(ord(el))

    return ls


if __name__ == "__main__":
    print(biggerIsGreater("ab"))
    print(biggerIsGreater("bb"))
    print(biggerIsGreater("abdc"))
    print(biggerIsGreater("dhck"))

    print(biggerIsGreater("dkhc"))
    print(biggerIsGreater("fedcbabcd"))





    