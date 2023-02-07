import random

# for better performance, the two big primes are given
all_ASCII_chars = '''!"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~ '''

def extended_euclidean_algorithm(a, b):
    
    s, old_s = 0, 1
    t, old_t = 1, 0
    r, old_r = b, a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return old_r, old_s, old_t

def find_e_and_d(euler_fun):
    while True:
        e = random.randint(3, euler_fun - 1)
        gcd, x, d = extended_euclidean_algorithm(euler_fun, e)
        if gcd == 1:
            return e, d % euler_fun
        
def secret_into_ciphertext(message, e, n):
    return (message ** (e)) % n

def public_into_text(message, d, n):
    return (message ** (d)) % n

def string_into_numbers(given_str):
    number_str = ""

    for char in given_str:
        if char not in all_ASCII_chars:
            print("Incorrect characters were used")
            return "INCORRECT"
        
        base = str(ord(char))
        base_extended = base if len(base) == 3 else "0" + base

        number_str += base_extended 
        
    return int(number_str)

def numbers_into_string(number):
    mess = ""
    number = str(number)
    if len(number) % 3 != 0:
        number = "0" + str(number)

    i = 0
    while i != len(number)/3:
        print(number[i:i+3])
        char = chr(int(number[i:i+3]))
        mess += char
        i += 3

    return mess

if __name__ == "__main__":

    p = 461
    q = 353


    n = p * q
    euler_fun = (p - 1) * (q - 1)
    del p, q

    message = "lo"


    e, d = find_e_and_d(euler_fun)

    encrypted = public_into_text(string_into_numbers(message), d, n)
    
    print(encrypted)

    decrypted = numbers_into_string(secret_into_ciphertext(encrypted, e, n))

    print(decrypted)