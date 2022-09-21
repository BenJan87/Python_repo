import pytest
from Lab_9_Zad_2 import multi_matrix
from Lab_9_Zad_2 import main_det
    
class Test_Matrixes:
    
    def test_multi(self):
        self.mat1 = [[1,2,3],[4,5,6],[7,8,9]]
        self.mat2 = [[1,0,0],[0,1,0],[0,0,1]]
        result = multi_matrix(self.mat1,self.mat2)
        assert result == self.mat1
        
    def test_det(self):
        self.mat3 = [[1,1],[3,4]]
        result = main_det(self.mat3)
        assert result == 1
        assert result == 1