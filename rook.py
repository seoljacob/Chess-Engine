from piece import Piece
from PyQt5.QtGui import QPixmap

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} rook'

    def get_moves(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_rook')
        else:
            return QPixmap('images/white_rook')