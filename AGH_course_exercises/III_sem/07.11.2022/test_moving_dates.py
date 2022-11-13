import unittest
from lesson_class import Lesson
from DeanerySystem.term_class import Term
from DeanerySystem.day import Day

class Test_moving_dates(unittest.TestCase):


    def test_later_day(self):
        fri_full_time = Lesson(Term(Day.FRI, 17, 0), '', '', 1) # False
        fri_not_full_time = Lesson(Term(Day.FRI, 17, 0), '', '', 1, False) # True

        self.assertFalse(fri_full_time.__laterDay())
        self.assertTrue(fri_not_full_time.__laterDay())

    def test_earlier_day(self):
        mon_full_time = Lesson(Term(Day.MON, 17, 0), '', '', 1) # False
        sat_not_full_time = Lesson(Term(Day.SAT, 17, 0), '', '', 1, False) # True

        self.assertFalse(mon_full_time.__earlierDay())
        self.assertTrue(sat_not_full_time.__earlierDay())


    def test_earlier_time(self):
        tue_full_time = Lesson(Term(Day.TUE, 8, 0), '', '', '') # False
        sat_not_full_Time = Lesson(Term(Day.SAT, 15, 0), '', '', '', False) # True

        self.assertFalse(tue_full_time.__earlierTime())
        self.assertTrue(sat_not_full_Time.__earlierTime())

    def test_later_time(self):
        thu_full_time = Lesson(Term(Day.THU, 15, 0), '', '', '') # True
        sun_not_full_time = Lesson(Term(Day.SUN, 20, 0), '', '', '', False) #False

        self.assertTrue(thu_full_time.__laterTime())
        self.assertFalse(sun_not_full_time.__laterTime())
        

if __name__ == '__main__':
    unittest.main()