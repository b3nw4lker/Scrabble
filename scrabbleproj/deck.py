import pygame
from scrabbleproj.constants import SQUARE_SIZE, DECK_Y_AXIS, ORANGE, TILE_VALUES

class Deck:
    def __init__(self):
        self.deck = []
        self.add_tiles_to_deck()
        
        
    def draw_deck(self, win):
        for x in range(7): 
            deckboxes = pygame.Rect(x*SQUARE_SIZE, DECK_Y_AXIS, 53, 53)
            pygame.draw.rect(win, ORANGE, deckboxes, 1)
            
    def add_tiles_to_deck(self):
        pass
        
        