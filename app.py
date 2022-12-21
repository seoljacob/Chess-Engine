import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QGridLayout
from PyQt5.QtCore import Qt
from board import Board
from custom_label import ChessPieceLabel

class ChessGUI(QMainWindow):
    _sx, _sy = None, None

    def __init__(self, chess_board):
        super().__init__()
        self.chess_board = chess_board # internal chess board

        # create and set dimensions of the GUI
        self.setWindowTitle("Chess Engine")
        self.setGeometry(0, 0, 800, 800) # (x, y, width, height)
        self.setFixedSize(800, 800)

        # where the main content goes
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(0) # controls the spacing between the widgets in the layout
        self.grid_layout.setContentsMargins(0, 0, 0, 0) # controls the spacing around the contents of the layout
        self.central_widget.setLayout(self.grid_layout)

        self.board = [[QFrame(self.central_widget) for _ in range(8)] for _ in range(8)] # creates a QFrame with the central_widget as its parent
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.board[i][j].setStyleSheet("QFrame { background-color: wheat }")
                else:
                    self.board[i][j].setStyleSheet("QFrame { background-color: tan }")
                self.board[i][j].setFixedSize(100, 100)
                self.grid_layout.addWidget(self.board[i][j], i, j)
        
        self.populate_board()
    
    def populate_board(self):
        # Iterate over the grid and update the GUI to match the board state
        for i in range(8):
            for j in range(8):
                piece = self.chess_board.grid[i][j]
                if piece:
                    label = ChessPieceLabel() # creates a QLabel with a QFrame as its parent (we can do this conversely as well)
                    label.setPixmap(piece.get_pixmap())
                    label.setScaledContents(True)
                    label.setFixedSize(100, 100)
                    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    label.mouse_press.connect(ChessGUI.set_start_pos)
                    label.mouse_release.connect(ChessGUI.update_board) # connect mouse release to event handler
                    self.grid_layout.addWidget(label, i, j)

    @staticmethod
    def set_start_pos(x, y):
        ChessGUI._sx = x
        ChessGUI._sy = y

    @staticmethod
    def update_board(ex, ey):
        # Update the internal chess board to match GUI
        print(f"Start pos: ({ChessGUI._sx}, {ChessGUI._sy})")
        print(f"End pos: ({ex}, {ey})")
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ChessGUI(Board())
    gui.show()
    sys.exit(app.exec_())
