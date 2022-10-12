magazine = [['tomato', 1000],
                ['cucumber', 500],
                ['carrot', 250]]

buyers_list = []

def get_input():
    try:
        operation = int(input("Choose operation (1-sell, 2-return, 3-add_product_to_magazine): "))
        if operation not in [1, 2, 3]:
            raise ValueError
        return operation
    except:
        print("Give correct number")


def selling(product, count, user, magazine, buyers_list):
    for line in magazine:
        if product == line[0] and line[1] >= count:
            line[1] -= count
            buyers_list.append([product, count, user])
            return [magazine, buyers_list]
    print("Incorrect product or amount of product")


def returning(product, count, user, flag, magazine, buyers_list):
    for line in magazine:
        if line[0] == product:
            line[1] += count
            # for flag equals 1, client just returns the product
            # otherwise it is just add to magazine 
            if flag == 1:
                buyers_list.append([product, -count, user])
            return [magazine, buyers_list]

    magazine.append([product, count])
    if flag == 1:
        buyers_list.append([product, -count, user])
    return [magazine, buyers_list]
    


if __name__=="__main__":
    #if in buyers is "-30" it means that client returned the product 
    while True:
        try:
            operation = get_input()
            match operation:
                case 1:
                    res = selling(input("insert product: "), int(input("insert amount")), input("insert user"), magazine, buyers_list)
                    magazine, buyers_list = selling[0], selling[1]

        except(KeyboardInterrupt):
            print(magazine)
            print(buyers_list)
            break