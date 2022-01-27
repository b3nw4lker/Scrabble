import random

import pygame

from scrabbleproj.constants import POINTS, IMAGE, SQUARE_SIZE, DECK_Y_AXIS, ORANGE


class Tile:
    def __init__(self, letter):
        self.letter = letter
        self.points = POINTS.get(letter)
        self.image = IMAGE.get(letter)
        self.clicked = False

class Deck:
    def __init__(self, win):
        self.tile_bag = TileBag()
        self.win = win
        self.deck_tiles = []
        print(f"Initial tile bag qty: {self.tile_bag.get_tile_bag_count()}")

        self.create_random_tile_deck()
        self.draw_deck()

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
            self.draw_tile(tile_object)

    def draw_tile(self, tile):
        self.win.blit(tile[0].image, (tile[1], DECK_Y_AXIS))

    # WARNING DO NOT USE THIS METHOD IT WILL CREATE A RANDOM DISASSOCIATED TILE!!!!
    def over_ride_tile_image(self):
        self.deck_tiles[0] = (Tile("Z"), 0)
        self.draw_tile(self.deck_tiles[0])


class TileBag:
    def __init__(self):
        self.tile_bag_values = POINTS
        self.tile_bag_items = self.create_list_of_tile_bag()

    def create_list_of_tile_bag(self):
        tile_bag = []

        for tile_name, points in self.tile_bag_values.items():
            qty = points

            for qty_of_tile in range(0, qty):
                tile_bag.append(Tile(tile_name))

        return tile_bag

    def get_tile_bag_count(self):
        return len(self.tile_bag_items)
