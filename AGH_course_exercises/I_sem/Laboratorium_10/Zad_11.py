import re

file_sin = open("C:/Users/benja/OneDrive/Pulpit/Studia_AGH/Zadania_cwiczeniowe/WDI_labki/wdi/Laboratorium_10/wart_sin.txt")
file_cos = open("C:/Users/benja/OneDrive/Pulpit/Studia_AGH/Zadania_cwiczeniowe/WDI_labki/wdi/Laboratorium_10/wart_cos.txt")
file_tg = open("C:/Users/benja/OneDrive/Pulpit/Studia_AGH/Zadania_cwiczeniowe/WDI_labki/wdi/Laboratorium_10/wart_tg.txt")
file_ctg = open("C:/Users/benja/OneDrive/Pulpit/Studia_AGH/Zadania_cwiczeniowe/WDI_labki/wdi/Laboratorium_10/wart_ctg.txt")
fun = input("Wpisz funkcję (sin, cos, tg, ctg): ")
x = input("""\nWpisz miarę w stopniach, np.: "30"\nlub w radianach, np.:"pi/2", "2*pi": """)

def sin(a):
    match a:
        case '180':
            return file_sin.readlines()[0]
        case '360':
            return file_sin.readlines()[0]
        case "pi/6":
            return file_sin.readlines()[30]
        case "pi/4":
            return file_sin.readlines()[45]
        case "pi/3":
            return file_sin.readlines()[60]
        case "pi/2":
            return file_sin.readlines()[90]
        case "pi":
            return file_sin.readlines()[0]
        case "2*pi":
            return file_sin.readlines()[0]
    if a == x and str.isdigit(a) is True and a != 180 and a != 360:
        return file_sin.readlines()[int(a)]

def cos(a):
    match a:
        case '180':
            return file_cos.readlines()[91]
        case '360':
            return file_cos.readlines()[0]
        case "pi/6":
            return file_cos.readlines()[30]
        case "pi/4":
            return file_cos.readlines()[45]
        case "pi/3":
            return file_cos.readlines()[60]
        case "pi/2":
            return file_cos.readlines()[90]
        case "pi":
            return file_cos.readlines()[91]
        case "2*pi":
            return file_cos.readlines()[0]
    if a == x and str.isdigit(a) is True and a != 180 and a != 360:
        return file_cos.readlines()[int(a)]

def tg(a):
    match a:
        case '180':
            return file_tg.readlines()[0]
        case '360':
            return file_tg.readlines()[0]
        case "pi/6":
            return file_tg.readlines()[30]
        case "pi/4":
            return file_tg.readlines()[45]
        case "pi/3":
            return file_tg.readlines()[60]
        case "pi/2":
            return file_tg.readlines()[90]
        case "pi":
            return file_tg.readlines()[0]
        case "2*pi":
            return file_tg.readlines()[0]
    if a == x and str.isdigit(a) is True and a != 180 and a != 360:
        return file_tg.readlines()[int(a)]

def ctg(a):
    match a:
        case '180':
            return file_tg.readlines()[0]
        case '360':
            return file_tg.readlines()[0]
        case "pi/6":
            return file_tg.readlines()[30]
        case "pi/4":
            return file_tg.readlines()[45]
        case "pi/3":
            return file_tg.readlines()[60]
        case "pi/2":
            return file_tg.readlines()[90]
        case "pi":
            return file_tg.readlines()[0]
        case "2*pi":
            return file_tg.readlines()[0]
    if a == x and str.isdigit(a) is True and a != 180 and a != 360:
        return file_ctg.readlines()[int(a)]

if fun == "sin":
    y = sin(x)
    print("sin(",x,") = ",y)
if fun == "cos":
    y = cos(x)
    print("cos(",x,") = ",y)
if fun == "tg":
    y = tg(x)
    print("tg(",x,") = ",y)
if fun == "ctg":
    y = ctg(x)
    print("ctg(",x,") = ",y)

z = str(fun+"("+x+") = "+y)

file_2 = open("C:/Users/benja/OneDrive/Pulpit/Studia_AGH/Zadania_cwiczeniowe/WDI_labki/wdi/Laboratorium_10/historia_kalkulatora.txt", "a")
file_2.write(z)

file_sin.close()
file_cos.close()
file_tg.close()
file_ctg.close()
file_2.close()


