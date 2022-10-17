import unittest
from skrypt_ex_2 import recognize_string


class Test_TestShopping(unittest.TestCase):

    def test_regex(self):
        self.assertEqual(recognize_string('Pies'), ['Wyraz: Pies'])
        self.assertEqual(recognize_string('20'), ['Liczba: 20'])
        self.assertEqual(recognize_string("20kotow5"), ['Liczba: 20', 'Wyraz: kotow', 'Liczba: 5'])
        self.assertEqual(recognize_string('ąłżć'), ['Wyraz: ąłżć'])

        
if __name__ == '__main__':
    unittest.main()