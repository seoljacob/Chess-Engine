from piece import Piece
from PyQt5.QtGui import QPixmap

class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.desc = f'{self.color} king'

    def can_move(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_king')
        else:
            return QPixmap('images/white_king')