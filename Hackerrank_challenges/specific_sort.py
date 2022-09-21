#sotring in given order: lower, upper, odd, even

def div(s):
    global upp
    global low
    global num
    
    s_u, s_l, odd, even = [], [], [], []
    
    for element in s:
        if element in num:
            if int(element) % 2 == 0:
                even.append(element)
            else:
                odd.append(element)
        elif element in low:
            s_l.append(element)
        else:
            s_u.append(element)
    
            
            
    x = sorted(s_l) + sorted(s_u) + sorted(odd) + sorted(even)
    res = ""
    for element in x:
        res += element

    return res
        
        
        
        
        
if __name__ == "__main__":
    upp = [chr(i) for i in range(65, 91)]
    low = [chr(i) for i in range(97, 123)]
    num = list(map(str, [i for i in range(10)]))
    
    print(div(input()))