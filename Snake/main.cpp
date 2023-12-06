#include <iostream>
#include <vector>
using namespace std;

class SnakePiece {
    public:
        bool head;
        int posX, posY;
        string previous, now;
        SnakePiece(int posX, int posY, string previous, string now, bool head=false) {
            this->head = head;
            this->posX = posX;
            this->posY = posY;
            this->previous = previous;
            this->now = now;
        }
        char printPieceAsFragment() {
            if (this->head) {
                return '✂';
            }
            return 'I';
        }
        void makeMove(string givenMove) {
            if (givenMove == "W") {
                this->posY -= 1;
            }
            else if (givenMove == "A") {
                this->posX -= 1;
            }
            else if (givenMove == "S") {
                this->posY += 1;
            }
            else if (givenMove == "D") {
                this->posX += 1;
            }
            this->previous = this->now;
            this->now = givenMove;
        }
};

class Snake {
    public:
        vector<SnakePiece> wholeSnake;
        void insertPieceIntoSnake(SnakePiece piece) {
            this->wholeSnake.push_back(piece);
        }
};

class Board {
    public:
        vector<vector<SnakePiece>> boardGame;
        Board() {
            this->boardGame = vector<vector<SnakePiece>>(10, vector<SnakePiece>(10));
        }
        void insertSnakeIntoBoard(Snake snakeObj) {
            for (auto piece : snakeObj.wholeSnake) {
                this->boardGame[piece.posY][piece.posX] = piece;
            }
        }
        void updateBoardAndSnakeAfterMove(string nowMove, Snake snakeObj) {
            string head = snakeObj.wholeSnake[0].now;
            if (head == "W" && nowMove == "S") {
                return;
            }
            else if (head == "A" && nowMove == "D") {
                return;
            }
            else if (head == "S" && nowMove == "W") {
                return;
            }
            else if (head == "D" && nowMove == "A") {
                return;
            }
            SnakePiece tail = snakeObj.wholeSnake[snakeObj.wholeSnake.size()-1];
            this->boardGame[tail.posY][tail.posX] = 0;
            for (int i=snakeObj.wholeSnake.size()-1; i>0; i--) {
                snakeObj.wholeSnake[i].posX = snakeObj.wholeSnake[i-1].posX;
                snakeObj.wholeSnake[i].posY = snakeObj.wholeSnake[i-1].posY;
            }
            snakeObj.wholeSnake[0].makeMove(nowMove);
            this->insertSnakeIntoBoard(snakeObj);
        }
};






// Snake: długość, kolor, liczba zjedzonych jabłek
