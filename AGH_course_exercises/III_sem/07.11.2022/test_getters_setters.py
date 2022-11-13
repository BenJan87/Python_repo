class Settlersi():
    def __init__(self) -> None:
        self.__min = 0

    @property
    def min(self):
        return self.__min

    @min.setter
    def min(self, given_min):
        if given_min >= 0:
            self.__min = given_min

        else:
            self.__min = -1


obj = Settlersi()
obj.min = -50
print(obj.min)
obj.min += 2
print(obj.min)