import unittest

from DeanerySystem.day import Day
from DeanerySystem.term_class import Term


class Test_TestDay(unittest.TestCase):
    term_1 = Term(Day.WED, 15, 20)
    term_2 = Term(Day.WED, 15, 30)

    term_3 = Term(Day.THU, 19, 50)
    term_4 = Term(Day.THU, 19, 40)

    term_5 = Term(Day.SUN, 19, 30)
    term_6 = Term(Day.SUN, 19, 30)

    def test_earlierThan(self):
        self.assertTrue(self.term_1.earlierThan(self.term_2))
        self.assertFalse(self.term_3.earlierThan(self.term_4))
        self.assertFalse(self.term_5.earlierThan(self.term_6))

    def test_laterThan(self):
        self.assertFalse(self.term_1.laterThan(self.term_2))
        self.assertTrue(self.term_3.laterThan(self.term_4))
        self.assertFalse(self.term_5.laterThan(self.term_6))

    def test_equals(self):
        self.assertFalse(self.term_1.equals(self.term_2))
        self.assertFalse(self.term_3.equals(self.term_4))
        self.assertTrue(self.term_5.equals(self.term_6))

    
if __name__ == '__main__':
    unittest.main()