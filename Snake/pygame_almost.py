import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Set the dimensions of the screen
WINDOW_WIDTH = 100
WINDOW_HEIGHT = 100
CELL_SIZE = 10

class SnakePiece:
    def __init__(self, posX: int, posY: int, previous: str, now: str, head=False):
        self.head = head
        self.posX = posX
        self.posY = posY
        self.previous = previous
        self.now = now

    def draw(self, screen):
        if self.head:
            pygame.draw.rect(screen, WHITE, (self.posX * CELL_SIZE, self.posY * CELL_SIZE, CELL_SIZE, CELL_SIZE))
        else:
            pygame.draw.rect(screen, GREEN, (self.posX * CELL_SIZE, self.posY * CELL_SIZE, CELL_SIZE, CELL_SIZE))


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
        self.posX = random.randint(0, 9)
        self.posY = random.randint(0, 9)
    

    def draw(self, screen):
        pygame.draw.rect(screen, RED, (self.posX * CELL_SIZE, self.posY * CELL_SIZE, CELL_SIZE, CELL_SIZE))


class Board:    
    def __init__(self, givenApple: Apple):
        self.boardGame = [[0]*10 for _ in range(10)]
        self.apple = givenApple

    def insertSnakeIntoBoard(self, snakeObj: Snake):
        boardApple = self.apple
        eaten = False
        if snakeObj.wholeSnake[0].posX == boardApple.posX and snakeObj.wholeSnake[0].posY == boardApple.posY:
            tail = snakeObj.wholeSnake[-1]
            
            tmpPiece = SnakePiece(tail.posX, tail.posY, tail.previous, tail.previous)
            match tail.now:
                case "W":
                    tmpPiece.posY += 1
                    tmpPiece.posY %= 10
                case "A":
                    tmpPiece.posX += 1
                    tmpPiece.posY %= 10

                case "S":
                    tmpPiece.posY -= 1
                    tmpPiece.posY %= 10

                case "D":
                    tmpPiece.posX -= 1
                    tmpPiece.posY %= 10
            snakeObj.insertPieceIntoSnake(tmpPiece)
            eaten = True

        for piece in snakeObj.wholeSnake:
            piece.posY %= 10
            piece.posX %= 10
            #different printing (x instead of y)
            self.boardGame[piece.posY][piece.posX] = piece

        if eaten:
            return True

    def insertAppleIntoBoard(self):
        givenApple = self.apple
        self.boardGame[givenApple.posY][givenApple.posX] = givenApple

    def updateBoardAndSnakeAfterMove(self, nowMove: str, snakeObj: Snake):
        newApple = Apple()
        newApple.posX = self.apple.posX
        newApple.posY = self.apple.posY
        # change head
        head = snakeObj.wholeSnake[0].now

        # cannot press W while S, so:
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

        newBoard = Board(newApple)
        newBoard.insertAppleIntoBoard()
        eatenApple = newBoard.insertSnakeIntoBoard(snakeObj)

        
        while eatenApple:
            tmpApple = Apple()
            collision = False
            for piece in snakeObj.wholeSnake:
                if tmpApple.posX == piece.posX and tmpApple.posY == piece.posY:
                    collision = True
                    break
            if not collision:
                newBoard.apple = tmpApple
                newBoard.insertAppleIntoBoard()
                break

        # for piece in snakeObj.wholeSnake:
            # self.insertSnakeIntoBoard(snakeObj)

        return newBoard, snakeObj

    

    def draw(self, screen):
        for row in range(len(self.boardGame)):
            for col in range(len(self.boardGame[row])):
                if self.boardGame[row][col] == 0:
                    pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))
                elif isinstance(self.boardGame[row][col], SnakePiece):
                    self.boardGame[row][col].draw(screen)
                else:
                    self.boardGame[row][col].draw(screen)




# Initialize Pygame
pygame.init()

# Set up the window
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Snake Game")

clock = pygame.time.Clock()

newApple = Apple()
newBoard = Board(newApple)

fst = SnakePiece(10//2, 10//2, 'W', 'W', head=True)
newSnake = Snake()
lose = False

newSnake.insertPieceIntoSnake(fst)

newBoard.insertSnakeIntoBoard(newSnake)
tmpMovement = 'W'


def handle_input():
    movement = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                movement = "W"
            elif event.key == pygame.K_a:
                movement = "A"
            elif event.key == pygame.K_s:
                movement = "S"
            elif event.key == pygame.K_d:
                movement = "D"
    return movement


while True:
    movement = handle_input()
    if movement:
        newBoard, newSnake = newBoard.updateBoardAndSnakeAfterMove(movement, newSnake)
        tmpMovement = movement
    else:
        newBoard, newSnake = newBoard.updateBoardAndSnakeAfterMove(tmpMovement, newSnake)

    for piece in newSnake.wholeSnake[1:]:
            if piece.posX == newSnake.wholeSnake[0].posX and piece.posY == newSnake.wholeSnake[0].posY:
                print("You lose!")
                lose = True
                break
    if lose:
        break
    window.fill(BLACK)

    newBoard.draw(window)
    pygame.display.update()

    clock.tick(10)