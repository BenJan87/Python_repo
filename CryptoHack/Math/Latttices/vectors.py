class Vector():
    def __init__(self, a, b, c):
        self.x_axis = a
        self.y_axis = b
        self.z_axis = c
    
    def sum_vec(u, v):
        return Vector(u.x_axis+v.x_axis, u.y_axis+v.y_axis, u.z_axis+v.y_axis)
    
    def sub_vec(u, v):
        return Vector(u.x_axis-v.x_axis, u.y_axis-v.y_axis, u.z_axis-v.y_axis)

    def mult_by_num(n, u):
        u.x_axis *= n
        u.y_axis *= n
        u.z_axis *= n
        return u

    def dot_product(u, v):
        return u.x_axis*v.x_axis+u.y_axis*v.y_axis+u.z_axis*v.z_axis

    
if __name__ == "__main__":
    u = Vector(7,7,2)
    v = Vector(2,6,3)
    w = Vector(1,0,0)
    #
    print(Vector.dot_product(Vector.mult_by_num(3, Vector.sub_vec(Vector.mult_by_num(2, v), w)), Vector.mult_by_num(2, u)))
    