def nearlySimilarRectangles(sides):
    
    i, count = 0, 0
    
    while i != len(sides):
        j = i + 1
        while j != len(sides):
            if sides[i][0] / sides[j][0] == sides[i][1] / sides[j][1]: 
                count += 1
            j += 1
        i += 1
    return count


arr = [[2, 1],[10, 7],[9, 5],[6,9],[7,3]]
print(nearlySimilarRectangles(arr))