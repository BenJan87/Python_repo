def solve(s):
    s = [i for i in s]
    
    for i in range(1, len(s)):
        if s[i-1] == " ":
            s[i] = s[i].upper()

    s[0] = s[0].upper()
    
    x = ""
    for i in s:
        x += i 
    print(x)



solve("3adam lincoln")