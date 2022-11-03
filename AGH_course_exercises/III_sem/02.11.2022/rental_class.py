class Rental():    

    @staticmethod
    def parse_file_line(file, magazine):
        try:
            with open(file, 'r') as magazine_file:
                lines = magazine_file.readlines()
        except:
            print("File not found or not available")
            return False

        for line in lines:
            line_list = line.split("_")
            
            try:
                if len(line_list) != 3:
                    raise ValueError
                bike_into_magazine = {'model': line_list[0], 
                                      'amount': int(line_list[1]),
                                      'cost_per_min': float(line_list[2])}

                if bike_into_magazine['amount'] <= 0 or bike_into_magazine['amount'] < 0:
                    raise TypeError            
            except(ValueError):
                print("Not correct format")
                return False
            except(TypeError):
                print("Not enough amount")
                return False
            magazine.append(bike_into_magazine)
            
        return magazine


    @staticmethod
    def parse_input_line():
        
        class CustomError(Exception):
            pass
        
        try:
            mode = input("Choose: 1 - rent a bike, 2 - return a bike:\n")
            if mode not in ["1", "2"]:
                print("Please give proper action\n")
                raise CustomError()
            mode = int(mode)
            
            biker = input("Insert biker: ").split("_")
            if len(biker) != 3:
                print("Incorrect input\n")
                raise CustomError()

            tmp_time = biker[2].split(":")

            int_time = [int(el) for el in tmp_time]
            if len(int_time) != 2 or int_time[0] > 23 or int_time[0] < 0 or int_time[1] < 0 or int_time[1] > 59:
                raise ValueError
            
            biker_person = ({'person': biker[0],
                            'model': biker[1],
                            'time_hour': int_time[0], 
                            'time_minute': int_time[1], 
                            'mode': mode})
            return biker_person
                
        except(ValueError):
            print("Incorrect time insertion\n")
        except(CustomError):
            pass

        return False


    @staticmethod
    def renting(magazine, biker, buyer_list):
        if_bike_existing = False
        i = 0
        for bike in magazine:
            if biker['model'] == bike['model']:
                if bike['amount'] == 0:
                    print("No bikes left")
                    return False
                else:
                    if_bike_existing = True
                    magazine[i]['amount'] -= 1 
                    break
            i += 1
                    
        if not if_bike_existing:
            print("There is no given model")
            return False

        time_st_h, time_st_m = biker['time_hour'], biker['time_minute']
        time_end_h, time_end_m = "Not returned", "Not returned"
            
        buyer_list.append({'who': biker['person'],
                           'model': biker['model'],
                           'time_st_h': time_st_h,
                           'time_st_m': time_st_m,
                           'time_end_h': time_end_h,
                           'time_end_m': time_end_m,
                           'cost': 0})
        print("Bike rented")
        return [magazine, buyer_list] 
    

    @staticmethod
    def returning(magazine, biker, buyers_list):
        if_purchase_exist = False
        for buyer in buyers_list:
            if buyer['who'] == biker['person'] and buyer['model'] == biker['model']:
                if_purchase_exist = True
                buyer['time_end_h'] = biker['time_hour']
                buyer['time_end_m'] = biker['time_minute']
                tmp_model = buyer['model']

                for bike in magazine:
                    if bike['model'] == tmp_model:
                        bike['amount'] += 1
                        money_per_min = bike['cost_per_min']
                        break

                if (buyer['time_end_h'] == buyer['time_st_h'] and buyer['time_st_m'] > buyer['time_end_m']) or buyer['time_end_h'] < buyer['time_st_h']:
                    print("incorrect returning time")
                    return False
                
                buyer['cost'] = ((60*(buyer['time_end_h']) + buyer['time_end_m']) - (buyer['time_st_h']*60 + buyer['time_st_m'])) * money_per_min
                break

        if not if_purchase_exist:
            print("There is no transaction")
            return False

        print("Bike returned")
        return [magazine, buyers_list]


if __name__ == "__main__":
    magazine, tmp_magazine, buyers_list = [], [], []
    try:
        file = input("Give magazine file: ")
    except(EOFError):
        print("Exiting...")
        exit(1)

    while True:
        tmp_magazine = Rental.parse_file_line(file, magazine)
        if tmp_magazine:
            break
        file = input("Give correct magazine file: ")
    magazine = tmp_magazine

    try:
        while True:
            biker = Rental.parse_input_line()
            if not biker:
                continue

            if biker['mode'] == 1:
                result_renting = Rental.renting(magazine, biker, buyers_list)
                if not result_renting:
                    continue
                magazine, buyers_list = result_renting[0], result_renting[1]

            else:
                result_returning = Rental.returning(magazine, biker, buyers_list)
                if not result_returning:
                    continue
                magazine, buyers_list = result_returning[0], result_returning[1]

    except(EOFError):
        for el in magazine:
            print(f"Model: {el['model']}, Amount: {el['amount']}")
        print()
        for el in buyers_list:
            print(f"User: {el['who']}, Model:{el['model']}, Cost:{el['cost']}")
            print(f"Rent time: h {el['time_st_h']} - m {el['time_st_m']}, Return time: h {el['time_end_h']} - m {el['time_end_m']}")
            print()