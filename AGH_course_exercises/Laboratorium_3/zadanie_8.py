#Wprowadzenie liczby
x = int(input("podaj liczbe: "))
#Choinka "zwyczajna"
for i in range(x+1):
    for a in range(x-i):
        print(" ", end="")
    for b in range(2*i-1):
        print("*", end="")
        b = b + 2
    print("")

#Import random do wylosowania gwiazdki lub bombki
import random
x = int(input("podaj liczbe: "))
for a in range(x - 1):
    print(" ", end="")
print("x")
for i in range(2,x+1):
    for a in range(x-i):
        print(" ", end="")
    for b in range(2*i-1):
        #Wylosowanie bombki lub gwiazdki
        p = random.randint(0,100)
        #prawdopodobieństwo wylosowannia gwiazdki 
        if p>20:
            print("*", end="")
        #prawdopodobieństwo wylosowannia bobmki
        else:
            print("o", end="")
        b = b + 2
    print("")
for a in range(x - 1):
    print(" ", end="")
print("U")