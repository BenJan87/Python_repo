# Wpisanie zmiennych

a = float(input("Wprowadź pierwszą liczbę: "))
b = float(input("Wprowadź drugą liczbę: "))

# Sprawdzenie danych
if a < 0 and b < 0:
    print("Wprowadzone liczby są niedodatnie")
    exit()
if (a <= 0 and b > 0) or (b <= 0 or a > 0):
    a = abs(a)
    b = abs(b)
# Dzielenie przez zero
if b == 0:
    print("Nastąpiło dzielenie przez zero")
    exit()
#Wykonanie działań
suma = a + b
iloczyn = a*b
róznica = a-b
iloraz = a/b
kwadrat_a = a**2
kwadrat_b = b**2
pierwiastek_a = a**(1/2)
pierwiastek_b = b**(1/2)


print()
print("Suma wpisanych liczb:",suma)
print("Róznica wpisanych liczb:", róznica)
print("Ioczyn wpisanych liczb:", iloczyn)
print("Iloraz wpisanych liczb", iloraz)
print("Kwadrat pierwszej wpisanej liczby:", kwadrat_a)
print("Kwadrat drugiej wpisanej liczby", kwadrat_b)
print("Pierwsiatek pierwszej wpisanej liczby:", pierwiastek_a)
print("Pierwiastek drugiej wpisanej liczby", pierwiastek_b)

# Warunek iloczyn == 10
if iloczyn == 10:
    print("Yay!")





    


