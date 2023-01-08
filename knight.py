from piece import Piece
from PyQt5.QtGui import QPixmap

# Piece with L shaped movement

class Knight(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} knight'

    def get_moves(self, chess_board):
        # 8 moves in total 2 and 1
        moves = []

        cur_row, cur_col = self.position

        # 4 moves -> where Knight moves vertically by 2 squares and horizontally by 1
        up, down, left, right = cur_row - 2, cur_row + 2, cur_col - 1, cur_col + 1

        # move upwards 2 and left 1
        if Knight.is_inbound(up) and Knight.is_inbound(left):
            if not chess_board.is_occupied((up, left)):
                moves.append((up, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][left], self):
                    moves.append((up, left))

        # move upwards 2 and right 1
        if Knight.is_inbound(up) and Knight.is_inbound(right):
            if not chess_board.is_occupied((up, right)):
                moves.append((up, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][right], self):
                    moves.append((up, right))

        # move downwards 2 and left 1
        if Knight.is_inbound(down) and Knight.is_inbound(left):
            if not chess_board.is_occupied((down, left)):
                moves.append((down, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][left], self):
                    moves.append((down, left))
        
        # move downwards 2 and right 1
        if Knight.is_inbound(down) and Knight.is_inbound(right):
            if not chess_board.is_occupied((down, right)):
                moves.append((down, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][right], self):
                    moves.append((down, right))

        # 4 moves -> where Knight moves horizontally by 2 squares and vertically by 1
        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 2, cur_col + 2

        # move upwards 1 and left 2
        if Knight.is_inbound(up) and Knight.is_inbound(left):
            if not chess_board.is_occupied((up, left)):
                moves.append((up, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][left], self):
                    moves.append((up, left))

        # move upwards 1 and right 2
        if Knight.is_inbound(up) and Knight.is_inbound(right):
            if not chess_board.is_occupied((up, right)):
                moves.append((up, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][right], self):
                    moves.append((up, right))
                    
        # move downwards 1 and left 2
        if Knight.is_inbound(down) and Knight.is_inbound(left):
            if not chess_board.is_occupied((down, left)):
                moves.append((down, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][left], self):
                    moves.append((down, left))
        
        # move downwards 1 and right 2
        if Knight.is_inbound(down) and Knight.is_inbound(right):
            if not chess_board.is_occupied((down, right)):
                moves.append((down, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][right], self):
                    moves.append((down, right))

        return moves


    def get_pixmap(self):
        if not self:
                return
        if self.color == 'black':
            return QPixmap('images/black_knight')
        else:
            return QPixmap('images/white_knight')