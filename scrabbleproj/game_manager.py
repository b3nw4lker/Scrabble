from scrabbleproj.board import Board
from scrabbleproj.deck import Deck, TileBag
from scrabbleproj.player import Player


class GameManager:

    def __init__(self, window):
        self.window = window
        self.board = Board(self.window)
        # self.tile_bag = TileBag() # List of Tiles
        # self.words = Words()
        self.deck = Deck(self.window)
        # How deck relate to players - Rebuild deck so that we create a deck on a player
        # Player contains their Deck
        self.player_one = Player()

        self.player_one.draw_deck(self.deck)