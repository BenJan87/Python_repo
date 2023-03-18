#xor with two strings:
def str_xor(s1, s2):
    return "".join(format(int(a, 16) ^ int(b, 16), "x") for a, b in zip(s1, s2))


print(str_xor('1f-Q3IrofIsUCihVz9/SiXwovQxjBc', 'a-2IcdlA00nFXqfUAH6gFXnXpWC0Y'))