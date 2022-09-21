from collections import Counter
    
def check_win(b):
    if b[0] != b[1] or b[-1] != b[-2]:
        return False
    for i in range(1, len(b) - 1):
        if b[i-1] != b[i] and b[i+1] != b[i]:
            return False
    return True
    
def happyLadybugs(b):
    if len(b) == 1:
        return "NO"
    if "_" not in b:
        if check_win(b):
            return "YES"
        return "NO"
    # bugs_count = Counter(b).most_common()
    bugs_count = sorted(Counter(b).most_common(), key = lambda x: x[1])
    if bugs_count[0] == "_" and len(bugs_count) == 1:
        return "NO"
    for el in bugs_count:
        if el[1] == 1 and el[0] != "_":
            return "NO"
        elif el[1] == 2:
            break
    return "YES"




if __name__ == "__main__":
    g = int(input())
    for g_itr in range(g):
        b = input()
        print(happyLadybugs(b))

