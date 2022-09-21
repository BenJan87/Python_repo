from re import search
#printing found patterns (its indices)
def check(word, k):
    m = search(k, word)
    if m:
        while m:
            print("({0}, {1})".format(m.start(), m.end() - 1))
            word = word[:m.start()] + "_" + word[m.start()+1:] 
            m = search(k, word)
    else:
        print("(-1, -1)")

if __name__ == "__main__":
    word = "aaadaadaa"
    k = "aa"
    check(word, k)