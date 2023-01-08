from piece import Piece
from PyQt5.QtGui import QPixmap


class Bishop(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} bishop'

    def get_moves(self, chess_board):
        moves = []

        cur_row, cur_col = self.position

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False

        # diagonally up + left
        while Bishop.is_inbound(up) and Bishop.is_inbound(left):
            if not chess_board.is_occupied((up, left)):
                moves.append((up, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][left], self) and not first_collision:
                    moves.append((up, left))
                    first_collision = True
                    break
                else:
                    break
            up -= 1
            left -= 1

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False

        # diagonally up + right
        while (Bishop.is_inbound(up) and Bishop.is_inbound(right)):
            if not chess_board.is_occupied((up, right)):
                moves.append((up, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][right], self) and not first_collision:
                    moves.append((up, right))
                    first_collision = True
                    break
                else:
                    break
            up -= 1
            right += 1

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False
            
        # diagonally down + left
        while (Bishop.is_inbound(down) and Bishop.is_inbound(left)):
            if not chess_board.is_occupied((down, left)):
                moves.append((down, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][left], self) and not first_collision:
                    moves.append((down, left))
                    first_collision = True
                    break
                else:
                    break
            down += 1
            left -= 1

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False
        
        # diagonally down + right
        while (Bishop.is_inbound(down) and Bishop.is_inbound(right)):
            if not chess_board.is_occupied((down, right)):
                moves.append((down, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][right], self) and not first_collision:
                    moves.append((down, right))
                    first_collision = True
                    break
                else:
                    break
            down += 1
            right += 1
        return moves

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_bishop')
        else:
            return QPixmap('images/white_bishop')
