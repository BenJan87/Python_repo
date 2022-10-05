N = int(input("Podaj liczbę N: "))
#Sprawdzanie czy liczba jest pierwsza
def is_prime_num(a):
    for i in range(2, a):
        if a % i == 0:
            return False
        return True

#Tworzenie listy liczb pierwszych mniejszych od n
def halprime_numbers(N):
    prime_num_list = [i for i in range(N) if is_prime_num(i) is True]
    prime_num_list.append(2)
    

    #Tworzenie listy z iloczynami liczb pierwszych (tych samych) do N
    multi_same_list = [prime_num_list[i]*prime_num_list[i] for i in range(len(prime_num_list)) if prime_num_list[i]*prime_num_list[i] < N ]

    #Tworzenie liczby z iloczynami liczb pierwszych (różnych) do N
    multi_dif_list = [prime_num_list[i]*prime_num_list[j] for i in range(len(prime_num_list)) for j in range(len(prime_num_list)) if prime_num_list[i]*prime_num_list[j] < N]
    for same_number in multi_dif_list:
        if same_number in multi_same_list:
            multi_dif_list.remove(same_number)
    
    return sorted(set(multi_dif_list)), sorted(multi_same_list)
    
    
print("Twoja listy to: ")
print(halprime_numbers(N))



