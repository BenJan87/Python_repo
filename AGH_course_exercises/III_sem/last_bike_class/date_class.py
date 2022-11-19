class Own_date():
    def __init__(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def __sub__(self, end_date):
        minutes_self = self.hour * 60 + self.minute
        minutes_end_date = end_date.hour * 60 + end_date.minute

        allminutes = minutes_self - minutes_end_date
        if allminutes < 0:
            allminutes += 24*60

        return allminutes


# ft = Own_date()
# ft.hour = 15
# ft.minute = 0
# sec = Own_date()
# sec.hour = 16
# sec.minute = 0

# print(sec - ft)