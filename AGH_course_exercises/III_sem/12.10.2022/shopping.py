
magazine = [{'product': "Tomato", 'amount': 50},
            {'product': "Orange", 'amount': 100},
            {'product': "Apple", 'amount': 40},
            {'product': "Pumpkin", 'amount': 20}]

buyers_list = []

def selling_from_magazine(magazine, buyers_list, product, count, user):
    if count <= 0:
        print("Amount is not positive")
        return False

    for position in magazine:
        if position['product'] == product:
            if count > position['amount']:
                print("There is not enough products in magazine (in magazine: {})".format(position['amount']))
                return False
            position['amount'] -= count
            buyers_list.append({'product': product, 'amount': count, 'user': user})
            return [magazine, buyers_list]
                
    print("There is no product in magazine")
    return False    


def returning_to_magazine(magazine, product, count):
    if count <= 0:
        print("Amount is not positive")
        return False
    for position in magazine:
        if position['product'] == product:
            position['amount'] += count
            return magazine
        
    magazine.append({'product': product, 'amount': count})
    return magazine


if __name__ == "__main__":
    while True:
        try:
            try:
                operation = int(input('Choose operation (1-buy product, 2-return product): '))
                if operation not in [1,2]:
                    print("Insert correct number of operation")
                    continue
                product = input("Give product name: ")
                count = float(input("Give amount of a product: "))
                if count % 1 != 0:
                    raise ValueError
                # selling operation
                if operation == 1:
                    user = input("Give buyer name: ")
                    result = selling_from_magazine(magazine, buyers_list, product, int(count), user)
                    if not result:
                        continue
                    else:
                        magazine, buyers_list = result[0], result[1]
                        continue
                # returning operation
                result = returning_to_magazine(magazine, product, int(count))
                if result:
                    magazine = result
            except(ValueError):
                print("Incorrect insertion type, please do the operation once again:")

        except(EOFError):
            print("\nMagazine status:")
            for el in magazine:
                print(el)
            print("\nBuyers list:")
            for el in buyers_list:
                print(el)
            exit()