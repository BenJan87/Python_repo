
# m2 = 0
# n1 = 1
# while n1 != m2:
#     print("Aby można było przemnożyć macierze, liczba wierszy pierwszej macierzy\nmusi być równa liczbę kolumn drugiej macierzy!")
#     m1 = int(input("Podaj liczbę wierszy w pierwszej macierzy: "))
#     n1 = int(input("Podaj liczbę kolumn w pierwszej macierzy: "))
#     m2 = int(input("Podaj liczbę wierszy w drugiej macierzy: "))
#     n2 = int(input("Podaj liczbę kolumn w drugiej macierzy: "))

def own_matrix(m, n):
    mat_1 = []
    while len(mat_1) != m:
        x = input("Podaj kolejne wiersze macierzy (liczby oddzielone spacją): ")
        y = x.split()
        while len(y) != n:
            x = input("Ilość liczb w wierszu musi być równa podanej wczesniej liczbie\nPodaj wiersz jeszcze raz: ")
            y = x.split()
        mat_1.append(y)
    return mat_1

# print("Podaj pierszą macierz:")
# A = (own_matrix(m1,n1))
# print("Podaj druga macierz:")
# B = (own_matrix(m2,n2))
# print("Pierwsza macierz:\n", A)
# print()
# print("Druga macierz:\n", B)

def multi_matrix(M1, M2):
    result = []
    for i in range(len(M1)):
        result.append([])
        for j in range(len(M2[0])):
            val = 0
            for k in range(len(M2)):
                val += int(M1[i][k])*int(M2[k][j])
            result[i].append(val)
    return result

# print("Powstała macierz z mnożenia:\n", multi_matrix(A, B))

def slice_matrix(M, slice_index):
    return [row[0:slice_index] + row[slice_index + 1:] for row in M[1:]]

def main_det(M):
    if len(M) == len(M[0]):
        if len(M) == 2:
            return int(M[0][0]) * int(M[1][1]) - int(M[0][1]) * int(M[1][0])
        if len(M) == 1:
            return int(M[0][0])
        else:
            x = [((-1) ** i) * int(M[0][i]) * main_det(slice_matrix(M, i)) for i in range(len(M))]
            return sum(x)
    

def matrix_num_multi(M, x):
    for i in range(len(M)):
        for j in range(len(M[0])):
            M[i][j] = x*int(M[i][j])
    return M

# if m1 == n1: 
#     print("Macierz A przemnożona przez swój wyznacznik: ")
#     print(matrix_num_multi(A, (main_det(A))))
# if m2 == n2:
#     print("Macierz B przemnożona przez swój wyznacznik: ")
#     print(matrix_num_multi(B, main_det(B)))
# if m1 != n1 :
#     y = int(input("Nie można obliczyć wyznacznika, podaj skalar: "))
#     print("Powstała macierz po pomnożeniu przez skalar:\n", y)
# if m2 != n2 :
#     y = int(input("Nie można obliczyć wyznacznika, podaj skalar: "))
#     print("Powstała macierz po pomnożeniu przez skalar:\n", y)


