from piece import Piece
from PyQt5.QtGui import QPixmap

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False
        self.desc = f'{self.color} pawn'
    
    def can_move(self, from_pos, to_pos):
        pass
    
    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_pawn')
        else:
            return QPixmap('images/white_pawn')
