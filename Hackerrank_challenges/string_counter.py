#printin the most 3 common letter in str(with also alphabetical order)

from collections import Counter


if __name__=="__main__":
    s = input()
    tmp = sorted(Counter(s).most_common(), key = lambda x: (-x[1], x[0]))

    for i in range(3):
        print(tmp[i][0], tmp[i][1])