from pickle import FALSE, TRUE
import pygame
from scrabbleproj.board import Board
from scrabbleproj.player import Player
from scrabbleproj.tile import Tile
from scrabbleproj.tile_bag import TileBag
from scrabbleproj.words import Words


class GameManager:

    def __init__(self, window):
        self.window = window
        #self.position = position
        self.board = Board(self.window)
        self.tile_bag = TileBag()
        self.words = Words()
        print(f"Initial tile bag qty: {self.tile_bag.get_tile_bag_count()}")

        self.player_one = Player("Ashley", self.tile_bag, self.window)
        self.board.draw_player_score(self.player_one.player_name, (101, 100))

        self.player_two = Player("Ben", self.tile_bag, self.window)
        self.board.draw_player_score(self.player_two.player_name, (401, 400))

        print(f"Tile bag qty after player one creation: {self.tile_bag.get_tile_bag_count()}")

        self.selected_tile = None

        # self.event_actions = {
        #     'board_click': self.board.locations,
        #     'swap_tile_click': self.board.swap_loction
        # }

    def handle(self, event):
        """
        Handles all game events
        :param event: Game loop event
        :return:
        """
        if event == pygame.MOUSEBUTTONDOWN: # need to add in and mouse pos is in the board collision zone
            GameManager.handle_board_placement()
    

    #     if mouse button clicked:
    #             what action is the player taking:
    #                 call that function - e.g. handle_board_removal, handle_tile_swap

    def handle_board_removal(self, x, y):
        Board.board[x][y] = object()

    def handle_board_placement(self, x, y):
        Board.board[x][y] = Tile.letter
        #self.win.blit(tile_name, tile)
        
        
        
        

        #     pos = pygame.mouse.get_pos()
        #     print(pos)
        #     tile_pos = (pos[0]/54,pos[1]/54)
        #     print(tile_pos)
        # else:
        #     pass
        

    def handle_hand_replacement(self, position):
        pass

    def handle_hand_select(self, position):
        if pygame.MOUSEBUTTONDOWN:
            print(Player.player_deck[position])
    

        

    def draw(self):
        pass

    def update(self, delta):
        # We are currently using clock.tick but could use this to make it all managed in the same place
        pass


