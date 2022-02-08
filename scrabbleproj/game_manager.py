from pickle import FALSE, TRUE
from pprint import pprint

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

        # self.player_two = Player("Ben", self.tile_bag, self.window)
        # self.board.draw_player_score(self.player_two.player_name, (401, 400))

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

        # print(event)
        if event.type == pygame.MOUSEBUTTONUP: # need to add in and mouse pos is in the board collision zone
            cursor_location = list(pygame.mouse.get_pos())
            if self.board.clicked_in_board(cursor_location):
                cell_clicked = self.board.get_tile_pos(cursor_location)
                board_data_object_location = self.board.board[cell_clicked[0]][cell_clicked[1]]
                print(board_data_object_location)
                self.board.board[cell_clicked[0]][cell_clicked[1]] = "Clicked"


            # Determine which tile user has clicked onto
            elif self.player_one.player_deck.clicked_in_deck(cursor_location):
                self.handle_hand_select(cursor_location)
            #     Determine which tile has been clicked in on the deck
            # elif clicked in swap button:
            #     pass

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
        tile_area_clicked = self.player_one.player_deck.get_tile_clicked(position)
        self.selected_tile = self.player_one.player_deck.deck_tiles[tile_area_clicked][0]
        print(self.selected_tile.letter)
        self.selected_tile.clicked = True
        self.selected_tile.player_assigned = self.player_one

        print(self.selected_tile.clicked)
        print(self.selected_tile.player_assigned)
    

    def draw(self):
        pass

    def update(self, delta):
        # We are currently using clock.tick but could use this to make it all managed in the same place
        pass


