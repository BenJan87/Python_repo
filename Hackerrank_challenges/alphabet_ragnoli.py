alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def print_rangoli(size):
    alpha = alphabet[:size]
    net = [["-" for _ in range(4*size-3)] for _ in range(2*size - 1)]
    center_cords=[size-1,2*size-2]
    net[center_cords[0]][center_cords[1]] = "a"
    dig_net(size, net)
    # for i in range(net(len)):
    view(net)

def dig_net(size, net, center="a"):
    center_cords = [[i, j] for i in range(len(net)) for j in range(len(net)) if net[i][j] == center]
    i, j = center_cords[0][0], center_cords[0][1] #cetner cords
    for k in range(size-1):
        net[k][i]



    print(center_cords)

def view(net):
    for i in range(len(net)):
        for j in range(len(net[0])):
            print(net[i][j], end="")
        print("", end="\n")

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)