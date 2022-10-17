import sys

print('Ładowanie modułu "{0}"'.format(__name__))

############################################

def wypisz(dict1):
    print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
    for number,count in dict1.items():
        print(f"{number}:{count},", end="")

def zapisz(dict1, argv):
    print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
    for number in argv[1:]:
        if number not in dict1:
            dict1[number] = 1
        else:
            dict1[number] += 1

    return dict1
############################################

print('Załadowano moduł "{0}"'.format(__name__))
if __name__ == "__main__":
    slownik = {}
    slownik = zapisz(slownik, sys.argv[1:])
    wypisz(slownik)