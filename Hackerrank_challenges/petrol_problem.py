def trans(arr, i):
    return arr[i:len(arr)] + arr[:i]

def truckTour(petrolpumps):
    global n
    
    for i in range(n):
        route = trans(petrolpumps, i)
        cur = 0
        flag = 0
        for j in range(n):
            cur += route[j][0] - route[j][1] 
            if cur < 0:
                flag = 1
                break
        if flag == 0:
            return i

n = 3
print(truckTour([[1, 5], [10, 3],[3, 4]]))