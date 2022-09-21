import random
#Zamiast znaku x - jako znak losowania liczby będzie rng:
# Wprowadzenie liczb i działań
print("Wybierz liczby: ")
x = float(input("Pierwsza liczba x = "))
y = float(input("Druga liczba y =  "))
print()
print("Dostępne działania:")
print("Dodawanie - '+' ")
print("Odejmowanie - '-'")
print("Mnożenie - '*' ")
print("Dzielenie - '/' ")
print("Potęgowanie - '**' (x do potęgi y) ")
print("Pierwsiatkowanie - '^' (pierwiastek stopnia y z x)")
print("losowanie liczby z zakresy od x do y - 'rng' (Zaokrąglenie do liczb całkowitych) ")
print()
działanie = input("Jakie chcesz wykonać działanie na tych liczbach? ")
#Błąd z dzieleniem przez zero
try:
    dodawanie = x+y
    odejmowanie = x-y
    mnożenie = x*y
    dzielenie = x/y
    potęgowanie = x**y 
    pierwiastkowanie = x**(1/y)
    losowanie = random.randint(int(x), int(y))
except ZeroDivisionError:
    print("Nastąpiło dzielenie przez zero")
#Wykonanie działań
if działanie == "+":
    print("Wynik działania to:", str(dodawanie))
if działanie == "-":
    print("Wynik działania to:", str(odejmowanie))
if działanie == "*":
    print("Wynik działania to:", str(mnożenie))
if działanie == "/" and y != 0:
    print("Wynik działania to:", str(dzielenie))
if działanie == "**":
    print("Wynik działania to:", str(potęgowanie))
if działanie == "^":
    print("Wynik działania to:", str(pierwiastkowanie))
if działanie == "rng":
    print("Wylosowana liczba z danego zakresu to", str(losowanie))
dalsze_kroki = input("Czy chcesz dalej kontynuować liczenie na kalkulatorze? ('T'/'N'): ")
#Zapętlenie kalkulatora:
while dalsze_kroki == "T":
    print("Wybierz liczby: ")
    x = float(input("Pierwsza liczba x = "))
    y = float(input("Druga liczba y =  "))
    print("Dostępne działania:")
    print("Dodawanie - '+' ")
    print("Odejmowanie - '-'")
    print("Mnożenie - '*' ")
    print("Dzielenie - '/' ")
    print("Potęgowanie - '**' (x do potęgi y) ")
    print("Pierwsiatkowanie - '^' (pierwiastek stopnia y z x)")
    print("losowanie liczby z zakresy od x do y - 'rng' (Zaokrąglenie do liczb całkowitych) ")

    działanie = input("Jakie chcesz wykonać działanie na tych liczbach? ")

    try:
        dodawanie = x+y
        odejmowanie = x-y
        mnożenie = x*y
        dzielenie = x/y
        potęgowanie = x**y 
        pierwiastkowanie = x**(1/y)
        
    except ZeroDivisionError:
        print("Nastąpiło dzielenie przez zero")
    if działanie == "+":
        print("Wynik działania to:", str(dodawanie))
    if działanie == "-":
        print("Wynik działania to:", str(odejmowanie))
    if działanie == "*":
        print("Wynik działania to:", str(mnożenie))
    if działanie == "/" and y != 0:
        print("Wynik działania to:", str(dzielenie))
    if działanie == "**":
        print("Wynik działania to:", str(potęgowanie))
    if działanie == "^":
        print("Wynik działania to:", str(pierwiastkowanie))
    if działanie == "rng" and x <= y:
        losowanie = random.randint(int(x), int(y))
        print("Wylosowana liczba z danego zakresu to", str(losowanie))
    if działanie == "rng" and x > y:
        losowanie = random.randint(int(y), int(x))
        print("Wylosowana liczba z danego zakresu to", str(losowanie))
    dalsze_kroki = input("Czy chcesz dalej kontynuować liczenie na kalkulatorze? ('T'/'N'): ")
    if dalsze_kroki == "N":
        exit()

    


