#returning the number of different words and the count of them

from collections import Counter




def counting(words):
    words = dict(Counter(words))
    
    print(len(words))
    counts = []
    for el in words:
        counts.append(words.get(el))
    print(*counts)






if __name__ == "__main__":
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())

    counting(words)