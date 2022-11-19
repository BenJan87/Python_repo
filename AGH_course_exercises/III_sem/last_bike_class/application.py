from date_class import Own_date
from last_rental_class import Vehicle, Bicycle, Electric, Rental, Client


# adding vehs to magazine:
Rental.add_to_magazine("Bolt", 4, "Scooter")
Rental.add_to_magazine("Xiaomi", 2, "Scooter")
Rental.add_to_magazine("Merida", 5, "Bike")
Rental.add_to_magazine("Kross", 3, "Bike")

# adding clients:
id_1 = Client("Jan", "Kowalski", "Warszawa") # -> Bolt
id_2 = Client("Anrzej", "Woźniak", "Gliwice") # -> Xiaomi
id_3 = Client("Euzebiusz", "Kasielski", "Katowice") # -> Kross

# Renting vehs:
Rental.rent_a_bike(1, "Bolt", Own_date(15, 0), "Scooter")
Rental.rent_a_bike(2, "Xiaomi", Own_date(16, 0), "Scooter")
Rental.rent_a_bike(3, "Kross", Own_date(17, 0), "Bike")

# returning bikes
Rental.returning_a_bike(id_1, Own_date(17, 0), "Bolt", "Scooter")
Rental.returning_a_bike(id_2, Own_date(17, 0), "Xiaomi", "Scooter")
Rental.returning_a_bike(id_3, Own_date(20, 0), "Kross", "Bike")

Rental.rent_a_bike(3, "Bolt", Own_date(16, 0), "Scooter")
Rental.returning_a_bike(id_3, Own_date(17, 0), "Bolt", "Scooter")

print(Rental.r_vehicles[0]) # printing bike_1
print(Rental.r_vehicles[1])
print(Rental())