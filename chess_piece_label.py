from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal
from pawn import Pawn

class ChessPieceLabel(QLabel):
    # set up event listener for mouse release event
    mouse_release = pyqtSignal(int, int, int, int)

    grid_size = 100

    def __init__(self, board, chess_board, grid_layout):
        super().__init__(None)
        self.board = board
        self.chess_board = chess_board
        self.grid_layout = grid_layout

        self.setMouseTracking(True)
        self.dragging = False
        self.s_col, self.s_row = None, None
        self.moves = []

    @staticmethod
    def round_to_100(number):
        rounded_number = number / 100  # 3.7 || 4.3
        rounded_number = round(rounded_number)  # 4.0 || 4.0
        rounded_number *= 100  # 400 || 400
        if rounded_number < 0:
            return 0
        if rounded_number > 700:
            return 700
        return rounded_number

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.dragging = True
            self.drag_start_pos = event.pos()

            self.s_col, self.s_row = int(
                self.x() / ChessPieceLabel.grid_size), int(self.y() / ChessPieceLabel.grid_size)

            piece = self.chess_board.grid[self.s_row][self.s_col]
            self.moves = piece.get_moves(self.chess_board)
            print(self.moves)
            for move in self.moves:
                row, col = move
                if (row + col) % 2 == 0:
                    self.board[row][col].setStyleSheet(
                        "QFrame { background-color: wheat; border: 1px solid #1e140a; }")
                else:
                    self.board[row][col].setStyleSheet(
                        "QFrame { background-color: tan; border: 1px solid #1e140a; }")

    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.pos() - self.drag_start_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

            for move in self.moves:
                row, col = move
                if (row + col) % 2 == 0:
                    self.board[row][col].setStyleSheet(
                        "QFrame { background-color: wheat }")
                else:
                    self.board[row][col].setStyleSheet(
                        "QFrame { background-color: tan }")

            x = ChessPieceLabel.round_to_100(self.x())
            y = ChessPieceLabel.round_to_100(self.y())

            e_col = int(x / ChessPieceLabel.grid_size)
            e_row = int(y / ChessPieceLabel.grid_size)

            # Case invalid movement -> there is a piece of the same color on the tile
            if (self.chess_board.is_occupied((e_row, e_col)) and self.chess_board.grid[e_row][e_col].color == self.chess_board.grid[self.s_row][self.s_col].color):
                self.move(self.s_col * ChessPieceLabel.grid_size,
                          self.s_row * ChessPieceLabel.grid_size)
                return

            # Case invalid movement -> the tile is not a valid tile that the piece can get to
            if (e_row, e_col) not in self.moves:
                self.move(self.s_col * ChessPieceLabel.grid_size,
                          self.s_row * ChessPieceLabel.grid_size)
                return

            # Case valid movement -> the tile is a valid tile that the piece can get to
            self.move(x, y)

            # Set Pawn's has_moved to True
            piece = self.chess_board.grid[self.s_row][self.s_col]

            if isinstance(piece, Pawn) and not piece.has_moved:
                piece.has_moved = True

            self.mouse_release.emit(self.s_col, self.s_row, e_col, e_row)
