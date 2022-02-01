from scrabbleproj.deck import Deck


class Player:
    def __init__(self, player_name, tile_bag, window):
        self.player_name = player_name
        self.tile_bag = tile_bag
        self.window = window
        self.player_deck = Deck(self.tile_bag, window)

        self.create_player_deck()

    def create_player_deck(self):
        self.player_deck.create_random_tile_deck()
