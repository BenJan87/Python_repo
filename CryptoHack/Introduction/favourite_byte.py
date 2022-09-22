data = "73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
arr_str = [el for el in bytes.fromhex(data)]
arr = []
for i in range(256):
    emp = [i ^ el for el in arr_str]
    emp = [chr(el) for el in emp]
    arr.append("".join(emp))
for el in arr:
    if el.startswith("crypto"):
        print(el)