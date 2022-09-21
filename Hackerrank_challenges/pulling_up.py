def block(stc, n):
    last = 2**31+1
    
    for i in range(n):
        if stc[0] < stc[-1]:
            if last >= stc[-1]:
                last = stc[-1]
                stc.pop(-1)
            else:
                return "No"
        
        else:
            if last >= stc[0]:
                last = stc[0]
                stc.pop(0)
            else:
                return "No"   
    
    return "Yes"






if __name__ == "__main__":
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        stc = list(map(int, input().split()))
        
        print(block(stc, n))