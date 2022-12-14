
class Plus():
    def __init__(self, center, size, cords):
        self.center = center
        self.size = size
        self.area = 4*size + 1
        self.cords = cords #do without center

def ch_even(grid):
    x, y = len(grid), len(grid[0])

    if x % 2 == 0:
        x = x//2-1
    else:
        x = x//2
    if y % 2 == 0:
        y = y//2-1
    else:
        y = y//2
    return x, y

def get_plus(grid, i, j):
    res = []
    max_it = min(ch_even(grid))
    cords = ([i, j], )
    for k in range(1, max_it + 1): #increasing size
        try:
            tmp = grid[i+k][j+k]
        except IndexError:
            break
        if i - k < 0 or j - k < 0 or grid[i-k][j] == "B" or grid[i+k][j] == "B" or grid[i][j-k] == "B" or grid[i][j+k] == "B":
            break
        cords += ([i, j-k], [i, j+k], [i-k, j], [i+k, j])
        print(cords)
        p = Plus([i, j], k, cords)
        # print(cords)
        res.append(p)
    return res

def all_pluses(grid):
    res = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "G":
                res.append(Plus([i, j], 0, [i, j]))
                res += get_plus(grid, i, j)
    return res

def check_integrity(a, b): #a, b are pluses (objects)
    for el in a.cords:
        if el in b.cords:
            return False
    return True

def sort_plus(pluses):
    pluses = sorted(pluses, key=lambda x: -x.size)
    res = []
    i, j = 0, 0
    while i != len(pluses) - 1:
        j = i + 1
        while j != len(pluses):
            if check_integrity(pluses[i], pluses[j]):
                res.append(pluses[i].area*pluses[j].area)
            j += 1
        i += 1
    return max(res)


if __name__ == "__main__":
    grid = ["GGGGGGGGGGGG",
            "GBGGBBBBBBBG",
            "GBGGBBBBBBBG",
            "GGGGGGGGGGGG",
            "GGGGGGGGGGGG",
            "GGGGGGGGGGGG",
            "GGGGGGGGGGGG",
            "GBGGBBBBBBBG",
            "GBGGBBBBBBBG",
            "GBGGBBBBBBBG",
            "GGGGGGGGGGGG",
            "GBGGBBBBBBBG"]
    # grid = [list(el) for el in grid]
    # for i in range(len(grid)):
    #     for j in range(len(grid[0])):
    #         if grid[i][j] == "B":
    #             grid[i][j] = "X"
    #         else:
    #             grid[i][j] = "_"
    #         print(grid[i][j], end=" ")
    #     print()
    pluses = all_pluses(grid)
    print(sort_plus(pluses))