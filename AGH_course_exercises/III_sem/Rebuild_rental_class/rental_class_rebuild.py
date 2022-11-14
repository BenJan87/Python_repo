from date_class import Own_date
class Rental():
    ID_BIKES, ID_CLIENT = 0, 0
    r_bicycles = []
    transactions = []
    r_clients = []

    @staticmethod
    def add_bike_to_magazine(model, cost) -> None:
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
    
    @staticmethod #printing all the clients
    def clients() -> str:
        new_str = ''
        for el in Rental.r_clients:
            new_str += f'{el.id:15} {el.name:15} {el.surname:15} {el.address}\n'
        return new_str

    @staticmethod #printing all the transactions
    def rental() -> str:
        new_str = ''
        for el in Rental.transactions:
            new_str += f'{el[0]:15} {el[1]:15} {el[2]}\n'
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

    def __repr__(self): # printing the correct code
        return '''
        def __init__(self, id_client, model):
        self.id_bike = Rental.ID_BIKES + 1 
        self.id_client = id_client 
        self.model = model 
        self._cost = None 
        self._date_rent = None 
        self._date_return = None 
        Rental.ID_BIKES += 1
        '''

    def __str__(self):
        new_str = ''
        for el in Rental.r_bicycles:
            new_str += f'{el.id_bike:15} | {el.model:15} | {el.cost}\n'
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
            self._cost = given_cost_pm
        except:
            print("Incorrect cost was given")

    @property
    def date_rent(self):
        return self._date_rent
    
    @date_rent.setter
    def date_rent(self, date):
        self._date_rent = date

    @property
    def date_return(self):
        return self._date_return
    
    @date_return.setter
    def date_return(self, given_date):
        self._date_return = given_date

class Client():
    def __init__(self):
        self.id = Rental.ID_CLIENT + 1
        self.name = ""
        self.surname = ""
        self.address = ""
        Rental.ID_CLIENT += 1

    def __str__(self): #printing the client
        return f'{self.name:15} {self.surname:15} {self.address}'


# if __name__ == "__main__":
#     while True: