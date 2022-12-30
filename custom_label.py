from PyQt5.QtWidgets import QLabel
from PyQt5.QtCore import Qt, pyqtSignal

"""
370 rounds to 400
430 rounds to 400
"""
def round_to_100(number):
    rounded_number = number / 100 #3.7 || 4.3
    rounded_number = round(rounded_number) #4.0 || 4.0
    rounded_number *= 100 # 400 || 400
    if rounded_number < 0:
        return 0
    if rounded_number > 700:
        return 700
    return rounded_number

class ChessPieceLabel(QLabel):
    mouse_release = pyqtSignal(int, int, int, int) # set up event listener for mouse release event

    def __init__(self, chess_board, grid_layout):
        super().__init__(None)
        self.chess_board = chess_board
        self.grid_layout = grid_layout

        self.setMouseTracking(True)
        self.dragging = False
        self.sx, self.sy = None, None
        self.moves = []

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.setCursor(Qt.ClosedHandCursor)
            self.dragging = True
            self.drag_start_pos = event.pos()
            self.sx, self.sy = self.x(), self.y()
            piece = self.chess_board.grid[int(self.sy / 100)][int(self.sx / 100)]
            print(piece.get_moves(self.chess_board))


    def mouseMoveEvent(self, event):
        if self.dragging:
            delta = event.pos() - self.drag_start_pos
            self.move(self.x() + delta.x(), self.y() + delta.y())

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragging = False

            x = round_to_100(self.x())
            y = round_to_100(self.y())

            grid_size = 100

            sx = int(self.sx / grid_size)
            sy = int(self.sy / grid_size)
            ex = int(x / grid_size)
            ey = int(y / grid_size)

            # y comes before x because matrices in Python are read [rows] then [cols]
            if self.chess_board.is_occupied((ey, ex)) and self.chess_board.grid[ey][ex].color == self.chess_board.grid[sy][sx].color:
                self.move(sx * grid_size, sy * grid_size)
                return

            self.move(x, y)

            self.mouse_release.emit(sx, sy, ex, ey) # send x, y on mouse release
           
        
