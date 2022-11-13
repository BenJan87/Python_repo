class Own_date():
    def __init__(self):
        self._hour = 0
        self._minute = 0


    @property
    def hour(self):
        return self._hour


    @hour.setter
    def hour(self, given_hour):
        if given_hour < 0 or given_hour > 23:
            raise ValueError('Hour is incorrect')
        self._hour = given_hour
        


    @property
    def minute(self):
        return self._minute
    

    @minute.setter
    def minute(self, given_minute):
        if given_minute < 0 or given_minute > 59:
            raise ValueError('Minute is incorrect')
        self._minute = given_minute


    def __sub__(self, end_date):
        minutes_self = self._hour * 60 + self._minute
        minutes_end_date = end_date._hour * 60 + end_date._minute

        all_minutes = minutes_self - minutes_end_date
        if all_minutes < 0:
            all_minutes += 24*60

        return all_minutes


# ft = Own_date()
# ft.hour = 15
# ft.minute = 0
# sec = Own_date()
# sec.hour = 16
# sec.minute = 0

# print(sec - ft)