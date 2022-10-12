import shop
import unittest

magazine = [['tomato', 1000],
                ['cucumber', 500],
                ['carrot', 250]]

buyers_list = []

class Test_TestSum(unittest.TestCase):
    

    # def test_selling(self):
    #     self.assertTrue(shop.selling('tomato', 5, 'Harry', magazine, buyers_list),  )


    def test_get_input(self):
        with self.assertRaises(ValueError):
            shop.get_input()


if __name__ == '__main__':
    unittest.main()