import pygame
from board import Board
from square import Square
from const import ROWS, COLS, SQSIZE
from dragger import Dragger

class Game:
    def __init__(self):
        self.board = Board()
        self.dragger = Dragger()


    # blit methods
    def show_bg(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                if(row + col) % 2 == 0:
                    color = (255, 255, 255) # white
                else:
                    color = (40, 40, 40) # gray

                rect = (col * SQSIZE, row * SQSIZE, SQSIZE, SQSIZE)

                pygame.draw.rect(surface, color, rect)

    def show_pieces(self, surface):
        for row in range(ROWS):
            for col in range(COLS):
                # Piece ?
                if self.board.squares[row][col].has_piece():
                    piece = self.board.squares[row][col].piece

                    # All pieces expect dragger piece.
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        img = pygame.image.load(piece.texture)
                        img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2  # Center the image on X-axis
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img, piece.texture_rect)

    
    def show_moves(self, surface):
        if self.dragger.dragging:
            piece = self.dragger.piece
            # Loop all possible moves.
            for move in piece.moves:
                # Show color.
                color = '#C86464' if (move.final.row + move.final.col) % 2 == 0 else '#C84646'
                # Make rectangle.
                rect = (move.final.col * SQSIZE, move.final.row * SQSIZE, SQSIZE, SQSIZE)
                # Display blit.
                pygame.draw.rect(surface, color, rect)
