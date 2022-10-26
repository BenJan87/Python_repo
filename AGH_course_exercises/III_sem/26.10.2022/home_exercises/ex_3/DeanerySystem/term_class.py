class Term():

    def __init__(self, day_of_week, hour, minute):
        self.hour = hour
        self.minute = minute
        self.duration = 90
        self.__day = day_of_week

    def __str__(self):
        match self.__day.value:
            case 1:
                day_name = "Monday"
            case 2:
                day_name = "Tuesday"
            case 3:
                day_name = "Wednesday"
            case 4:
                day_name = "Thursday"
            case 5:
                day_name = "Friday"
            case 6:
                day_name = "Saturday"
            case 7:
                day_name = "Sunday"

        return f'{day_name} {self.hour}:{self.minute} [{self.duration}]'

    def earlierThan(self, termin):
        if self.__day.value < termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
        return False


    def laterThan(self, termin):
        if self.__day.value > termin.__day.value:
            return True
        elif self.__day.value == termin.__day.value:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self.__day.value == termin.__day.value and self.hour == termin.hour and self.minute == termin.minute and self.duration == termin.duration:
            return True
        return False
        