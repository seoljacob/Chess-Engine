from piece import Piece
from PyQt5.QtGui import QPixmap

class Queen(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} queen'

    def get_moves(self, chess_board):
        moves = []

        cur_row, cur_col = self.position

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False
        
        # Case 1 -> move upwards 
        while Queen.is_inbound(up):
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
        while Queen.is_inbound(down):
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
        while Queen.is_inbound(left):
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
        while Queen.is_inbound(right):
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

        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1
        first_collision = False

        # diagonally up + left
        while Queen.is_inbound(up) and Queen.is_inbound(left):
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
        while (Queen.is_inbound(up) and Queen.is_inbound(right)):
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
        while (Queen.is_inbound(down) and Queen.is_inbound(left)):
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
        while (Queen.is_inbound(down) and Queen.is_inbound(right)):
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
            return QPixmap('images/black_queen')
        else:
            return QPixmap('images/white_queen')