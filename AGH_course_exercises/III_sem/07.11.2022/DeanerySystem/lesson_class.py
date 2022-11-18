from day import Day
from term_class import Term
class Lesson():
    def __init__(self):
        self.__term = None
        self.__name = None
        self.__teacherName = None
        self.__year = None
        self.__fullTime = None 

    @property
    def term(self):
        return self.__term

    @property
    def name(self):
        return self.__name

    @property
    def teacherName(self):
        return self.__teacherName

    @property
    def year(self):
        return self.__year

    @property
    def fullTime(self):
        return self.__fullTime

    @term.setter
    def term(self, given_term):
        self.__term = given_term

    @name.setter
    def name(self, given_name):
        self.__name = given_name

    @teacherName.setter
    def teacherName(self, given_teacher_name):
        self.__teacherName = given_teacher_name

    @year.setter
    def year(self, year):
        if year in range(1, 6):
            self.__year = year
        else:
            print("Incorrect number")

    @fullTime.setter
    def fullTime(self, given_data):
        if isinstance(given_data, bool):
            self.__fullTime = given_data
        else:
            print("Incorrect full-time check")


    def __earlierDay(self):
        previous_day = self.__term.day.value - 1
        new_minute = self.__term.minute + self.__term.duration
        new_hour = self.__term.hour
        if previous_day == 0:
            previous_day += 7
        while new_minute > 59:
            new_hour += 1
            new_minute -= 60

        if self.__fullTime:
            if previous_day in [1, 2, 3, 4]:
                if new_hour >= 8 and new_hour <= 19 or new_hour == 20 and new_minute == 0:
                    return True
            if previous_day == 5:
                if new_hour >= 8 and new_hour <= 16 or new_hour == 17 and new_minute == 0:
                    return True
        else:
            if previous_day in [6, 7]:
                if new_hour >= 8 and new_hour <= 19 or new_hour == 20 and new_minute == 0:
                    return True
            if previous_day == 5:
                if new_hour >= 17 and new_hour <= 19 or new_hour == 20 and new_minute == 0:
                    return True

        return False
                  

    def __laterDay(self):
        next_day = self.__term.day.value + 1
        if next_day == 8:
            next_day -= 7

        new_minute = self.__term.minute + self.__term.duration
        new_hour = self.__term.hour

        while new_minute > 59:
            new_hour += 1
            new_minute -= 60

        if self.__fullTime:
            if next_day in [1, 2, 3, 4]:
                if new_hour >= 8 and new_hour <= 19 or new_hour == 20 and new_minute == 0:
                    return True
            if next_day == 5:
                if new_hour >= 8 and new_hour <= 16 or new_hour == 17 and new_minute == 0:
                    return True
        else:
            if next_day in [6, 7]:
                if (new_hour >= 8 and new_hour <= 19) or (new_hour == 20 and new_minute == 0):
                    return True
            if next_day == 5:
                if new_hour >= 17 and new_hour <= 19 or new_hour == 20 and new_minute == 0:
                    return True
        return False


    def __earlierTime(self):
        # rember from one - day of week
        minute_from_start = self.__term.day.value * 24 * 60 + self.__term.hour * 60 + self.__term.minute
        new_minute = minute_from_start - self.__term.duration

        new_day = new_minute//1440
        new_minute = new_minute % 1440

        new_hour = new_minute//60
        new_minute = new_minute % 60

        if self.__fullTime:
            if new_day in range(1, 6) and new_hour >= 8:
                return True
        else:
            if new_day == 5 and new_hour >= 17 or new_day in [6, 7] and new_hour >= 8:
                return True
            
        return False


    def __laterTime(self):    
        minute_from_start = self.__term.day.value * 24 * 60 + self.__term.hour * 60 + self.__term.minute
        new_minute = minute_from_start + self.__term.duration

        new_day = new_minute//1440
        new_minute = new_minute % 1440

        new_hour = new_minute//60
        new_minute = new_minute % 60

        if self.__fullTime:
            if new_day in range(1, 5) and (new_hour <= 19 or new_hour == 20 and new_minute == 0):
                return True
            if new_day == 5 and (new_hour <= 16 or new_hour == 17 and new_minute == 0):
                return True
        else:
            if new_day in [5, 6, 7] and (new_hour <= 19 or new_hour == 20 and new_minute == 0):
                return True

        return False


    def __str__(self):
        new_hour = self.__term.hour
        new_day = self.__term.day.value
        new_minute = self.__term.minute
        duration = self.__term.duration

        new_minute += duration
        while new_minute > 59:
            new_hour += 1
            new_minute -= 60
        
        match new_day:
            case 1:
                new_day = "Monday"
            case 2:
                new_day = "Tuesday"
            case 3:
                new_day = "Wednesday"
            case 4:
                new_day = "Thursday"
            case 5:
                new_day = "Friday"
            case 6:
                new_day = "Saturday"
            case 7:
                new_day = "Sunday"
        
        match self.__year:
            case 1:
                new_year = 'Pierwszy'
            case 2:
                new_year = 'Drugi'
            case 3:
                new_year = 'Trzeci'
            case 4:
                new_year = 'Czwarty'
            case 5:
                new_year = 'Piąty'

        new_full_time = 'stacjonarnych'
        if not self.__fullTime:
            new_full_time = "nie" + new_full_time
        

        return f'''{self.__name} ({new_day} {self.__term.hour}:{self.__term.minute}-{new_hour}:{new_minute})
{new_year} rok studiów {new_full_time}
Prowadzący: {self.__teacherName}'''