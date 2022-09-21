from random import randint

def phone(n):
    for i in range(n):
        tmp = ""
        for k in range(9):
            tmp += str(randint(0, 9))
        print(tmp)


def rand_names(n):
    for i in range(n):
        pass