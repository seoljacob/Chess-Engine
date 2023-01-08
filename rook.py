from piece import Piece
from PyQt5.QtGui import QPixmap

class Rook(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} rook'

    def get_moves(self, chess_board):
        moves = []

        cur_row, cur_col = self.position
        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1

        first_collision = False
        
        # Case 1 -> move upwards 
        while Rook.is_inbound(up):
            if not chess_board.is_occupied((up, cur_col)):
                moves.append((up, cur_col))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][cur_col], self) and not first_collision:
                    moves.append((up, cur_col))
                    first_collision = True
                    break
                else:
                    break
            up -= 1

        first_collision = False
    
        # Case 2 -> move downwards
        while Rook.is_inbound(down):
            if not chess_board.is_occupied((down, cur_col)):
                moves.append((down, cur_col))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][cur_col], self) and not first_collision:
                    moves.append((down, cur_col))
                    first_collision = True
                    break
                else:
                    break
            down += 1

        first_collision = False

        # Case 3 -> move left
        while Rook.is_inbound(left):
            if not chess_board.is_occupied((cur_row, left)):
                moves.append((cur_row, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[cur_row][left], self) and not first_collision:
                    moves.append((cur_row, left))
                    first_collision = True
                    break
                else:
                    break
            left -= 1

        first_collision = False

        # Case 4 -> move right
        while Rook.is_inbound(right):
            if not chess_board.is_occupied((cur_row, right)):
                moves.append((cur_row, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[cur_row][right], self) and not first_collision:
                    moves.append((cur_row, right))
                    first_collision = True
                    break
                else:
                    break
            right += 1
        return moves

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_rook')
        else:
            return QPixmap('images/white_rook')