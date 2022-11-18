# one
from sys import argv;print(list(filter(lambda x: x % 2 == 0, [int(el) for sublist in [line.strip().split() for el in argv[1:] for line in open(el, 'r')] for el in sublist])))

# For better understanding:
# from sys import argv
# res = list(filter(lambda x: x % 2 == 0, [int(el) for sublist in [line.strip().split() for el in argv[1:] for line in open(el, 'r')] for el in sublist]))
# print(res)
