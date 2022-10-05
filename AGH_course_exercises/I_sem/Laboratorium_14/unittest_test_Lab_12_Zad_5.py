import unittest
from Lab12_Zad_5 import Im_numbers
    
class LearnTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.num_1 = Im_numbers(1,2)
        self.num_2 = Im_numbers(1,2)
    
    def test_sum(self):
        result = Im_numbers.add_Im(self.num_1,self.num_2)
        self.assertAlmostEqual(result.Re, 2)
        
    def test_div(self):
        result = Im_numbers.div_Im(self.num_1,self.num_2)
        self.assertAlmostEqual(result.Im, 0)


if __name__ == "__main__":
    unittest.main()