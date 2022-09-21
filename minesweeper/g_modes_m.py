def choose_gamemode():
    print("Welcome to minesweeper <3")
    game_mode = 0
    while game_mode != 1 and game_mode != 2 and game_mode != 3:
        print("1. Beginner (9x9 - 10 mines)")
        print("2. Intermediate (16x16 - 40 mines)")
        print("3. Expert (30x16 - 99 mines)")
        game_mode = int(input(("Choose difficulty: ")))

    if game_mode == 1:
        n, m = 9, 9
    elif game_mode == 2:
        n, m = 16, 16
    else:
        n, m = 16, 30

    return game_mode, n, m