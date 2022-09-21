import unittest
from Lab_9_Zad_2 import multi_matrix
from Lab_9_Zad_2 import main_det
    
class LearnTest(unittest.TestCase):
    
    def setUp(self):
        print("SETUP Called...")
        self.mat1 = [[1,2,3],[4,5,6],[7,8,9]]
        self.mat2 = [[1,0,0],[0,1,0],[0,0,1]]
    
    def test_multi(self):
        result = multi_matrix(self.mat1,self.mat2)
        self.assertAlmostEqual(result, self.mat1)
        
    def test_div(self):
        result = main_det(self.mat1)
        self.assertIs(result, 0)


if __name__ == "__main__":
    unittest.main()

 