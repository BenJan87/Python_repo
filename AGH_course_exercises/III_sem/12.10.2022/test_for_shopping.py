import unittest
from shopping import *


class Test_TestShopping(unittest.TestCase):
    # test for selling_from_magazine:
    
    def test_not_enough_products(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        buyers_list = []
        self.assertFalse(selling_from_magazine(magazine, buyers_list, 'Tomato', 60, 'Harry'), "amount is okay")

    def test_not_positive(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        buyers_list = []
        self.assertFalse(selling_from_magazine(magazine, buyers_list, 'Orange', -5, 'John'), "Number is positive")
        self.assertFalse(selling_from_magazine(magazine, buyers_list, 'Orange', 0, 'John'), "Number is positive")

    def test_not_existing_product(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        buyers_list = []
        self.assertFalse(selling_from_magazine(magazine, buyers_list, 'Banana', 20, 'Danny'))

    def test_sell_to_magazine(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        buyers_list = []

        res_magazine = [{'product': "Tomato", 'amount': 50},
                        {'product': "Orange", 'amount': 100},
                        {'product': "Apple", 'amount': 40},
                        {'product': "Pumpkin", 'amount': 15}]
        res_buyers_list = [{'product': "Pumpkin", 'amount': 5, 'user': 'Emily'}]

        self.assertEqual(selling_from_magazine(magazine, buyers_list, 'Pumpkin', 5, 'Emily'), [res_magazine, res_buyers_list])
    
    # tests for returning
    def test_returning_not_positive_amount(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        self.assertFalse(returning_to_magazine(magazine,'Orange', -5), "Number is positive")
        self.assertFalse(returning_to_magazine(magazine,'Orange', 0), "Number is positive")

    def test_return_to_magazine_with_existing_product(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        res_magazine = [{'product': "Tomato", 'amount': 50},
                        {'product': "Orange", 'amount': 100},
                        {'product': "Apple", 'amount': 100},
                        {'product': "Pumpkin", 'amount': 20}]
        self.assertEqual(returning_to_magazine(magazine, 'Apple', 60), res_magazine)

    def test_returning_to_magazine_with_not_existing_product(self):
        magazine = [{'product': "Tomato", 'amount': 50},
                {'product': "Orange", 'amount': 100},
                {'product': "Apple", 'amount': 40},
                {'product': "Pumpkin", 'amount': 20}]

        res_magazine = [{'product': "Tomato", 'amount': 50},
                        {'product': "Orange", 'amount': 100},
                        {'product': "Apple", 'amount': 40},
                        {'product': "Pumpkin", 'amount': 20},
                        {'product': "Banana", 'amount': 50}]
        self.assertEqual(returning_to_magazine(magazine, 'Banana', 50), res_magazine)


if __name__ == '__main__':
    unittest.main()