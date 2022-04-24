from operator import truediv
import random

import pygame
from scrabbleproj.constants import SQUARE_SIZE, DECK_Y_AXIS, ORANGE


class Deck:
    def __init__(self, tile_bag, window):
        self.win = window
        self.deck_tiles = []
        self.tile_bag = tile_bag
        self.position = (0, 870)
        self._deck_size = (7 * 54, 7 * 54)
        self._rect = pygame.Rect(self.position, self._deck_size)

    def clicked_in_deck(self, cursor_location):
        return self._rect.collidepoint(cursor_location)

    def create_random_tile_deck(self):
        tile_locations_x = [0, 54, 107, 162, 216, 270, 324]

        for location in tile_locations_x:
            random_tile_selected = random.choice(self.tile_bag.tile_bag_items)
            # Deck Tiles are a tuple - First element is Tile object, second is the x deck tile location
            # (tile_locations list)
            self.deck_tiles.append((random_tile_selected, location))
            self.tile_bag.tile_bag_items.remove(random_tile_selected)

    # drawing the deck 7 boxes long
    def draw_deck(self):
        for x in range(7):
            deck_boxes = pygame.Rect(x * SQUARE_SIZE, DECK_Y_AXIS, 53, 53)
            pygame.draw.rect(self.win, ORANGE, deck_boxes, 1)

        for tile_object in self.deck_tiles:
            self._draw_tile(tile_object)
            
    def draw_deck_partially(self):
        
        for tile_object in self.deck_tiles:
            if tile_object[0] is None:
                self._draw_tile(tile_object)
            else:
                pass

    

    def _draw_tile(self, tile):
        self.win.blit(tile[0].image, (tile[1], DECK_Y_AXIS))
        # Public we call this from the player

    def get_tile_clicked(self, position):
        position[0] -= self.position[0]

        selected_tile = position[0] // SQUARE_SIZE

        print("This is the selected tile")
        print(selected_tile)

        if selected_tile < len(self.deck_tiles):
            print("returning selected tile")
            return selected_tile
        else:
            print("returning -1")
            return -1

    def get_location_in_deck(self, tile_object):
        for index, tile in enumerate(self.deck_tiles):
            if tile[0] == tile_object:
                return index

        return None

    def update_tile_in_deck(self, tile_object):
        self._draw_tile(tile_object)

    def disable_tile(self, tile_location):
        pass
        # print("tile location")
        # print(tile_location)
        # self.deck_tiles[tile_location][0].disabled = True

    # def replenish_tiles(self, tiles_needing_replacing):
    #     for tile in tiles_needing_replacing:
    #         print(f"Tile needs replacing at location and index {tile}")



