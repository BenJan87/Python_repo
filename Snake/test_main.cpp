#include <iostream>
#include <vector>

class SnakePiece {
public:
    int posX;
    int posY;
    SnakePiece* previous;
    SnakePiece* next;
    bool head;
    SnakePiece(int posX, int posY, SnakePiece* previous, SnakePiece* next, bool head=false) {
        this->posX = posX;
        this->posY = posY;
        this->previous = previous;
        this->next = next;
        this->head = head;
    }
    std::string printPieceAsFragment() {
        if (this->head) {
            return "✂";
        }
        return "✂";
    }
};

class Snake {
public:
    std::vector<SnakePiece*> wholeSnake;
    void insertPieceIntoSnake(SnakePiece* piece) {
        this->wholeSnake.push_back(piece);
    }
};

class Board {
public:
    std::vector<std::vector<SnakePiece*>> boardGame;
    Board() {
        this->boardGame = std::vector<std::vector<SnakePiece*>>(50, std::vector<SnakePiece*>(50, nullptr));
    }
    void insertPieceIntoBoard(SnakePiece* piece) {
        this->boardGame[piece->posX][piece->posY] = piece;
    }
    void changePiecePosition() {}
    void printBoard() {
        for (auto row : this->boardGame) {
            for (auto piece : row) {
                if (piece == nullptr) {
                    std::cout << "0 ";
                }
                else {
                    std::cout << piece->printPieceAsFragment() << " ";
                }
            }
            std::cout << std::endl;
        }
    }
};

int main() {
    Board variableBoard;
    SnakePiece* fst = new SnakePiece(3, 1, nullptr, nullptr, true);
    SnakePiece* sec = new SnakePiece(2, 3, nullptr, nullptr);
    SnakePiece* thr = new SnakePiece(2, 4, nullptr, nullptr);
    variableBoard.insertPieceIntoBoard(fst);
    variableBoard.insertPieceIntoBoard(sec);
    variableBoard.insertPieceIntoBoard(thr);
    variableBoard.printBoard();
    std::cout << "done" << std::endl;
    return 0;
}