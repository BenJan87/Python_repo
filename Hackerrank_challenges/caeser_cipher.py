
#ceaser_cipher conversion:

def caesarCipher(s, k):
    alf_l = 'abcdefghijklmnopqrstuvwxyz'
    alf_u = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    k = k % len(alf_l)
    temp_l = alf_l[k:]+alf_l[:k]
    temp_u = alf_u[k:]+alf_u[:k]
    
    res = ""
    for element in s:
        if element in alf_l:
            res += temp_l[alf_l.index(element)]
        elif element in alf_u:
            res += temp_u[alf_u.index(element)] 
        else:
            res += element
    print(res)
    

    

if __name__ == '__main__':

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)