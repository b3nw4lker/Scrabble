import pygame 
from .constants import WHITE, ORANGE, SQUARE_SIZE


class Board:
    def __init__(self):
        self.board = []
        self.selected_tile = None
    
    def draw_squares(self, win):
        win.fill(WHITE)
        pygame.draw.rect(win, ORANGE, (row *SQUARE_SIZE, col *SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        