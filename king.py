from piece import Piece
from PyQt5.QtGui import QPixmap

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} king'

    def get_moves(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_king')
        else:
            return QPixmap('images/white_king')