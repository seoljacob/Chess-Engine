from piece import Piece

class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.has_moved = False
    
    def can_move(self, from_pos, to_pos):
        pass
    
