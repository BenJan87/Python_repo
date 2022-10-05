# while True:
#     n = int(input("Wpsiz liczbę naturalną dodatnią: "))
#     if n > 0:
#         break

# def factorial(n):
#     n = int(n)
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n*int(factorial(n-1))

# def sum(n):
#     n = int(n)
#     if n == 2:
#         return [ 1 for i in range(n) ]
#     else:
#         x = [1 for i in range(n-1)]
#         x.append(n-a)
        
#     return
        
        

# print(sum(n))


def one_list(n):
    x = [1 for i in range(n)]
    return x


# def summand(ones):
#     flag = 0
#     for element1 in ones[-1]:
#         new_list = []
        
#         for element2 in ones[-1][ones[-1].index(element1) + 1:]:
#             new_list.append(element1 + element2)
            
#             if len(ones[-1]) >= 3:
#                 for i in range(len(ones[-1]) - 2):
#                     new_list.append(1)
#             ones.append(new_list)
#             if not element1 > element2:
#                 flag = 1
#                 break
#             if len(new_list) > 2:
#                 summand(ones)
#             break
#         if flag == 1:
#             break
#     if len(new_list)> 2:
#         summand(ones)                
#     return ones


# print(summand(one_list(4)))


# def summand(ones):
#     flag = 0
#     tmp_list = []
#     for list in ones:
#         for i in range(len(list)):
#             new_list = []
#             for element1, element2 in zip(list, list[1:]):
#                 if flag % (len(list)) == 0:
#                     new_list.append(element1 + element2)
#                 if flag % (len(list)) != 0:
#                     new_list.append(element2)
#                 flag += 1
#             tmp_list.append(new_list)
#     for list in tmp_list:
#         ones.append(list)
#     if len(ones[-1]) > 2:
#         summand(ones)
#     return ones

# print(summand(one_list(5)))

# for list in 


def summand(a, x):
    tmp_ones_list = one_list(a)
    if len(one_list(a)) > 1:
        tmp_list = [tmp_ones_list[0]+tmp_ones_list[1]]
    else:
        pass
    while len(tmp_list) < a-1:
        tmp_list.append(1)
    if a==x:
        all_list = []
    all_list.append(tmp_list)
    if len(all_list) == x-2:
        return all_list
    else:
        return summand(a-1,x)
    
print(summand(4,4))

#Możliwa funkcja
def funkcja(n,x,all_list=""):
    if n == 1:
        return all_list

    tab=[1 for d in range(n-1)]

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












