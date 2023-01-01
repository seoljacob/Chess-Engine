from piece import Piece
from PyQt5.QtGui import QPixmap


class Pawn(Piece):
    def __init__(self, color, position):
        super().__init__(color, position)
        self.has_moved = False
        self.desc = f'{self.color} pawn'

    @staticmethod
    def is_inbound(val):
        if val < 0 or val > 7:
            return False
        return True

    def get_moves(self, chess_board):
        moves = []
        cur_row = self.position[0]
        cur_col = self.position[1]

        # For black pawns:
        if self.color == 'black':
            # Case: move forward by 1
            if Pawn.is_inbound(cur_row + 1) and not chess_board.is_occupied((cur_row + 1, cur_col)):
                moves.append((cur_row + 1, cur_col))

            # Case: first move --> move forward by 2
            if Pawn.is_inbound(cur_row + 2) and not self.has_moved and not chess_board.is_occupied((cur_row + 2, cur_col)):
                moves.append((cur_row + 2, cur_col))

            # Case: take opponent piece --> move diagonally to the left by 1
            if ((Pawn.is_inbound(cur_row + 1) and Pawn.is_inbound(cur_col - 1))
                and chess_board.grid[cur_row + 1][cur_col - 1]
                    and chess_board.grid[cur_row + 1][cur_col - 1].color == 'white'):
                moves.append((cur_row + 1, cur_col - 1))

            # Case: take opponent piece --> move diagonally to the right by 1
            if ((Pawn.is_inbound(cur_row + 1) and Pawn.is_inbound(cur_col + 1))
                and chess_board.grid[cur_row + 1][cur_col + 1]
                    and chess_board.grid[cur_row + 1][cur_col + 1].color == 'white'):
                moves.append((cur_row + 1, cur_col + 1))

        elif self.color == 'white':
            # Case: move forward by 1
            if Pawn.is_inbound(cur_row - 1) and not chess_board.is_occupied((cur_row - 1, cur_col)):
                moves.append((cur_row - 1, cur_col))

            # Case: first move --> move forward by 2
            if Pawn.is_inbound(cur_row - 2) and not self.has_moved and not chess_board.is_occupied((cur_row - 2, cur_col)):
                moves.append((cur_row - 2, cur_col))

            # Case: take opponent piece --> move diagonally to the left by 1
            if ((Pawn.is_inbound(cur_row - 1) and Pawn.is_inbound(cur_col - 1))
                and chess_board.grid[cur_row - 1][cur_col - 1]
                    and chess_board.grid[cur_row - 1][cur_col - 1].color == 'black'):
                moves.append((cur_row - 1, cur_col - 1))

            # Case: take opponent piece --> move diagonally to the right by 1
            if ((Pawn.is_inbound(cur_row - 1) and Pawn.is_inbound(cur_col + 1))
                and chess_board.grid[cur_row - 1][cur_col + 1]
                    and chess_board.grid[cur_row - 1][cur_col + 1].color == 'black'):
                moves.append((cur_row - 1, cur_col + 1))

        return moves

    def get_pixmap(self):
        if not self:
            return
        if self.color == 'black':
            return QPixmap('images/black_pawn')
        else:
            return QPixmap('images/white_pawn')
