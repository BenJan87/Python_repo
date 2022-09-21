import random
t = str(input("Czy chcesz wporwadzić własny ciąg? (Y/N): "))
exam_seq = []
if t == "Y" or t == "y":
    while t == "Y" or t == "y":
        x = int(input("Podaj liczbę całkowitą: "))
        print()
        exam_seq.append(x)
        t = str(input("Wpisz 'Y' jesli chcesz dodać kolejną liczbę \n 'N' jeśli chcesz zakończyc dodawanie liczb do listy: "))

    print("Twój ciąg to:", exam_seq)
    tmp = [exam_seq[0]]
    seq_2 = []

    for i in range((int(len(exam_seq)))-1):
        # Wszystkie ciągi rosnące:
        if exam_seq[i+1]>exam_seq[i]:
            tmp.append(exam_seq[i+1])
        # Wszystkie listy tymczasowe
        if len(tmp)>len(seq_2):
            seq_2 = tmp
        # Wybranie najdłuższej listy / nastepny wyraz ciągu jest mniejszy lub równy
        if exam_seq[i+1]<exam_seq[i]:
            tmp = [exam_seq[i+1]]

    print("Najdłuższy podciąg rosnący to: ")
    print(seq_2)

    print("Suma tego podciągu wynosi:")
    print(sum(seq_2))






#Losowy ciąg
print("Dowolnie wylosowany ciąg")
n = int(input("Podaj długość listy: "))
m = int(input("Podaj górna granicę zakresu: "))
l = int(input("Podaj dolna granicę zakresu: "))
   
    
sequence = []   

while len(sequence) < n:
    x = random.randint(l, m)
    sequence.append(x)
print()
print("Ciąg wszystkich wyrazów:", sequence)

tmp = [sequence[0]]
seq_2 = []

for i in range(n-1):
    # Wszystkie ciągi rosnące:
    if sequence[i+1]>sequence[i]:
        tmp.append(sequence[i+1])
    # Wszystkie listy tymczasowe
    if len(tmp)>len(seq_2):
        seq_2 = tmp
    # Wybranie najdłuższej listy / nastepny wyraz ciągu jest mniejszy lub równy
    if sequence[i+1]<sequence[i]:
        tmp = [sequence[i+1]]

print("Najdłuższy podciąg rosnący to: ")
print(seq_2)

print("Suma tego podciągu wynosi:")
print(sum(seq_2))

