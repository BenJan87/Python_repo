class Ben():
    def __init__(self):
        self.age = 20

    def __str__(self):
        return f"{self.age}"

obj = Ben()
print(obj)