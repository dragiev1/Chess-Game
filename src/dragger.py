import pygame

from const import SQSIZE

class Dragger:

    def __init__(self):
        self.piece = None
        self.dragging = False
        self.mouseX = 0
        self.mouseY = 0
        self.initial_row = 0
        self.initial_col = 0

    # blit method.
    def update_blit(self, surface):
        # Texture update.
        self.piece.set_texture(size=128)
        texture = self.piece.texture
        # Image.
        img = pygame.image.load(texture)
        # Rectangle.
        img_center = (self.mouseX, self.mouseY)
        self.piece.texture_rect = img.get_rect(center = img_center)
        # blit.
        surface.blit(img, self.piece.texture_rect)

    # Other methods.
    def update_mouse(self,pos):
        self.mouseX, self.mouseY = pos # (xcor, ycor)

    def save_initial(self, pos):
        self.initial_col = pos[0] // SQSIZE
        self.initial_row = pos[1] // SQSIZE
    
    def drag_piece(self, piece):
        self.piece = piece
        self.dragging = True
    
    def undrag_piece(self):
        self.piece = None
        self.dragging = False