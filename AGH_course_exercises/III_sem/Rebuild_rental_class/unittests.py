import unittest
from rental_class_rebuild import Rental, Bicycle, Client
from date_class import Own_date

class Test_Rental_Rebuild(unittest.TestCase):
    def test_add_bike_to_magazine(self):
        new_bicycle = Bicycle(0, "Merida")
        new_bicycle.cost = 2
        new_bicycle.id_bike = 2
        
        Rental.add_bike_to_magazine("Merida", 2)
        rental_bicycle = Rental.r_bicycles[0]

        new_bic_list = [new_bicycle.id_bike, new_bicycle.id_client, new_bicycle.cost, new_bicycle.model]
        ren_bic_list = [rental_bicycle.id_bike, rental_bicycle.id_client, rental_bicycle.cost, rental_bicycle.model]

        self.assertEqual(new_bic_list, ren_bic_list)
        Rental.ID_BIKES = 0
        Rental.r_bicycles = []
        # print("adding")

    def test_rent_a_bike(self):
        new_bike = Bicycle(0, "Merida")
        new_bike.cost = 2 
        # ID_bike = 1
        
        new_client = Client()
        new_client.name = "Jan"
        new_client.surname = "Kowalski"
        new_client.address = "Warszawa"

        new_date = Own_date()
        new_date.hour = 10
        new_date.minute = 30

        Rental.r_clients = [new_client]
        Rental.r_bicycles = [new_bike]
        Rental.rent_a_bike(1, "Merida", new_date)

        proper_bike = Bicycle(1, 'Merida')
        proper_bike.cost = 2
        proper_bike.id_bike = 1
        proper_bike.date_rent = new_date

        self.assertEqual([new_bike.id_bike, new_bike.id_client, new_bike.model, new_bike.cost, new_bike.date_rent.hour, new_bike.date_rent.minute],
                         [proper_bike.id_bike, proper_bike.id_client, proper_bike.model, proper_bike.cost, proper_bike.date_rent.hour, proper_bike.date_rent.minute])
        print("Bikes:")
        print(new_bike)
        print("Code for Bike:")
        print(repr(new_bike))

    def test_return(self):
        # print("Return")
        return_date = Own_date()
        return_date.hour = 12
        return_date.minute = 0

        Rental.returning_a_bike(1, return_date)
        print("Transactions:")
        print(Rental.rental())
        e_1, e_2, e_3 = 1, "Merida", 180.0
        self.assertEqual(Rental.rental(), f'{e_1:15} {e_2:15} {e_3}\n')
        print("Clients:")
        print(Rental.clients())
        


if __name__ == "__main__":
    unittest.main()