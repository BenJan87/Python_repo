from vectors import *

def gram_schmidt(arr, base,i):
    if i == 0:
        base.append(arr[i])
        return arr[i]
    base.append(Vector.sub_vec(arr[i], multi_by_num))



if __name__ == "__main__":
    u = Vector([4, 6, 2, 5])
    v = Vector([2,1,-3,4])
    w = Vector([1,0,-2,7])
    x = Vector([6, 2, 9, -5])

    vecs = [u, v, w, x]
    base = []
    i = len(arr) - 1
    gram_schmidt(vecs, base, i)