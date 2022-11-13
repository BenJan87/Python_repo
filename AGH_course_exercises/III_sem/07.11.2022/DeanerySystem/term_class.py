# from day import Day
class Term():

    def __init__(self, day_of_week, hour, minute, duration = 90):
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.day = day_of_week

    def __str__(self):
        match self.day.value:
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
        if self.day.value < termin.day.value:
            return True
        elif self.day.value == termin.day.value:
            if self.hour < termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute < termin.minute:
                    return True
        return False


    def laterThan(self, termin):
        if self.day.value > termin.day.value:
            return True
        elif self.day.value == termin.day.value:
            if self.hour > termin.hour:
                return True
            elif self.hour == termin.hour:
                if self.minute > termin.minute:
                    return True
        return False

    def equals(self, termin):
        if self.day.value == termin.day.value and self.hour == termin.hour and self.minute == termin.minute and self.duration == termin.duration:
            return True
        return False
    
    def __sub__(self, termin):
        if termin.day.value >= self.day.value:
            flag = 7
        else: 
            flag = 0
        
        time_self = (self.day.value + flag) * 24 * 60 + self.hour * 60 + self.minute + self.duration
        time_termin = (termin.day.value) * 24 * 60 + termin.hour * 60 + termin.minute

        return Term(termin.day, termin.hour, termin.minute, time_self - time_termin)
    

    def __lt__(self, termin):
        if self.earlierThan(termin):
            return True
        return False

    def __le__(self, termin):
        if self.earlierThan(termin) or self.equals(termin):
            return True
        return False

    def __gt__(self, termin):
        if self.laterThan(termin):
            return True
        return False
    
    def __ge__(self, termin):
        if self.laterThan(termin) or self.equals(termin):
            return True
        return False
    
    def __eq__(self, termin):
        if self.equals(termin):
            return True
        return False