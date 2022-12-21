from piece import Piece
from PyQt5.QtGui import QPixmap

# Piece with L shaped movement

class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.desc = f'{self.color} knight'

    def get_pixmap(self):
        if not self:
                return
        if self.color == 'black':
            return QPixmap('images/black_knight')
        else:
            return QPixmap('images/white_knight')