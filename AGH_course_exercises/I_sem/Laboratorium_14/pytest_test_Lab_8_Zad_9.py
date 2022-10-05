import pytest
from Lab_8_Zad_9 import is_prime_num
from Lab_8_Zad_9 import halprime_numbers
    
class Test_Prime_num:
    def test_is_prime_num(self):
        result = is_prime_num(3)
        assert result is True
        
    def test_det(self):
        result = halprime_numbers(19)
        assert result == ([6, 10, 14, 15, 18], [4, 9])

