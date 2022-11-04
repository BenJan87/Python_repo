import unittest
from rental_class import Rental

class Test_TestDay(unittest.TestCase):
    
    def test_parse_file_line(self):
        magazine_1 = [{'model': "B'twin", 'amount': 40, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 50, 'cost_per_min': 2.0},
                      {'model': "Kross", 'amount': 60, 'cost_per_min': 3.0},
                      {'model': "Shimano", 'amount': 70, 'cost_per_min': 4.0},
                      {'model': "Rockrider", 'amount': 80, 'cost_per_min': 5.0},
                      {'model': "Romet", 'amount': 90, 'cost_per_min': 6.0}]
        
        self.assertEqual(Rental.parse_file_line(r'02.11.2022\magazine.txt', []), magazine_1)
        self.assertFalse(Rental.parse_file_line('No_file_found', []))
        self.assertFalse(Rental.parse_file_line(r'02.11.2022\incorrect_magazine.txt',[]))
        self.assertFalse(Rental.parse_file_line(r'02.11.2022\incorrect_amounts.txt', []))

    def test_renting(self):
        magazine_2 = [{'model': "B'twin", 'amount': 0, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 50, 'cost_per_min': 2.0}]
        res_magazine = [{'model': "B'twin", 'amount': 0, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 49, 'cost_per_min': 2.0}]
            
        biker = {'person': "Ben", 'model': "Merida", 'time_hour': 17, 'time_minute': 0, 'mode': 1}
        biker_2 = {'person': "Adam", 'model': "Shimano", 'time_hour': 17, 'time_minute': 0, 'mode': 1}
        biker_3 = {'person': "Ben",'model': "B'twin", 'time_hour': 17, 'time_minute': 0, 'mode': 1}

        buyer_list = []
        res_buyer_list = [{'who': biker['person'],
                           'model': biker['model'],
                           'time_st_h': 17,
                           'time_st_m': 0,
                           'time_end_h': "Not returned",
                           'time_end_m': "Not returned",
                           'cost': 0}]

        self.assertEqual(Rental.renting(magazine_2, biker, buyer_list),[res_magazine, res_buyer_list])
        self.assertFalse(Rental.renting(magazine_2, biker_2, buyer_list))
        self.assertFalse(Rental.renting(magazine_2, biker_3, buyer_list))

    def test_returning(self):
        magazine_3 = [{'model': "B'twin", 'amount': 0, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 50, 'cost_per_min': 2.0}]
        res_magazine = [{'model': "B'twin", 'amount': 1, 'cost_per_min': 1.0},
                      {'model': "Merida", 'amount': 50, 'cost_per_min': 2.0}]

        biker = {'person': "Ben", 'model': "B'twin", 'time_hour': 18, 'time_minute': 0, 'mode': 2}
        biker_not_correct_time = {'person': "Ben", 'model': "B'twin", 'time_hour': 16, 'time_minute': 0, 'mode': 2}
        buyer_list = [{'who': biker['person'], 'model': biker['model'], 'time_st_h': 17, 'time_st_m': 0, 'time_end_h': "Not returned", 'time_end_m': "Not returned", 'cost': 0}]
        res_buyer_list = [{'who': biker['person'], 'model': biker['model'], 'time_st_h': 17, 'time_st_m': 0, 'time_end_h': 18, 'time_end_m': 0, 'cost': 60}]
        fake_buyer_list = []
        
        self.assertEqual(Rental.returning(magazine_3, biker, buyer_list),[res_magazine, res_buyer_list])
        self.assertFalse(Rental.returning(magazine_3, biker_not_correct_time, buyer_list), [res_magazine, res_buyer_list])
        self.assertFalse(Rental.returning(magazine_3, biker, fake_buyer_list), [res_magazine, res_buyer_list])

    def test_input(self):
        biker = {'person': "Ben", 'model': "B'twin", 'time_hour': 18, 'time_minute': 0, 'mode': 2}
        print("\nCorrect input:  name_model_hourTime:minuteTime - also give 2 as a mode\n")
        self.assertEqual(Rental.parse_input_line(), biker)

        print("\nTry put not enough data - e.g. only name and model")
        self.assertFalse(Rental.parse_input_line())
        
        print("\nTry put not correct action")
        self.assertFalse(Rental.parse_input_line())

        print("\nTry put inccorect time - e.g. 25 in hours")
        self.assertFalse(Rental.parse_input_line())
        

if __name__ == '__main__':
    unittest.main()