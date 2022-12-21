from piece import Piece
from PyQt5.QtGui import QPixmap

class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.desc = f'{self.color} queen'

    def can_move(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_queen')
        else:
            return QPixmap('images/white_queen')