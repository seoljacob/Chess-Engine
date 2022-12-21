from piece import Piece
from PyQt5.QtGui import QPixmap

class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.desc = f'{self.color} rook'

    def can_move(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_rook')
        else:
            return QPixmap('images/white_rook')