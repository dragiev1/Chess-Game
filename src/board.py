from const import COLS, ROWS
from piece import Pawn, Knight, Bishop, Rook, King, Queen
from square import Square

class Board:
    
    def __init__(self):

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
        
    # Private function to create Square objects on the board.
    def _create(self):
        
        for row in range(ROWS):
            for col in range(COLS):
                self.squares[row][col] = Square(row, col) 

    # Add pieces to the board.
    def _add_pieces(self, color):
        row_pawn, row_other = (6, 7) if color == 'white' else (1, 0)

        # All Pawns.
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn, col, Pawn(color))
        # All Knights.
        self.squares[row_other][1] = Square(row_other, 1, Knight(color))
        self.squares[row_other][6] = Square(row_other, 6, Knight(color))
        # All Bishops.
        self.squares[row_other][2] = Square(row_other, 2, Bishop(color))
        self.squares[row_other][5] = Square(row_other, 5, Bishop(color))
        # All Rooks.
        self.squares[row_other][0] = Square(row_other, 0, Bishop(color))
        self.squares[row_other][7] = Square(row_other, 7, Bishop(color))
        # One Queen.
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # One King.
        self.squares[row_other][4] = Square(row_other, 4, King(color))