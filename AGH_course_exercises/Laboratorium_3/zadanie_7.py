# Wprowadzanie zmiennych:

pl = int(input("Wprowadź pierwsza liczbę: "))
dl = int(input("Wprowadź drugą liczbę (większą od pierwszej): "))

# średnia:

śr1 = ((dl +pl)/2)

# Zaleźności większość:
while dl < pl:
    print("Pierwsza podana liczba musi byc większa od drugiej!")
    pl = int(input("Wprowadź pierwsza liczbę: "))
    dl = int(input("Wprowadź drugą liczbę (większą od pierwszej): "))

# Zakres mniejszy lub równy 20:
if abs(pl - dl) <= 20: 
    lista = print(list(range(pl, dl+1)))
    

# Zakres większy od 20 i sr1 jest całkowite:
if abs(pl - dl) > 20 and (float(śr1) - int(śr1)) == 0:
   lista = []
   for x in range(int(śr1-3), int(śr1)):
       lista.append(x)
   for z in range(int(śr1+1), int(śr1 + 4)):
       lista.append(z)



# Zakres większy od 20 i sr1 jest wymierne:
if abs(pl - dl) > 20 and (float(śr1) - int(śr1)) != 0:
   lista = []
   for y in range(int(śr1-2), int(śr1+4)):
       lista.append(y)
print(lista)



    
    




