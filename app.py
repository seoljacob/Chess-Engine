import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFrame, QGridLayout, QStackedLayout
from PyQt5.QtCore import Qt
from board import Board
from custom_label import ChessPieceLabel

class ChessGUI(QMainWindow):
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
                    label = ChessPieceLabel(self.chess_board)
                    label.setPixmap(piece.get_pixmap())
                    label.setScaledContents(True)
                    label.setFixedSize(100, 100)
                    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    label.mouse_release.connect(self.move_piece) # connect mouse release to event handler
                    self.grid_layout.addWidget(label, i, j)

    def move_piece(self, sx, sy, ex, ey):
        # Update the internal chess board to match GUI
        piece = self.chess_board.get_piece((sy, sx))
        self.chess_board.set_piece((ey, ex), piece) # check if dest is occupied, if not, place piece
        if not self.chess_board.is_same_tile((sy, sx), (ey, ex)):
            self.chess_board.clean_up((sy, sx))

        self.update_GUI()

    def update_GUI(self):
        for i in range(self.grid_layout.count()):
            label = self.grid_layout.itemAt(i).widget()
            if isinstance(label, ChessPieceLabel):
                label.deleteLater()
        self.populate_board()
        # self.chess_board.show()
        

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ChessGUI(Board())
    gui.show()
    sys.exit(app.exec_())
