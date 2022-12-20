from knight import Knight
from bishop import Bishop
from rook import Rook
from queen import Queen
from king import King
from pawn import Pawn

class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.populate_board()

    def populate_board(self):
        # Place the white pieces on the board
        self.grid[0][0] = Knight('white')  # White knight
        self.grid[0][1] = Bishop('white')  # White bishop
        self.grid[0][2] = Rook('white')  # White rook
        self.grid[0][3] = Queen('white')  # White queen
        self.grid[0][4] = King('white')  # White king
        self.grid[0][5] = Bishop('white')  # White bishop
        self.grid[0][6] = Knight('white')  # White knight
        self.grid[0][7] = Rook('white')  # White rook
        for i in range(8):
            self.grid[1][i] = Pawn('White')  # White pawns

        # Place the black pieces on the board
        self.grid[7][0] = Knight('black')  # Black knight
        self.grid[7][1] = Bishop('black')  # Black bishop
        self.grid[7][2] = Rook('black')  # Black rook
        self.grid[7][3] = Queen('black')  # Black queen
        self.grid[7][4] = King('black')  # Black king
        self.grid[7][5] = Bishop('black')  # Black bishop
        self.grid[7][6] = Knight('black')  # Black knight
        self.grid[7][7] = Rook('black')  # Black rook
        for i in range(8):
            self.grid[6][i] = Pawn('black')  # Black pawns

    def move_piece(self, from_pos, to_pos):
        # Move a chess piece from one position to another
        pass

    def in_check(self):
        # Check if the current player is in check
        pass
    def in_checkmate(self):
        # Check if the current player is in checkmate
        pass

if __name__ == "__main__":
    test = Board()
    print(test.grid)