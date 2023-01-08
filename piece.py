class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position

    def get_position(self):
        return self.position

    def set_position(self, value):
        self.position = value

    @staticmethod
    def is_inbound(val):
        if val < 0 or val > 7:
            return False
        return True

    def get_moves(self):
        pass

    def get_pixmap(self):
        return