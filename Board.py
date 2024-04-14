from typing import Dict
from Pieces import Piece,Pawn,Rook,Queen,King,Bishop,Knight


class Board:
    def __init__(self):
        self.board = self.create_starting_position()

    def create_starting_position(self) -> Dict[str, Piece]:
        pieces = {}
        #
        for col in 'abcdefgh':
            pieces[col + '2'] = Pawn('w')
            pieces[col + '7'] = Pawn('b')

        # White figures
        pieces['a1'] = Rook('w')
        pieces['b1'] = Knight('w')
        pieces['c1'] = Bishop('w')
        pieces['d1'] = Queen('w')
        pieces['e1'] = King('w')
        pieces['f1'] = Bishop('w')
        pieces['g1'] = Knight('w')
        pieces['h1'] = Rook('w')

        # black figures
        pieces['a8'] = Rook('b')
        pieces['b8'] = Knight('b')
        pieces['c8'] = Bishop('b')
        pieces['d8'] = Queen('b')
        pieces['e8'] = King('b')
        pieces['f8'] = Bishop('b')
        pieces['g8'] = Knight('b')
        pieces['h8'] = Rook('b')

        return pieces

    def print_board(self):
        board_state = []
        for row in range(8, 0, -1):
            board_row = []
            board_row.append(str(row))
            for col in 'abcdefgh':
                piece = self.board.get(col + str(row), None)
                if piece:
                    board_row.append(piece.symbol)
                else:
                    board_row.append('.')
            board_row.append(str(row))
            board_state.append(board_row)
        board_state.append(list(' abcdefgh '))
        return board_state

    def move_piece(self, from_pos: str, to_pos: str):
        piece = self.board.get(from_pos)
        if not piece:
            print("No piece at specified position")
            return

        move_checks = {
            Pawn: Pawn.can_move,
            Rook: Rook.can_move,
            Knight: Knight.can_move,
            Bishop: Bishop.can_move,
            Queen: Queen.can_move,
            King: King.can_move
        }

        move_func = move_checks.get(type(piece))
        if not move_func or not move_func(piece, from_pos, to_pos, self.board):
            print(f"Invalid move for {type(piece).__name__}")
            return

        self.board[to_pos] = piece
        self.board[from_pos] = None

board = Board()