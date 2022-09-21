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
a = 5


def factorial(a):
    all_num = [i for i in range(1, a)]
    for i in all_num:
        a = a*i
    return a
def bin_theorem(n, k):
    return (factorial(n))/((factorial(k))*factorial(n-k))



import math
print(math.sin(3.14/2))
