from const import COLS, ROWS
from piece import Pawn, Knight, Bishop, Rook, King, Queen
from square import Square
from move import Move

class Board:
    
    def __init__(self):

        self.squares = [[0, 0, 0, 0, 0, 0, 0, 0] for col in range(COLS)]
        self.last_move = None
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def move(self, piece, move):
        initial = move.initial
        final = move.final
        # Console board move update.
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece
        # Move
        piece.moved = True
        # Clear valid moves.
        piece.clear_moves()
        # Set last move.
        self.last_move = move


    def valid_move(self, piece, move):
        return move in piece.moves

    # Calculate possible moves for each piece.
    def calc_moves(self, piece, row, col):
        '''
            Calculate all possible (valid) moves of a specific piece on a square.
        '''
        def pawn_moves():
            # Steps.
            steps = 1 if piece.moved else 2

            # Vertical moves.
            start = row + piece.dir
            end = row + (piece.dir*(1+steps))
            for possible_move_row in range(start, end, piece.dir):
                if Square.in_range(possible_move_row):
                    if self.squares[possible_move_row][col].isempty():
                        # Create initial and final move squares.
                        initial = Square(row, col)
                        final = Square(possible_move_row, col)
                        # Create new move.
                        move = Move(initial, final)
                        # Append move.
                        piece.add_move(move)
                    else:
                        # blocked
                        break
                else:
                    # Not in range
                    break

            # Diagonal moves.
            possible_move_row = row + piece.dir
            possible_move_cols = [col-1, col+1]
            for possible_move_col in possible_move_cols:
                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].has_rival(piece.color):
                        # Create initial and final move squares.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create new move.
                        move = Move(initial, final)
                        # Append move.
                        piece.add_move(move)

        def straightline_moves(incrs):
            for incr in incrs:
                row_incr, col_incr = incr
                possible_move_row = row + row_incr
                possible_move_col = col + col_incr

                while True:
                    if Square.in_range(possible_move_row, possible_move_col):
                        # Create initial and final move squares.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col)
                        # Create new move.
                        move = Move(initial, final)
                        
                        # Empty = continue looping.
                        if self.squares[possible_move_row][possible_move_col].isempty():
                            # Append move.
                            piece.add_move(move)
                        # Has enemy piece = add move + break
                        if self.squares[possible_move_row][possible_move_col].has_rival(piece.color):
                            # Append move.
                            piece.add_move(move)
                            break
                        # Has team piece = break.
                        if self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color):
                            break
                    else: break  # Not in range.
                        
                    # Incrementing incrs.
                    possible_move_row = possible_move_row + row_incr 
                    possible_move_col = possible_move_col + col_incr        

        def knight_moves():
            # 8 possible moves.
            possible_moves = [
                (row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-1)
            ]

            for possible_move in possible_moves:
                possible_move_row, possible_move_col = possible_move
                if Square.in_range( possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create squares for new move.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece.
                        # Create new move.
                        move = Move(initial, final)
                        piece.add_move(move)
                        # Append new valid move.

        def king_moves():
            adjs = [
                (row-1, col+0), # Up.
                (row-1, col+1), # Up-right.
                (row+0, col+1), # Right.
                (row+1, col+1), # Down-right.
                (row+1, col+0), # Down.
                (row+1, col-1), # Down-left.
                (row+0, col-1), # Left.
                (row-1, col-1), # Up-left.
            ]

            # Normal moves.
            for possible_move in adjs:
                possible_move_row, possible_move_col = possible_move

                if Square.in_range(possible_move_row, possible_move_col):
                    if self.squares[possible_move_row][possible_move_col].isempty_or_rival(piece.color):
                        # Create squares for new move.
                        initial = Square(row, col)
                        final = Square(possible_move_row, possible_move_col) # piece = piece.
                        # Create new move.
                        move = Move(initial, final)
                        piece.add_move(move)
                        # Append new valid move.

            # Castling moves.

            # Queen castling.
            
            # King castling.

        if isinstance(piece, Pawn): pawn_moves()
        elif isinstance(piece, Knight): knight_moves()

        elif isinstance(piece, Bishop): 
            straightline_moves([
                (-1, 1), # Upright.
                (-1, -1), # Upleft.
                (1, 1), # Downright.
                (1, -1), # Downleft.
        ])
        elif isinstance(piece, Rook): 
            straightline_moves([
                (-1, 0), # Up.
                (0, 1), # Right.
                (1, -0), # Down.
                (0, -1) # Left.
            ])
        elif isinstance(piece, Queen): 
            straightline_moves([
                (-1, 1), # Upright.
                (-1, -1), # Upleft.
                (1, 1), # Downright.
                (1, -1), # Downleft.
                (-1, 0), # Up.
                (0, 1), # Right.
                (1, -0), # Down.
                (0, -1) # Left.
            ])
        elif isinstance(piece, King): king_moves()
        
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
        self.squares[row_other][0] = Square(row_other, 0, Rook(color))
        self.squares[row_other][7] = Square(row_other, 7, Rook(color))
        # One Queen.
        self.squares[row_other][3] = Square(row_other, 3, Queen(color))
        # One King.
        self.squares[row_other][4] = Square(row_other, 4, King(color))