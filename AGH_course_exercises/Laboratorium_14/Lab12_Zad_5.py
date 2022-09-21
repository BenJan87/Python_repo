
class Im_numbers:
    def __init__(self, Re, Im):
        self.Re = Re
        self.Im = Im
    
    def add_Im(num_1, num_2):
        return Im_numbers(num_1.Re+num_2.Re,num_1.Im+num_2.Im)

    def sub_Im(num_1, num_2):
        return Im_numbers(num_1.Re-num_2.Re, num_1.Im-num_2.Im)

    def multi_Im(num_1,num_2):
        return Im_numbers(num_1.Re*num_2.Re-num_1.Im*num_2.Im, num_1.Re*num_2.Im+num_2.Re*num_1.Im)

    def div_Im(num_1, num_2):
        return Im_numbers((num_1.Re*num_2.Re+num_1.Im*num_2.Im)/(num_2.Re**2+num_2.Im**2),(num_2.Re*num_1.Im-num_1.Re*num_2.Im)/(num_2.Re**2+num_2.Im**2))

    def exp_Im(num_1,n):
        import math
        n = float(n)
        z1 = float(math.sqrt((num_1.Re**2+num_1.Im**2)))
        return Im_numbers(z1**n*math.cos(n*math.atan(num_1.Im/num_1.Re)),z1**n*math.sin(n*math.atan(num_1.Im/num_1.Re)))

# x = input("Podaj pierwszą liczbę: (cz. rzeczywistą, a pózniej oddzielona spacją cz. urojona)\nnp.: liczbę 4-5i - wpisz: '4 -5': ")
# x1 = x.split()
# num_1 = Im_numbers(float(x1[0]),float(x1[1]))
# y = input("Podaj drugą liczbę: ")
# y1 = y.split()
# num_2 = Im_numbers(float(y1[0]),float(y1[1]))
# n = input("Podaj liczbę naturalną, do której spotęgowane zostaną dane dwie liczby: ")


# addition = Im_numbers.add_Im(num_1, num_2)
# subtraction = Im_numbers.sub_Im(num_1, num_2)
# multiplication = Im_numbers.multi_Im(num_1, num_2)
# division = Im_numbers.div_Im(num_1, num_2)
# exp_1 = Im_numbers.exp_Im(num_1,n)
# exp_2 = Im_numbers.exp_Im(num_2,n)

# print("Pierwsza podana liczba: (",num_1.Re,") + (",num_1.Im,") i")
# print("Druga podana liczba: (",num_2.Re,") + (",num_2.Im,") i")

# print("\nDodawanie: (",addition.Re,") + (",addition.Im,") i")
# print("Odejmowanie: (",subtraction.Re,") + (",subtraction.Im,") i")
# print("Mnożenie: (",multiplication.Re,") + (",multiplication.Im,") i")
# print("Dzielenie: (",division.Re,") + (",division.Im,") i")

# print("\nPodniesie pierwszej liczby do potęgi'",n,"' : (",round(exp_1.Re,4),") + (",round(exp_1.Im,4),") i")
# print("Podniesie drugiej liczby do potęgi'",n,"' : (",round(exp_2.Re,4),") + (",round(exp_2.Im,4),") i")

# print("\n\nRozwiązywanie równań kwadratowych:")
# x = input("Podaj liczbę zespoloną przy x^2: \n(np.: dla 5-i -> wpisz: '5 -1'): ")
# y = input("Podaj liczbę zespoloną przy x: ")
# z = input("Podaj wyraz wolny: ")
# x1 = x.split()
# y1 = y.split()
# z1 = z.split()
# num_1 = Im_numbers(float(x1[0]),float(x1[1]))
# num_2 = Im_numbers(float(y1[0]),float(y1[1]))
# num_3 = Im_numbers(float(z1[0]),float(z1[1]))

# num_delta = Im_numbers.sub_Im(Im_numbers.exp_Im(num_2,2) , Im_numbers.multi_Im(Im_numbers(4,0),Im_numbers.multi_Im(num_1,num_3)))
# pos_sqrt_delta = Im_numbers.exp_Im(num_delta,1/2)
# neg_sqrt_delta = Im_numbers(-pos_sqrt_delta.Re,-pos_sqrt_delta.Im)


# numer_first_z = Im_numbers.sub_Im(pos_sqrt_delta,num_2)
# numer_sec_z = Im_numbers.sub_Im(neg_sqrt_delta,num_2) 
# number2 = Im_numbers(2, 0)
# dem_z = Im_numbers.multi_Im(number2, num_1)
# first_z = Im_numbers.div_Im(numer_first_z,dem_z)
# sec_z = Im_numbers.div_Im(numer_sec_z,dem_z)


# if num_delta.Re == 0 and num_delta.Im == 0:
#     print("Rozwiazaniem danego równania jest liczba:")
#     print("x0 = (",first_z.Re,") + (",first_z.Im,") i")
# else:
#     print("Rozwiazaniami danego równania są liczby:")
#     print("x1 = (",round(first_z.Re,4),") + (",round(first_z.Im,4),") i")
#     print("x2 = (",round(sec_z.Re,4),") + (",round(sec_z.Im,4),") i")
    

