from scrabbleproj.constants import SQUARE_SIZE
from scrabbleproj.deck import Deck


class Player:
    def __init__(self, player_name, tile_bag, window):
        self.player_name = player_name
        self.tile_bag = tile_bag
        self.window = window
        self.score = 0
        self.player_deck = Deck(self.tile_bag, window)
        
        self.create_player_deck()
               

        print(self.player_deck.deck_tiles)

    def create_player_deck(self):
        self.player_deck.create_random_tile_deck()

