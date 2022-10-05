while True:
    
    # Wprowadzenie trzech liczb:
    a = int(input("Wprowadź pierwszą liczbę: "))
    b = int(input("Wprowadź drugą liczbę: "))
    c = int(input("Wprowadź trzecią liczbę: "))
    if a <= 0 or b <= 0 or c <= 0 or a == b or a == c or b == c:
        print("Wpisz liczby naturalne dodatnie i róźne od siebie!")
        print()
    if a > 0 and b > 0 and c > 0 and a != b and a != c and b != c:
        break

#Znalezienie najmniejszej liczby:
if a < b and a < c:
    i = a
    while True:
        #Sprawdzenie czy dana liczba nie jest nwd:
        if (a%i == 0) and (b%i == 0) and (c%i == 0):
            nwd = i
            #wzór na nww:
            nww = (a*b*c)/nwd
            print("NWW to", str(int(nww)))
            break
        #Sprwadzenie liczby o jeden mniejszej, aż nie znajdziemy nwd tych trzech liczb:
        else:
            i -= 1
if b < a and b < c:
    i = b
    while True:
        if (a%i == 0) and (b%i == 0) and (c%i == 0):
            nwd = i
            #wzór na nww:
            nww = (a*b*c)/nwd
            print("NWW to", str(int(nww)))
            break
        else:
            i -= 1
if c < b and c < a:
    i = c
    while True:
        if (a%i == 0) and (b%i == 0) and (c%i == 0):
            nwd = i
            #wzór na nww:
            nww = (a*b*c)/nwd
            print("NWW to", str(int(nww)))
            break
        else:
            i -= 1