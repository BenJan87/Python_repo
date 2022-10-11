import unittest
from printing_prime_numbers import prime

class Prime_Test(unittest.TestCase):

    def test_prime(self):
        result_prime = [2, 3, 5, 7, 11, 13, 17, 19]
        for number in result_prime:    
            self.assertEqual(prime(number), True)

    def test_not_prime(self):
        result_not_prime = [4, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20]
        for number in result_not_prime:
            self.assertEqual(prime(number), False)

    def test_negative(self):
        result_negative = [-1, -5, -6 -9]
        for number in result_negative:
            self.assertEqual(prime(number), False)

    def test_bin(self):
        result_bin = [0, 1]
        for number in result_bin:
            self.assertEqual(prime(number), False)


if __name__=="__main__":
    unittest.main()