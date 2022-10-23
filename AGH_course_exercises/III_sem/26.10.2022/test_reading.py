file = open("file.txt", "r")

for el in file.readlines():
    print(el, end="")