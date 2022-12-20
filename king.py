from piece import Piece

class King(Piece):
    def __init__(self, color):
        super().__init__(color)

    def can_move(self):
        pass