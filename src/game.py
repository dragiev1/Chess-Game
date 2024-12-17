import pygame
from board import Board
from square import Square
from const import ROWS, COLS, SQSIZE

class Game:
    def __init__(self):
        self.board = Board()


    # Show methods
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
                    img = pygame.image.load(piece.texture)
                    img_center = col * SQSIZE + SQSIZE//2, row * SQSIZE + SQSIZE//2  # Center the image on X-axis
                    piece.texture_rect = img.get_rect(center = img_center)
                    surface.blit(img, piece.texture_rect)