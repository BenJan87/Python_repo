from gui_m import graphic_m, transform_hash
from matrix_filling_m import fill 
from g_modes_m import choose_gamemode
from shooting_m import shoot

if __name__ == "__main__":
    game_mode, n, m = choose_gamemode()
    solution_board = graphic_m(n, m)
    empty_board = transform_hash(graphic_m(n, m))
    solution_board, win = fill(solution_board, game_mode)
    print()
    shoot(solution_board, game_mode, win, empty_board)