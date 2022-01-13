import pygame 
from .constants import COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE


class Board:
    def __init__(self):
        self.board = []
        self.selected_tile = None
    
    def draw_squares(self, win):
        win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, ORANGE, rect, 1)
        
        