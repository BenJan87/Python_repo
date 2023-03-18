

class Value_ranked():
    def __init__(self, postion, score):
        self.score = score
        self.position = postion

def build_obj_arr(arr):
    no_dup_arr = sorted(list(set(arr)), reverse = True)
    obj_arr = [Value_ranked(pos + 1, score) for pos, score in enumerate(no_dup_arr)]
    return obj_arr
    

def find_pos(arr_obj, result):
    if len(arr_obj) == 1:
        if result > arr_obj[0].score:
            return arr_obj[0].position - 1
        if result < arr_obj[0].score:
            return arr_obj[0].position + 1
        
        return arr_obj[0].position
    
    median = len(arr_obj) // 2

    if arr_obj[median].score > result:
        arr_obj = arr_obj[median:]
    elif arr_obj[median].score < result:
        arr_obj = arr_obj[:median]
    else:
        arr_obj = [arr_obj[median]]

    return find_pos(arr_obj, result)



def loop_player(arr, list_players):
    

    arr_obj = build_obj_arr(arr)
    positions = []

    for player in list_players:
        if player > arr_obj[0].score:
            positions.append(1)
            continue
        if player < arr_obj[-1].score:
            positions.append(len(arr_obj) + 1)
            continue

        pos = find_pos(arr_obj, player)
        positions.append(pos)

    return positions





if __name__ == "__main__":

    # ranked = [100, 100, 50, 40, 40, 20, 10]
    # players = [5, 25, 50, 120]
    

    ranked = [100, 90, 90, 80, 75, 60]
    players = [50, 65, 77, 90, 102]

    print(loop_player(ranked, players))
