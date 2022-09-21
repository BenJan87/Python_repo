file = open("C:\\Users\\benja\\OneDrive\\Pulpit\\zer_one.txt", "r")
line_count = 0
while True:
    tmp = file.readline()
    if tmp == "":
        break
    zer_count = 0
    one_count = 0
    for el in tmp:
        if el == "0":
            zer_count += 1
        elif el == "1":
            one_count += 1
    if zer_count % 3 == 0 and zer_count != 0 or one_count % 2 == 0 and one_count != 0:
        line_count += 1

print(line_count)