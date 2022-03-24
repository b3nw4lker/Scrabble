import pygame
from scrabbleproj.tile_bag import TileBag

from .constants import BLACK, COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE, BONUS_TILE_LOCATIONS
from .tile import Tile


class Board:
    def __init__(self, window):
        self.board = [[Tile(None) for col in range(COLS)] for row in range(ROWS)]
        self.position = (0, 0) # Check this what is this??

        print(self.board)
        for row in self.board:
            print(row)
            print('/n')

        self._board_size = (15 * SQUARE_SIZE, 15 * SQUARE_SIZE)
        self._rect = pygame.Rect(self.position, self._board_size)
        self.win = window
        self.selected_tile = None
        self.tile_bag = TileBag()
        self._draw_squares()
        self._draw_tile_boosters()
        self._draw_tile_bag_count()

    def clicked_in_board(self, cursor_location):
        return self._rect.collidepoint(cursor_location)
        
    # drawself.win the grid for scrabble
    def _draw_squares(self):
        self.win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                self.board[x][y].tile_location = (x * SQUARE_SIZE, y * SQUARE_SIZE)
                rect = pygame.Rect(x * SQUARE_SIZE, y * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.win, ORANGE, rect, 1)

    def draw_player_score(self, player, location):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 12)
        score = font.render(f"{player.player_name}'s Score :{player.score}", True, BLACK)
        self.win.blit(score, (871, location[0]))
        player2scorebox = pygame.Rect(870, location[1], 100, 40)
        pygame.draw.rect(self.win, ORANGE, player2scorebox, 1)

    # triple word placement
    def _draw_tile_boosters(self):
        grid_line = []
        for tile_name, tile_locations in BONUS_TILE_LOCATIONS.items():
            grid_line.append(Tile(None))
            for tile in tile_locations:
                # self.board.append(grid_line)
                self.win.blit(tile_name, tile)

    def update_tile(self, tile, tile_location):
        self.win.blit(tile.image, (tile_location[0], tile_location[1]))
    
    def _draw_tile_bag_count(self):
        ammount = self.tile_bag.get_tile_bag_count()
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf', 12)
        tile_bag_counter = font.render("Tiles Remaining :" + str(ammount), True, BLACK)
        self.win.blit(tile_bag_counter, (810, 880))
        tilebagbox = pygame.Rect(800, 870, 150, 40)
        pygame.draw.rect(self.win, ORANGE, tilebagbox, 1)

    def get_tile_pos(self, position):
        position[0] -= self.position[0]
        position[1] -= self.position[1]

        # Calculate integer division
        return (position[0] // SQUARE_SIZE,
                position[1] // SQUARE_SIZE)

    def find_word_on_board(self):
        print('W')
        # word = []
        # for col in self.board:
        #     for tile in col:
        #         letter_in_word = tile
        #         print('this is ')
        #         word.append(letter_in_word)
        #         print(len(word))
        #         print('it worked!!!!!!!')

