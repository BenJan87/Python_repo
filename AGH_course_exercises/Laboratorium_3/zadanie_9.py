# UWAGA: PIN to 1234!!
# Twoje saldo na początku to 2000 pln
# Podanie PIN-u będzie wymagane, gdy przejdzie się do innej operacji

operacja = 0
pin = 0

#początkowe saldo
saldo = 2000

# Zapętlenie całego programu:
while operacja != 4:
    
    # Wybieranie operacji:
    print("Wybierz operację: ")
    print("1. Dokonaj wpłaty")
    print("2. Dokonaj wypłaty")
    print("3. Sprawdź saldo")
    print("4. Zakończ użytkowanie z bankomatu")
    
    #Podanie operacji:
    operacja = int(input("Wpisz nr operacji: "))
    
    # operacja nr 1
    if operacja == 1:
        pin = int(input("Wpisz pin: "))
    # Sprawdzenie pinu
        while pin != 1234:
            pin = int(input("Zły PIN - podaj jeszcze raz: "))
        
    #poprawny pin
    
        wpłata = int(input("Jaką kwotę chcesz wpłacić?: "))
        saldo = int(saldo) + int(wpłata)
        print("Twoje obecne saldo to ", str(saldo), "pln")
        pin = 0
    # operacja nr 2
    
    if operacja == 2:
        pin = int(input("Wpisz pin: "))
    
    # Sprawdzenie pinu
        while pin != 1234:
            pin = int(input("Zły PIN - podaj jeszcze raz: "))
        wypłata = int(input("Jaką kwotę chcesz wypłacić?: "))
        saldo = int(saldo) - int(wypłata)
        
        #Saldo mniejsze od 0:
        if int(saldo) < 0:
            print("Nie mozna wypłacić tyle pieniędzy")
            saldo = int(saldo) + int(wypłata)
        pin = 0
        print("Twoje obecne saldo to ", str(saldo), "pln")
    if operacja == 3:
        pin = int(input("Wpisz pin: "))
    
    # Sprawdzenie pinu
        while pin != 1234:
            pin = int(input("Zły PIN - podaj jeszcze raz: "))
        print("Twoje obecne saldo to ", str(saldo), "pln")
        pin = 0



    
        

    

 


