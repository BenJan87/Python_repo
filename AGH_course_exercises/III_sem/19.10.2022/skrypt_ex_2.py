import re

def recognize_string(word):
    res = []
    while word:
        flag = 0

        if word[0] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            pattern = re.search("[0-9]+", word)
            flag = 1
        else:
            pattern = re.search("[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ]+", word)
            
        st, nd = pattern.start(), pattern.end()

        if flag == 0:
            res.append(f"Wyraz: {word[st:nd]}")
        else:
            res.append(f"Liczba: {word[st:nd]}")
        word = word[nd:]
    
    return res

        
if __name__ == "__main__":
    words = input().split()
    for word in words:
        print("\n", word)
        result = recognize_string(word)
        for el in result:
            print(el)