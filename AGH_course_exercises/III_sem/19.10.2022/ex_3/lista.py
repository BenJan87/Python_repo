import sys
from collections import Counter


print('Ładowanie modułu "{0}"'.format(__name__))

#########################################

# def wypisz(arr):
#     print('Wywołano funkcję "wypisz()" modułu "{0}"'.format(__name__))
#     for el in arr:
#         if el == arr[-1]:
#             print(f"{el[0]}:{el[1]}")
#         else:
#             print(f"{el[0]}:{el[1]},", end="")

# def zapisz(arr):
#     print('Wywołano funkcję "zapisz()" modułu "{0}"'.format(__name__))
#     return Counter("".join(arr)).most_common()

def wypisz(arr):
    i = 0
    while i < len(arr):
        print(f"{arr[i]}:{arr[i+1]},", end="")
        i += 2

def zapisz(arr, argv):
    for number in argv:
        try:
            position = arr[::2].index(number)
            arr[position*2+1] += 1
        except:
            arr += [number, 1]
    return arr 

#########################################
if __name__=="__main__":
    print('Załadowano moduł "{0}"'.format(__name__))
    lista = []
    lista = zapisz(lista, sys.argv[1:])
    wypisz(lista)