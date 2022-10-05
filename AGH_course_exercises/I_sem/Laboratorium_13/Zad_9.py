def funkcja(n,x,all_list=""):
    if n == 1:
        return all_list

    tab=[1 for i in range(n-1)]

    tab.append(x-len(tab))
    all_list += str(tab)
    if tab.count(x-n) > 1 and len(tab) != x:
        #do zapetlenia
        tab2 = []
        tab2.append(int(tab.count(x-n)))
        tab2.append(x-len(tab) + (x-n))
        all_list += str(tab2)

    return funkcja(n-1,x,all_list)

x = int(input("Podaj liczbę: "))
print(funkcja(x,x))