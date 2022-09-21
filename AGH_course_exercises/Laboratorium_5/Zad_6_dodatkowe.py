

liczba = (int(input("Wprowadź liczbę naturalną: ")))
#Liczby 0 i 1 nie są ani pierwsze, ani złoźone
if liczba == 0:
    print("Twoja liczba to 0")
    exit()
if liczba == 1:
    print("Twoja liczba to 1")
    exit()
y = 2
while True:
    if liczba%y != 0:
        y += 1 
        if y == liczba:
            print("Twoja liczba jest pierwsza") 
            break
    if liczba%y == 0:
        print("Twoja liczba nie jest pierwsza")
        break
    

