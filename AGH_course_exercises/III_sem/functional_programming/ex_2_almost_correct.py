from collections import Counter as ctr;data = ""; 
while True: 
    try:
        data += " " + input() 
    except(EOFError):
        print(ctr(list(map(lambda el: len(el), data.split()))).most_common());exit()