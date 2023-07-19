class Board():
    def __init__(self) -> list:
        self.tmp_board = [[0]*8]*8
        
    def __str__(self):
        repr_board = ""
        for row in self.tmp_board:
            for pos in row:
                repr_board += str(pos) + " " 
            repr_board += "\n"

        return repr_board
    
    

class Chess_figure():
    def __init__(self, x: int, y: int, color: str, on_board: bool) -> None:
        self.x = x
        self.y = y
        self.color = color
        self.on_board = on_board
        self.basic_move = []
        self.taking_move = []

    def check_possible_moves(self):
        pass


class Pawn(Chess_figure):
    def __init__(self, x: int, y: int, color: str, on_board: bool) -> None:
        super().__init__(x, y, color, on_board)
        self.basic_move = [
            [0, -1], [0, -2]
        ] if self.color == "white" else [
            [0, 1], [0, 2]
        ]

        self.taking_move = [
            [-1, -1], [-1, 1]
        ] if self.color == "white" else [
            [-1, 1], [1, 1]
        ] 

        
    def moving(self):
        


board = Board()
print(board)
