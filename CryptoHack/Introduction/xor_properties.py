from binascii import unhexlify
key_1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
key_23 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
# KEY2 = KEY1 ^ KEY23
best = "04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf"

def str_xor(s1, s2):
    return "".join(format(int(a, 16) ^ int(b, 16), "x") for a, b in zip(s1, s2))

fst = str_xor(best, key_1)
flag = str_xor(fst, key_23)
print(unhexlify(flag))