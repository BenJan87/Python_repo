from gui_m import print_board
def zeros_reveal(mat, empty_board, p, q, have_been):
    try:
        if mat[p-2][q] == 0 and (p-2, q) not in have_been:
            show_number_around(mat, p-2, q, empty_board)
            empty_board[p-2][q] = " "
            have_been.append((p-2, q))
            zeros_reveal(mat, empty_board, p-2, q, have_been)
    except IndexError:
        pass

    try:
        if mat[p][q-2] == 0 and (p, q-2) not in have_been:
            show_number_around(mat, p, q-2, empty_board)
            empty_board[p][q-2] = " "
            have_been.append((p, q-2))
            zeros_reveal(mat, empty_board, p, q-2, have_been)
    except IndexError:
        pass

    try:
        if mat[p][q+2] == 0 and (p, q+2) not in have_been:
            show_number_around(mat, p, q+2, empty_board)
            empty_board[p][q+2] = " "
            have_been.append((p, q+2))
            zeros_reveal(mat, empty_board, p, q+2, have_been)
    except IndexError:
        pass

    try:
        if mat[p+2][q] == 0 and (p+2, q) not in have_been:
            show_number_around(mat, p+2, q, empty_board)
            empty_board[p+2][q] = " "
            have_been.append((p+2, q))
            zeros_reveal(mat, empty_board, p+2, q, have_been)
    except IndexError:
        pass

    return empty_board

def show_number_around(mat, p, q, empty_board):
    try:
        if mat[p-2][q-2] != 0:
            empty_board[p-2][q-2] = mat[p-2][q-2]
    except IndexError:
        pass

    try:
        if mat[p-2][q] != 0:
            empty_board[p-2][q] = mat[p-2][q]
    except IndexError:
        pass

    try:
        if mat[p-2][q+2] != 0:
            empty_board[p-2][q+2] = mat[p-2][q+2]
    except IndexError:
        pass
    #3

    try:
        if mat[p][q-2] != 0:
            empty_board[p][q-2] = mat[p][q-2]
    except IndexError:
        pass
        
    try:
        if mat[p][q+2] != 0:
            empty_board[p][q+2] = mat[p][q+2]
    except IndexError:
        pass
    #5
    try:
        if mat[p+2][q-2] != 0:
            empty_board[p+2][q-2] = mat[p+2][q-2]
    except IndexError:
        pass

    try:
        if mat[p+2][q] != 0:
            empty_board[p+2][q] = mat[p+2][q]
    except IndexError:
        pass

    try:
        if mat[p+2][q+2] != 0:
            empty_board[p+2][q+2] = mat[p+2][q+2]
    except IndexError:
        pass

def playing(mat, p, q, empty_board):
    p, q = 2*p + 1, 2*q + 1
    n = len(mat)//2
    m = len(mat[0])//2

    if isinstance(mat[p][q], int):
        if mat[p][q] == 0:
            empty_board[p][q] = " "
            show_number_around(mat, p, q, empty_board)
            return zeros_reveal(mat, empty_board, p, q, [(p, q)])
        else:
            empty_board[p][q] = mat[p][q]
    else:
        if mat[p][q] == u"\u058D":
            print("\n\n\nBOMB!\n\n\n")
            for k in range(1, 2*n+1, 2):
                for l in range(1, 2*m+1, 2):
                    if mat[k][l] == u"\u058D":
                        empty_board[k][l] = u"\u058D"
                    else:
                        empty_board[k][l] = " "
            empty_board[p][q] = "!"
            print_board(empty_board)
            exit()
    return empty_board

def flag(empty_board, p, q):
    if empty_board[p][q] == u"\u2690":
        empty_board[p][q] = u"\u25A0"
    else:
        if empty_board[p][q] != u"\u25A0":
            print("\n\n\nAlredy discovered!\n\n\n")
        else:    
            empty_board[p][q] = u"\u2690"

    return empty_board

def check_win(empty_board, game_mode, win):
    count = 0
    for i in range(1, len(empty_board), 2):
        for j in range(1, len(empty_board[0]), 2):
            if empty_board[i][j] == u"\u25A0":
                count += 1
            if count > win:
                return
    print("-"*70)
    print("Congrats, you won! <3")
    for i in range(1, len(empty_board), 2):
        for j in range(1, len(empty_board[0]), 2):
            if empty_board[i][j] == u"\u25A0":
                empty_board[i][j] = u"\u058D"
            else:
                empty_board[i][j] = " "
    print_board(empty_board)
    exit()

def shoot(solution_board, game_mode, win, empty_board):
    while True:
        try:
            shoot = list(map(int, input("""Insert cordinates (e.g. "1 2" ) or press enter to make a flag:""").split()))
            empty_board = playing(solution_board, shoot[1] - 1, shoot[0] - 1, empty_board)
            check_win(empty_board, game_mode, win)
            print_board(empty_board)
            print("\n"*2,"-"*100,"\n")
        except (ValueError, IndexError):
            shoot = list(map(int, input("(Also incorrect input gives flag insertion)\nInsert flag cordinates: ").split()))
            empty_board = flag(empty_board, shoot[1]*2-1, shoot[0]*2-1)
            print_board(empty_board)
            print("\n"*2,"-"*100,"\n")