

#checking the cool and bad numbers, then printing the happiness



def happiness(main, cool, bad):
    hap = 0
    
    for el in main:
        if el in cool:
            hap += 1
        elif el in bad:
            hap -= 1
    
    return hap        

if __name__ == "__main__":
    useless = input()
    
    main = list(map(int, input().split()))
    cool = set(map(int, input().split()))
    bad = set(map(int, input().split()))
    
    print(happiness(main, cool, bad))