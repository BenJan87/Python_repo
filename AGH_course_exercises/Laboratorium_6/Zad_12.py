print("Przybliżenie pola pod wykresem funkcji określonej wzorem: f(x)= 1/x ")
print ("Wprowadź 'k', gdzie 'k' to koniec zakresu, do którego chcesz poznać wartość pola")
k = float(input(" <1;k>, gdzie k to: "))
while True:
    if k < 1 and k != 0:
        print("Wpisz liczbę większą lub równą 1")
        k = float(input("k = "))
    if k == 1:
        print("Pole pod wykresem jest równe zero")
        exit()
    if k == 0:
        try:
            y = 1/k
            if k == 0: 
                raise ZeroDivisionError
        except ZeroDivisionError:
            print("Nastapiło dzielenie przez zero - wprowadź inną liczbę:")
            k = float(input("k = "))
    if k > 1:
        break
 
a = 1
# Wartość pierwszego pola, gdy x = 1, f(X) = 1, 
# a długośc boku prostokąta wynosi length = 0.0001
lista = [0.0001]
while a < k:
    length = 0.0001
    a += 0.0001
    f_x = 1/a
    pole = f_x * length
    lista.append(float(pole))
przyb = sum(lista)
print("Przybliżone pole pod wykresem w danym przedziale wynosi:", przyb)
print()

import math
cał = (math.log(k, math.e))
print("Dokładna wartość pola pod wykresem wynosi:", cał)
print()

print("Błąd względny przybliżenia wynosi", str(round(((abs(przyb - cał))/cał)*100, 5)), "%")