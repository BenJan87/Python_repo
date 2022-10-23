import re
string = "       pierwszy drugi  czwarty  drugi    "
res = re.findall(r'^\s+\S+', string)
if res:
    res += re.findall(r'\S+', string)[1:]
else:
    res = re.findall(r'\S+', string)

print(res)