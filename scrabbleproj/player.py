from tkinter import NONE
from scrabbleproj.constants import SQUARE_SIZE
from scrabbleproj.deck import Deck



class Player():
    def __init__(self, player_name, tile_bag, window, score_location):
        self.player_name = player_name
        self.tile_bag = tile_bag
        self.window = window
        self.score = 0
        self.player_deck = Deck(self.tile_bag, window)
        self.score_location = score_location


        
        self.create_player_deck()

    def create_player_deck(self):
        self.player_deck.create_random_tile_deck()
        
    
        

