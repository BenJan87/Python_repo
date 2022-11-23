# n - chessboard size n x n
# start position (0 ,0)
# compute to (n-1, n-1)
# a, b how the knigth can move
class Knight_l():

    def __init__(self, fst, sec):
        self.fst = fst
        self.sec = sec

    def try_reaching(self, n):
        pos_hor, pos_ver = n - 1, n - 1
        move_1, move_2 = self.fst, self.sec
        flag = 0
        visited_pos = ()
        def check_positive(a, b, n):
            if a >= 0 and b >= 0 and a <= n - 1 and b <= n - 1:
                return True
        
        def check_finish(a , b):
            if a == 0 and b == 0:
                return True

        while True:
            try:
                pos_hor -= move_1
                pos_ver -= move_2
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor += move_1
                pos_ver += move_2
            
            try:
                pos_hor -= move_2
                pos_ver -= move_1
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor += move_2
                pos_ver += move_1

            try:
                pos_hor += move_1
                pos_ver -= move_2
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor -= move_1
                pos_ver += move_2
            
            try:
                pos_hor += move_2
                pos_ver -= move_1
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor -= move_2
                pos_ver += move_1
            
            try:
                pos_hor -= move_2
                pos_ver += move_1
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    break
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor += move_2
                pos_ver -= move_1

            try:
                pos_hor -= move_1
                pos_ver += move_2
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor += move_1
                pos_ver -= move_2

            try:
                pos_hor += move_1
                pos_ver += move_2
                temp_pos = [pos_ver, pos_hor]
                if check_finish(pos_ver, pos_hor):
                    break
                if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                    raise
                visited_pos += (temp_pos, )
                continue
            except:
                pos_hor -= move_1
                pos_ver -= move_2

            
            pos_hor += move_2
            pos_ver += move_1
            temp_pos = [pos_ver, pos_hor]
            if check_finish(pos_ver, pos_hor):
                break
            if not check_positive(pos_hor, pos_ver, n) or temp_pos in visited_pos:
                flag = 1
            break
            
                
    
        if flag:
            return -1

        return len(visited_pos) + 1


def make_possible_moves(n):
    moves_tuple = ()
    for i in range(1, n):
        for j in range(1, n):
            moves_tuple += ([i, j],)
    return moves_tuple

if __name__ == "__main__":
    n = int(input())
    moves_tuple = make_possible_moves(n)
    count = 0
    for el in moves_tuple:
        knight = Knight_l(el[0], el[1])
        print(knight.try_reaching(n), end=" ")
        count += 1
        if count == 4:
            count = 0
            print()