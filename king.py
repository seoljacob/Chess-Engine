from piece import Piece
from PyQt5.QtGui import QPixmap

class King(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.desc = f'{self.color} king'

    def get_moves(self, chess_board):
        # 8 moves
        moves = []

        cur_row, cur_col = self.position
        up, down, left, right = cur_row - 1, cur_row + 1, cur_col - 1, cur_col + 1

        # move upwards 1 square
        if King.is_inbound(up):
            if not chess_board.is_occupied((up, cur_col)):
                moves.append((up, cur_col))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][cur_col], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((up, cur_col))
        
        # move down 1 square
        if King.is_inbound(down):
            if not chess_board.is_occupied((down, cur_col)):
                moves.append((down, cur_col))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][cur_col], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((down, cur_col))

        # move left 1 square
        if King.is_inbound(cur_row):
            if not chess_board.is_occupied((cur_row, left)):
                moves.append((cur_row, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[cur_row][left], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((cur_row, left))
        
        # move right 1 square
        if King.is_inbound(cur_row):
            if not chess_board.is_occupied((cur_row, right)):
                moves.append((cur_row, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[cur_row][right], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((cur_row, right))

        # move upwards and left 1 square
        if King.is_inbound(up) and King.is_inbound(left):
            if not chess_board.is_occupied((up, left)):
                moves.append((up, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][left], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((up, left))

        # move upwards and right 1 square
        if King.is_inbound(up) and King.is_inbound(right):
            if not chess_board.is_occupied((up, right)):
                moves.append((up, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[up][right], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((up, right))

        # move downwards and left 1 square
        if King.is_inbound(down) and King.is_inbound(left):
            if not chess_board.is_occupied((down, left)):
                moves.append((down, left))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][left], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((down, left))

        # move downwards and right 1 square
        if King.is_inbound(down) and King.is_inbound(right):
            if not chess_board.is_occupied((down, right)):
                moves.append((down, right))
            else:
                if not chess_board.is_same_color(chess_board.grid[down][right], self):
                    # < -- Add check to see if King is in check -- > 
                    moves.append((down, right))
        

        return moves

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_king')
        else:
            return QPixmap('images/white_king')