#Programm which printing recursive tree


def show(arr, p, q):
    for i in range(q):
        print("")
        for j in range(p):
            print(arr[i][j], end="")



def conversion(length, i, j):
    global arr
    for k in range(length):
        arr[i-k][j] = "1"
        arr[i-k-length+1][j-k] = "1"
        arr[i-k-length+1][j+k] = "1"
    arr[i-2*length+1][j-length] = "1"
    arr[i-2*length+1][j+length] = "1"

    if length == 1:
        return
    conversion(length//2, i - 2*length, j - length)
    conversion(length//2, i - 2*length, j + length)

# def conv_2(length, i, j, n):
#     global arr
#     j_list = [j]
#     it = 1
#     while True:
#         for j in j_list:
#             for k in range(length):
#                 arr[i-k][j] = "1"
#                 arr[i-k-length+1][j-k] = "1"
#                 arr[i-k-length+1][j+k] = "1"
#             arr[i-2*length+1][j-length] = "1"
#             arr[i-2*length+1][j+length] = "1"

#         it += 1
#         i = i - 2*length
#         for _ in range(2**):
#             j_list.append(j-length)
#             j_list.append(j+length)
#         for _ in range(2**(n-it+1)):
#             j_list.pop()
        
#         length = length // 2
#         if length == 1:
#             break


if __name__=="__main__":
    p = int(input("Rows: "))
    q = int(input("Columns: "))
    n = int(input("iterations: "))

    arr = [ ["_" for i in range(p)] for j in range(q)]
    
    
    i, j = q - 1, p // 2
    length = 2**(n-1)
    # conv_2(length, i, j, n)
    conversion(length, i, j, n)
    show(arr, p, q)
    



