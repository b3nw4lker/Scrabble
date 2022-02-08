import imp
import pygame
from scrabbleproj.tile_bag import TileBag

from .constants import BLACK, COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE, BONUS_TILE_LOCATIONS


class Board:
    def __init__(self, window):
        self.board = [[object() for col in range(COLS)] for row in range(ROWS)]
        self.board[0][0] = -1
        print(self.board)
        #self.board = [object(), object(), object()] # Maybe this needs to be empty strings or other and replaced with objects
        # .append(object())
        # https://www.geeksforgeeks.org/multi-dimensional-lists-in-python/
        # a = [[], [], []]
        # for record in a:
        #     print(record)
        # [{cell: (location), tile: Tile()}, {cell: (location), tile: object()}, {cell: (location), tile: object()}, {cell: (location), tile: object()}, {cell: (location), tile: object()}]
        # [3, 6, 9, 12, 15]
        # [4, 8, 12, 16, 20]
        self.win = window
        self.selected_tile = None
        self.tile_bag = TileBag()
        self._draw_squares()
        self._draw_tile_boosters()
        self._draw_swap_button()
        self._draw_tile_bag_count()

    # draself.wing the grid for scrabble
    def _draw_squares(self):
        self.win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.win, ORANGE, rect, 1)

    def draw_player_score(self, player_name, location):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 12)
        score = font.render(f"{player_name}'s Score :", True, BLACK)
        self.win.blit(score, (871, location[0]))
        player2scorebox = pygame.Rect(870, location[1], 100, 40)
        pygame.draw.rect(self.win, ORANGE, player2scorebox, 1)

    # Swap Tile Button
    def _draw_swap_button(self):
        button_pressed = False
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 12)
        score = font.render("Swap tile", True, BLACK)
        self.win.blit(score, (510, 880))
        swapbuttonbox = pygame.Rect(500, 870, 100, 40)
        pygame.draw.rect(self.win, ORANGE, swapbuttonbox, 1)
        pos = pygame.mouse.get_pos()
        if swapbuttonbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and not button_pressed: # Making it so that only one click is registered as a positive output
                # FIXME: This isn't right
                button_pressed = True
                print('Clicked')
                button_pressed = False

    # triple word placement
    def _draw_tile_boosters(self):
        for tile_name, tile_locations in BONUS_TILE_LOCATIONS.items():
            for tile in tile_locations:
                self.win.blit(tile_name, tile)
    
    def _draw_tile_bag_count(self):
        ammount = self.tile_bag.get_tile_bag_count()
        font = pygame.font.Font('freesansbold.ttf', 12)
        tile_bag_counter = font.render("Tiles Remaining :" + str(ammount), True, BLACK)
        self.win.blit(tile_bag_counter, (810, 880))
        tilebagbox = pygame.Rect(800, 870, 150, 40)
        pygame.draw.rect(self.win, ORANGE, tilebagbox, 1)
        