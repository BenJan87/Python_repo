from date_class import Own_date
class Rental():
    ID_BIKES, ID_CLIENT = 0, 0
    r_bicycles = []
    transactions = []
    r_clients = []

    @staticmethod
    def add_to_magazine_bike(model, cost) -> None:
        bike = Bicycle(0, model)
        bike.cost = cost
        if not bike.cost:
            print("Somethong wrong, again...\n")
            return
        Rental.r_bicycles.append(bike)
    
    @staticmethod
    def rent_a_bike(id_client, model, date_rent) -> bool:
        arr = Rental.r_bicycles
        for i in range(len(arr)):
            if arr[i].model == model and not arr[i].date_rent:
                arr[i].id_client = id_client
                arr[i].date_rent = date_rent
                return True
        return False

    @staticmethod
    def returning_a_bike(id_client, date_return) -> bool:
        arr = Rental.r_bicycles
        for i in range(len(arr)):
            if arr[i].id_client == id_client and arr[i].date_rent:
                arr[i].date_return = date_return
                
                tmp_arr = [id_client, arr[i].model, (date_return - arr[i].date_rent) * arr[i].cost]
                Rental.transactions.append(tmp_arr)

                arr[i].id_client = 0
                arr[i].date_rent = None
                arr[i].date_return = None
                return True
        return False
    
    @staticmethod
    def clients():
        new_str = ''
        for el in Rental.r_clients:
            new_str += f'{el.id:10} {el.name:30} {el.surname:30} {el.address}\n'
        return new_str

    @staticmethod
    def rental():
        new_str = ''
        for el in Rental.transactions:
            new_str += f'{el[0]:10} {el[1]:20} {el[2]}\n'
        return new_str
    
class Bicycle():
    def __init__(self, id_client, model):
        self.id_bike = Rental.ID_BIKES + 1 #
        self.id_client = id_client #
        self.model = model #
        self._cost = None #per minute
        self._date_rent = None #
        self._date_return = None #
        Rental.ID_BIKES += 1

    def __repr__(self):
        return '''
        def __init__(self, id_client, model):
        self.id_bike = Rental.ID_BIKES + 1 #
        self.id_client = id_client #
        self.model = model #
        self._cost = None #per minute
        self._date_rent = None #
        self._date_return = None #
        Rental.ID_BIKES += 1
        '''

    def __str__():
        new_str = ''
        for el in Rental.r_bicycles:
            new_str += f'{el.id_bike:10} | {el.model:10} | {el.cost}\n'
        return new_str

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, given_cost_pm):
        try:
            given_cost_pm = float(given_cost_pm)
            if given_cost_pm < 0:
                raise
        except:
            print("Incorrect cost was given")

    @property
    def date_rent(self):
        return self._date_rent
    
    @date_rent.setter
    def date_rent(self, given_hour, given_minute):
        while True:
            try:
                given_hour, given_minute = int(given_hour), int(given_minute)
                tmp_date = Own_date()
                tmp_date.minute = given_minute
                tmp_date.hour = given_hour
                break
            except:
                pass

    @property
    def date_return(self):
        return self._date_return
    
    @date_return.setter
    def date_return(self, given_hour, given_minute):
        while True:
            try:
                given_hour, given_minute = int(given_hour), int(given_minute)
                tmp_date = Own_date()
                tmp_date.minute = given_minute
                tmp_date.hour = given_hour
                break
            except:
                pass

class Client():
    def __init__(self):
        self._id = Rental.ID_CLIENT + 1
        self.name
        self.surname
        self.address
        Rental.ID_CLIENT += 1

    def __str__(self):
        return f'{self.name:30} {self.surname:30} {self.address}'


# if __name__ == "__main__":
#     while True: