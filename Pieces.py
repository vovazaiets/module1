from typing import Dict
class Piece:
    def __init__(self, color, symbol: str):
        self.color = color
        self.symbol = symbol

class Pawn(Piece):
    def __init__(self, color: str):
        symbol = '♙' if color == 'w' else '♟'
        super().__init__(color, symbol)
        self.first_move = True

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = int(to_pos[1]) - int(from_pos[1])

        if self.color == 'w' and rank_diff < 0:
            return False
        if self.color == 'b' and rank_diff > 0:
            return False

        if file_diff == 0 and abs(rank_diff) == 1 and to_pos not in board:
            return True
        elif file_diff == 0 and abs(rank_diff) == 2 and self.first_move:
            return True
        elif file_diff == 1 and abs(rank_diff) == 1 and to_pos in board and board[to_pos].color != self.color:
            return True
        else:
            return False



class Rook(Piece):
    def __init__(self, color: str):
        symbol = '♖' if color == 'w' else '♜'
        super().__init__(color, symbol)

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = abs(int(from_pos[1]) - int(to_pos[1]))

        if file_diff == 0 or rank_diff == 0:
            if to_pos in board:
                return board[to_pos].color != self.color
            return True
        else:
            return False



class Knight(Piece):
    def __init__(self, color: str):
        symbol = '♘' if color == 'w' else '♞'
        super().__init__(color, symbol)

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = abs(int(from_pos[1]) - int(to_pos[1]))

        if (file_diff == 2 and rank_diff == 1) or (file_diff == 1 and rank_diff == 2):
            if to_pos in board:
                return board[to_pos].color != self.color
            return True
        else:
            return False



class Bishop(Piece):
    def __init__(self, color: str):
        symbol = '♗' if color == 'w' else '♝'
        super().__init__(color, symbol)

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = abs(int(from_pos[1]) - int(to_pos[1]))

        if file_diff == rank_diff:
            if to_pos in board:
                return board[to_pos].color != self.color
            return True
        else:
            return False



class Queen(Piece):
    def __init__(self, color: str):
        symbol = '♕' if color == 'w' else '♛'
        super().__init__(color, symbol)

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = abs(int(from_pos[1]) - int(to_pos[1]))

        if file_diff == 0 or rank_diff == 0 or file_diff == rank_diff:
            if to_pos in board:
                return board[to_pos].color != self.color
            return True
        else:
            return False

class King(Piece):
    def __init__(self, color: str):
        symbol = '♔' if color == 'w' else '♚'
        super().__init__(color, symbol)

    def can_move(self, from_pos: str, to_pos: str, board: Dict[str, Piece]) -> bool:
        file_diff = abs(ord(from_pos[0]) - ord(to_pos[0]))
        rank_diff = abs(int(from_pos[1]) - int(to_pos[1]))

        if file_diff <= 1 and rank_diff <= 1:
            if to_pos in board:
                return board[to_pos].color != self.color
            return True
        else:
            return False
