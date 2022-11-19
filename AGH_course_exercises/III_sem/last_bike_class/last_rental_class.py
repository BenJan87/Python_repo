from date_class import Own_date
from abc import ABC, abstractmethod
from copy import deepcopy
# 15 km/h is the speed
class Rental():
    ID_BIKE, ID_ELECTRIC, ID_CLIENT = 0, 0, 0
    r_vehicles = []
    transactions = []
    r_clients = []

    @staticmethod
    def add_to_magazine(model, cost, veh_type) -> None:
        if veh_type == "Bike":
            vehicle = Bicycle(0, model)
        else:
            vehicle = Electric(0, model)

        vehicle.type = veh_type 
        vehicle.cost = cost
        Rental.r_vehicles.append(vehicle)
    
    @staticmethod
    def rent_a_bike(id_client, model, date_rent, veh_type) -> bool:
        arr = Rental.r_vehicles
        for i in range(len(arr)):
            if arr[i].model == model and not arr[i].date_rent and arr[i].type == veh_type:
                arr[i].id_client = id_client
                arr[i].date_rent = date_rent
                return True
        return False

    @staticmethod
    def returning_a_bike(client, date_return, model, veh_type) -> bool:
        arr = Rental.r_vehicles
        for i in range(len(arr)):
            if arr[i].id_client == client.id and arr[i].date_rent and arr[i].model == model and arr[i].type == veh_type:
                tmp_vehicle = deepcopy(arr[i])
                tmp_vehicle.date_return = date_return
                
                arr[i].history.append([client.name, client.surname, tmp_vehicle.date_rent, date_return])
                client.history.append(tmp_vehicle)

                cost = (date_return - arr[i].date_rent) * arr[i].cost
                if arr[i].type == "Scooter":
                    km = round(15/60*(date_return - arr[i].date_rent), 2)
                    tmp_arr = [client.id, arr[i].model, cost, km]
                    arr[i].history[-1].append(km)
                else:
                    tmp_arr = [client.id, arr[i].model, cost]

                Rental.transactions.append(tmp_arr)

                arr[i].id_client = 0
                arr[i].date_rent = None
                arr[i].date_return = None
                return True
        return False
    

    def __str__(self):
        basic = ""
        for veh in Rental.r_vehicles:
            x = sum([el[4] for el in veh.history if len(el) == 5])

            name = [veh.history[i][0] +" "+ veh.history[i][1] for i in range(len(veh.history))]
            basic += f"{veh.model:20} {name if not veh.id_client and name else ''} {x if x else ''}\n"
        return basic

    # @staticmethod #printing all the clients
    # def clients() -> str:
    #     new_str = ''
    #     for el in Rental.r_clients:
    #         new_str += f'{el.id:15} {el.name:15} {el.surname:15} {el.address}\n'
    #     return new_str

    # @staticmethod #printing all the transactions
    # def rental() -> str:
    #     new_str = ''
    #     for el in Rental.transactions:
    #         new_str += f'{el[0]:15} {el[1]:15} {el[2]}\n'
    #     return new_str
    
class Vehicle(ABC):
    def __init__(self, id_client, model):
        self.id_veh = None #
        self.id_client = id_client #
        self.model = model #
        self._cost = None #per minute
        self.date_rent = None #
        self.date_return = None #
        self.type = None
        self.history = []

    def __str__(self):
        tmp = self.history
        for el in self.history:
            basic += f"{tmp[0]} {tmp[1]:15} {tmp[2].hour}:{tmp[2].minute} {tmp[3].hour}:{tmp[3].minute}"

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

class Bicycle(Vehicle):
    def __init__(self, id_client, model):
        super().__init__(id_client, model)
        self.id_veh = Rental.ID_BIKE + 1
        self.type = "Bike"
        self.history = []
        Rental.ID_BIKE + 1
    
    def __str__(self):
        s = ""
        basic = f"Name:{s:15} KM:{s:10} Dates:\n"
        for tmp in self.history:
            basic += f"{tmp[0]:10} {tmp[1]:10} {tmp[2].hour}:{tmp[2].minute} {tmp[3].hour}:{tmp[3].minute}"
        return basic

class Electric(Vehicle):
    def __init__(self, id_client, model):
        super().__init__(id_client, model)
        self.id_veh = Rental.ID_ELECTRIC + 1
        self.kilometers = []
        self.type = "Scooter"
        Rental.ID_ELECTRIC + 1

    def __str__(self):
        s = ""
        basic = f"Name:{s:15} KM:{s:10} Dates:\n"
        for tmp in self.history:
            basic += f"{tmp[0]:10} {tmp[1]:10} {tmp[4]} {tmp[2].hour:10}:{tmp[2].minute} {tmp[3].hour}:{tmp[3].minute}\n"
        return basic
        
class Client():
    def __init__(self, name, surname, address):
        self.id = Rental.ID_CLIENT + 1
        self.name = name
        self.surname = surname
        self.address = address
        self.history = []
        Rental.ID_CLIENT += 1
        Rental.r_clients.append(self)

    def add_to_r_clients(self):
        Rental.r_clients.append(self)

    def __str__(self): #printing the client
        return f'{self.name:15} {self.surname:15} {self.address}'