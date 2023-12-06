# arr = [1, 2, 3, 4]

# x = arr[0]
# x += 1

# print(arr)

# import random
# while True:
#     x = random.randint(0, 2500)
#     if x == 1300:
#         print(x)
#         break


def fun(x):
    if x == 1:
        return 1
    
x = 0
print(fun(x))

class Klasa():
    def __init__(self, x = 1) -> None:
        self.x = x

    def change(self):
        self.x += 1



new = Klasa()
print(new.x)

new.change()
print(new.x)

newVar = new
newVar.x += 1

print(newVar.x)
print(new.x)

