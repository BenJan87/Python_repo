class Vector_len():
    def length(u):
        u = [el**2 for el in u]
        return (sum(u))**(1/2)

if __name__ == "__main__":
    u = [4, 6, 2, 5]
    print(Vector_len.length(u))