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
        self.grid[0][0] = Rook('black')  # black knight
        self.grid[0][1] = Knight('black')  # black bishop
        self.grid[0][2] = Bishop('black') # black rook
        self.grid[0][3] = Queen('black')  # black queen
        self.grid[0][4] = King('black')  # black king
        self.grid[0][5] = Bishop('black')  # black bishop
        self.grid[0][6] = Knight('black')  # black knight
        self.grid[0][7] = Rook('black')  # black rook
        for i in range(8):
            self.grid[1][i] = Pawn('black')  # black pawns

        # Place the black pieces on the board
        self.grid[7][0] = Rook('white')  # white knight
        self.grid[7][1] = Knight('white')  # white bishop
        self.grid[7][2] = Bishop('white')  # white rook
        self.grid[7][3] = Queen('white')  # white queen
        self.grid[7][4] = King('white')  # white king
        self.grid[7][5] = Bishop('white')  # white bishop
        self.grid[7][6] = Knight('white')  # white knight
        self.grid[7][7] = Rook('white')  # white rook
        for i in range(8):
            self.grid[6][i] = Pawn('white')  # white pawns
    
    def show(self):
        for row in self.grid:
            print(row)

    def is_same_tile(self, from_pos, to_pos):
        if from_pos == to_pos:
            return True

    def is_tile_occupied(self, to_pos):
        if self.grid[to_pos[0]][to_pos[1]]:
            return True
        return False

    def get_piece(self, from_pos):
        return self.grid[from_pos[0]][from_pos[1]]

    def set_piece(self, to_pos, piece):
        if not self.is_tile_occupied(to_pos):
            self.grid[to_pos[0]][to_pos[1]] = piece
        else:
            self.grid[to_pos[0]][to_pos[1]] = None
            self.grid[to_pos[0]][to_pos[1]] = piece

    def clean_up(self, from_pos):
        self.grid[from_pos[0]][from_pos[1]] = None

    def in_check(self):
        # Check if the current player is in check
        pass
    def in_checkmate(self):
        # Check if the current player is in checkmate
        pass

if __name__ == "__main__":
    test = Board()
    print(test.grid)