class Vector():
    def __init__(self, arr):
        self.cords = arr
    
    def dot_product(a, b):
        return sum([a.cords[i]*b.cords[i] for i in range(len(a.cords))])

    def sum_vec(a, b):
        return Vector([a.cords[i]+b.cords[i] for i in range(len(a.cords))])

    def sub_vec(a, b_m):
        return Vector([a.cords[i]-b_m.cords[i] for i in range(len(a.cords))])

    def length(u):
        return (sum([el**2 for el in u]))**(1/2)

    def mult_by_num(u, n):
        return Vector([u.cords[i]*n for i in range(len(u.cords))])

    
if __name__ == "__main__":
    u = Vector([7,7,2])
    v = Vector([2,6,3])
    w = Vector([1,0,0])
    print(Vector.dot_product(Vector.mult_by_num( Vector.sub_vec(Vector.mult_by_num(v, 2), w), 3), Vector.mult_by_num(u, 2)))
    