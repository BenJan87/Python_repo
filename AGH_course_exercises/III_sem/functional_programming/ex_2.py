from collections import Counter as ctr;data = ""; 
while True: data += " " + input() if data[-4:] != "exit" else print(ctr(list(map(lambda el: len(el), data.split()[:-1]))).most_common())