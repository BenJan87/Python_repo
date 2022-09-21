string = "ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB"



blank = ""
for el in string:
    if el == "A":
        blank += "1"
    else:
        blank += "0"
print(blank)