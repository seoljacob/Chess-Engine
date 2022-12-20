import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QFrame, QGridLayout
from PyQt5.QtGui import QPixmap, QColor

class ChessGUI(QMainWindow):
    def __init__(self, board):
        super().__init__()
        self.board = board
        self.populate_board()

        self.setWindowTitle("Chess Engine")
        self.setGeometry(0, 0, 800, 800) # (x, y, width, height)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.grid_layout = QGridLayout(self.central_widget)
        self.grid_layout.setSpacing(0) # controls the spacing between the widgets in the layout
        # self.grid_layout.setContentsMargins(0, 0, 0, 0) # controls the spacing around the contents of the layout
        self.central_widget.setLayout(self.grid_layout)

        self.board = [[QFrame(self.central_widget) for _ in range(8)] for _ in range(8)] # specify the parent widget when instantiating a QFrame
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                    self.board[i][j].setStyleSheet("QFrame { background-color: white }")
                else:
                    self.board[i][j].setStyleSheet("QFrame { background-color: black }")
                self.board[i][j].setFixedSize(100, 100)
                self.grid_layout.addWidget(self.board[i][j], i, j)
    
    def populate_board(self):
        # Iterate over the grid and update the GUI to match the board state
        pass

    def move_piece(self, from_pos, to_pos):
        self.board.move_piece(from_pos, to_pos)
        self.update_board()

    def update_board(self):
        # Update the GUI to match the updated board state
        pass

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = ChessGUI()
    gui.show()
    sys.exit(app.exec_())
