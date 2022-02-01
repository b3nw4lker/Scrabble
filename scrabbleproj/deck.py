import random

import pygame

from scrabbleproj.constants import SQUARE_SIZE, DECK_Y_AXIS, ORANGE


class Deck:
    def __init__(self, tile_bag, window):
        self.win = window
        self.deck_tiles = []
        self.tile_bag = tile_bag
        self._draw_deck()

    def create_random_tile_deck(self):
        tile_locations_x = [0, 54, 107, 162, 216, 270, 324]

        for location in tile_locations_x:
            random_tile_selected = random.choice(self.tile_bag.tile_bag_items)
            # Deck Tiles are a tuple - First element is Tile object, second is the x deck tile location
            # (tile_locations list)
            self.deck_tiles.append((random_tile_selected, location))
            self.tile_bag.tile_bag_items.remove(random_tile_selected)

        self._draw_deck()

    # drawing the deck 7 boxes long
    def _draw_deck(self):
        for x in range(7):
            deck_boxes = pygame.Rect(x * SQUARE_SIZE, DECK_Y_AXIS, 53, 53)
            pygame.draw.rect(self.win, ORANGE, deck_boxes, 1)

        for tile_object in self.deck_tiles:
            self._draw_tile(tile_object)

    def _draw_tile(self, tile):
        self.win.blit(tile[0].image, (tile[1], DECK_Y_AXIS))

    # WARNING DO NOT USE THIS METHOD IT WILL CREATE A RANDOM DISASSOCIATED TILE!!!!
    # def override_tile(self):
    #     self.deck_tiles[0] = (Tile("Z"), 0)
    #     self.draw_tile(self.deck_tiles[0])

    def swap_tile(self, tile):
        # Public we call this from the player
        pass
