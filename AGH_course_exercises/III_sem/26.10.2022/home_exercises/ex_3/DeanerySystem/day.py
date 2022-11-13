from enum import Enum
class Day(Enum):
    MON = 1
    TUE = 2
    WED = 3
    THU = 4
    FRI = 5
    SAT = 6
    SUN = 7

    def difference(self, day):
        res = day.value - self.value
        if res < 4 and res > -4:
            return res
        elif res > 4:
            return res - 7
        else:
            return res + 7


def nth_day_from(n, day):
    res = (((day.value) + n) % 7)
    if res == 0:
        return Day.SUN
    return Day(res)

print("Imported day!")
