import pytest
from Lab12_Zad_5 import Im_numbers
    
class Test_Im_numbers:
    
    def setup(self):
        self.num_1 = Im_numbers(1,2)
        self.num_2 = Im_numbers(1,2)

    def test_sum(self):
        result = Im_numbers.add_Im(self.num_1,self.num_2)
        assert result.Re == 2
        
    def test_is_not(self):
        result_div = Im_numbers.div_Im(self.num_1,self.num_2)
        result_sub = Im_numbers.sub_Im(self.num_1,self.num_2)
        assert result_div is not result_sub