import os
import random

class SnakePiece:
    def __init__(self, posX: int, posY: int, previous: str, now: str, head=False):
        self.head = head
        self.posX = posX
        self.posY = posY
        self.previous = previous
        self.now = now
        

    def printPieceAsFragment(self):
        if self.head:
            return '✂'
        return 'I'

    def makeMove(self, givenMove: str):
        # change position
        # change previous
        # change now

        match givenMove:
            case "W":
                self.posY -= 1
                self.posY %= 10
            case "A":
                self.posX -= 1
                self.posY %= 10

            case "S":
                self.posY += 1
                self.posY %= 10

            case "D":
                self.posX += 1
                self.posY %= 10


        self.previous = self.now
        self.now = givenMove


class Snake:
    def __init__(self):
        self.wholeSnake = []
    
    def insertPieceIntoSnake(self, piece: SnakePiece):
        self.wholeSnake.append(piece)

class Apple:
    def __init__(self):
        self.posX = random.randint(0, 50) % 10
        self.posY = random.randint(0, 50) % 10
        
    # def addAppleToBoard(self, currBoard: Board):
    #     currBoard.boardGame[self.posY][self.posX] = self
    #     return currBoard

    def printPieceAsApple(self):
        return "A"


class Board:
    def __init__(self):
        self.boardGame = [[0]*10 for _ in range(10)]
        self.apple = None

    def insertSnakeIntoBoard(self, snakeObj: Snake):
        for piece in snakeObj.wholeSnake:
            piece.posY %= 10
            piece.posX %= 10
            self.boardGame[piece.posY][piece.posX] = piece

    def insertAppleIntoBoard(self, apple: Apple):
        apple.posY %= 10
        apple.posX %= 10
        self.boardGame[apple.posY][apple.posX] = apple
        self.apple = apple

    def updateBoardAndSnakeAfterMove(self, nowMove: str, snakeObj: Snake):
        head = snakeObj.wholeSnake[0].now

        if head == "W" and nowMove == "S": 
            nowMove = "W"
        
        # cannot press S while W, so:
        elif head == "S" and nowMove == "W":
            nowMove = "S"

        # cannot press A while D:
        elif head == "A" and nowMove == "D":
            nowMove = "A"

        # cannot press D while A:
        elif head == "D" and nowMove == "A": 
            nowMove = "D"

        snakeObj.wholeSnake[0].makeMove(nowMove)

        for i in range(1, len(snakeObj.wholeSnake)):
            snakeObj.wholeSnake[i].makeMove(snakeObj.wholeSnake[i-1].previous)

        if self.apple is None:
            newApple = Apple()
            while any(piece.posX == newApple.posX and piece.posY == newApple.posY for piece in snakeObj.wholeSnake):
                newApple = Apple()
            self.insertAppleIntoBoard(newApple)

        newBoard = Board()
        newBoard.insertAppleIntoBoard(self.apple)
        newBoard.insertSnakeIntoBoard(snakeObj)

        return newBoard, snakeObj
    
    def printBoard(self):
        # piece is either 0 or SnakePiece object
        for row in self.boardGame:
            for piece in row:
                if piece == 0:
                    print("0", end=" ")
                elif isinstance(piece, SnakePiece):
                    print(piece.printPieceAsFragment(), end=" ")
                else:
                    print(piece.printPieceAsApple(), end=" ")
            print()


if __name__ == "__main__":
    variableBoard = Board()

    fst = SnakePiece(1, 1, 'W', 'W', head=True)
    sec = SnakePiece(1, 2, 'W', 'W')
    thr = SnakePiece(1, 3, 'W', 'W')
    fou = SnakePiece(1, 4, 'W', 'W')
    fif = SnakePiece(1, 5, 'W', 'W')

    variableSnake = Snake()

    variableSnake.insertPieceIntoSnake(fst)
    variableSnake.insertPieceIntoSnake(sec)
    variableSnake.insertPieceIntoSnake(thr)
    variableSnake.insertPieceIntoSnake(fou)
    variableSnake.insertPieceIntoSnake(fif)

    nullApple = Apple()
    nullApple.posX = -1
    nullApple.posY = -1
    variableBoard.insertSnakeIntoBoard(variableSnake)
    variableBoard.insertAppleIntoBoard(nullApple)

    variableBoard.printBoard()

    lose = False

    while True:
        newBoard, newSnake = variableBoard.updateBoardAndSnakeAfterMove(input(), variableSnake)

        for piece in newSnake.wholeSnake[1:]:
            if piece.posX == newSnake.wholeSnake[0].posX and piece.posY == newSnake.wholeSnake[0].posY:
                print("You lose!")
                lose = True
                break
        if lose:
            break

        print()

        newBoard.printBoard()

    print("done")
