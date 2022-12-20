from piece import Piece
from PyQt5.QtGui import QPixmap

class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self):
        pass

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_bishop')
        else:
            return QPixmap('images/white_bishop')