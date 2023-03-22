import itertools

data = input()
list1 = []
list1[:0] = data
groups = itertools.groupby(data)

for key, group in groups:
    print(f"({len(list(group))}, {key})", end=" ")