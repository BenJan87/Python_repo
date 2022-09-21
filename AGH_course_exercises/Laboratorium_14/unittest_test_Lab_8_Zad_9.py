import unittest
from Lab_8_Zad_9 import is_prime_num
from Lab_8_Zad_9 import halprime_numbers
    
class LearnTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.a = 21
        self.b = 14
    
    def test_multi(self):
        result = is_prime_num(self.b)
        self.assertIs(result, True)
        
    def test_div(self):
        result = halprime_numbers(14)
        self.assertAlmostEqual(result, ([6, 10], [4, 9]))

if __name__ == "__main__":
    unittest.main()