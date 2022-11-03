import unittest
from rental_class import Rental

class Test_TestDay(unittest.TestCase):
    
    def test_parse_file_line(self):
        magazine_1 = [{'model': "B'twin", 'amount': 40, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 50, 'cost_per_min': 2.0},
                      {'model': "Kross", 'amount': 60, 'cost_per_min': 3.0},
                      {'model': "Shimano", 'amount': 70, 'cost_per_min': 4.0},
                      {'model': "Rockrider", 'amount': 80, 'cost_per_min': 5.0},
                      {'model': "Romet", 'amount': 90, 'cost_per_min': 6.0}]
        
        self.assertEqual(Rental.parse_file_line(r'02.11.2022\magazine.txt', []), magazine_1)
        self.assertFalse(Rental.parse_file_line('No_file_found', []))
        self.assertFalse(Rental.parse_file_line(r'02.11.2022\incorrect_magazine.txt',[]))
        self.assertFalse(Rental.parse_file_line(r'02.11.2022\incorrect_amounts.txt', []))




if __name__ == '__main__':
    unittest.main()