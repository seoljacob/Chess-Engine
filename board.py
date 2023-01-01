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
        self.grid[0][0] = Rook('black', (0, 0))  # black knight
        self.grid[0][1] = Knight('black', (0, 1))  # black bishop
        self.grid[0][2] = Bishop('black', (0, 2)) # black rook
        self.grid[0][3] = Queen('black', (0, 3))  # black queen
        self.grid[0][4] = King('black', (0, 4))  # black king
        self.grid[0][5] = Bishop('black', (0, 5))  # black bishop
        self.grid[0][6] = Knight('black', (0, 6))  # black knight
        self.grid[0][7] = Rook('black', (0, 7))  # black rook
        for i in range(8):
            self.grid[1][i] = Pawn('black', (1, i))  # black pawns

        # Place the black pieces on the board
        self.grid[7][0] = Rook('white', (7, 0))  # white knight
        self.grid[7][1] = Knight('white', (7, 1))  # white bishop
        self.grid[7][2] = Bishop('white', (7, 2))  # white rook
        self.grid[7][3] = Queen('white', (7, 3))  # white queen
        self.grid[7][4] = King('white', (7, 4))  # white king
        self.grid[7][5] = Bishop('white', (7, 5))  # white bishop
        self.grid[7][6] = Knight('white', (7, 6))  # white knight
        self.grid[7][7] = Rook('white', (7, 7))  # white rook
        for i in range(8):
            self.grid[6][i] = Pawn('white', (6, i))  # white pawns
    
    def show(self):
        """Displays all rows of the chess board.
        """
        for row in self.grid:
            print(row)

    def is_same_color(self, piece1, piece2):
        if piece1 and piece2 and piece1.color == piece2.color:
            return True
        return False

        
    def is_same_tile(self, from_pos, to_pos):
        """Checks whether the source tile and the destination tile are the same. 

        Args:
            from_pos (tuple): (source x, source y)
            to_pos (tuple): (destination x, destination y)

        Returns:
            boolean: True or False
        """
        if from_pos == to_pos:
            return True

    def is_occupied(self, to_pos):
        """Checks whether the destination tile is occupied.

        Args:
            to_pos (tuple): (destination x, destination y)

        Returns:
            boolean: True or False
        """
        if self.grid[to_pos[0]][to_pos[1]]:
            return True
        return False

    def get_piece(self, from_pos):
        """Returns the piece that belongs to the tile (from_pos[0], from_pos[1])

        Args:
            from_pos (tuple): (source x, source y)

        Returns:
            _type_: Piece
        """
        return self.grid[from_pos[0]][from_pos[1]]

    def set_piece(self, to_pos, piece):
        # print(f'Before: {piece.position}')
        if not self.is_occupied(to_pos):
            self.grid[to_pos[0]][to_pos[1]] = piece # update internal chess board
            piece.set_position((to_pos[0], to_pos[1])) # update position of piece
        else:
            self.grid[to_pos[0]][to_pos[1]] = None
            self.grid[to_pos[0]][to_pos[1]] = piece
            piece.set_position((to_pos[0], to_pos[1]))
        # print(f'After: {piece.position}')

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