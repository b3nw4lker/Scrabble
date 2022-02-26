from distutils.errors import LibError
from pickle import FALSE, TRUE
from pprint import pprint
from tkinter import Button

import pygame
import random
from scrabbleproj.board import Board
from scrabbleproj.player import Player
from scrabbleproj.tile import Tile
from scrabbleproj.tile_bag import TileBag
from scrabbleproj.words import Words
from scrabbleproj.buttons import Button , swapbutton, endturn
from scrabbleproj.constants import LIGHT_ORANGE, ORANGE, WHITE

class GameManager:

    def __init__(self, window):
        self.window = window
        self.board = Board(self.window)
        self.tile_bag = TileBag()
        self.words = Words()
            
    
    
        print(f"Initial tile bag qty: {self.tile_bag.get_tile_bag_count()}")
        self.player_one = Player("Player One", self.tile_bag, self.window)
        self.player_two = Player("Player Two", self.tile_bag, self.window)

        self.turn_end = False
        if self.turn_end is False:
            self.current_player = self.player_one
        else:
            self.current_player = self.player_two
            return
        
        playerturn = Button((WHITE), 50, 815, 100, 40, (f'Its {self.current_player.player_name}s turn !'))
        
        self.swapbutton = swapbutton
        self.end_turn_button = endturn
        self.players_go_button = playerturn
            
        
        self.board.draw_player_score(self.player_one.player_name, (101, 100))
        self.board.draw_player_score(self.player_two.player_name, (401, 400))
        self.swapbutton.draw_button(self.window)
        self.end_turn_button.draw_button(self.window)
        self.players_go_button.draw_button(self.window)
        
        
       
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
        cursor_location = list(pygame.mouse.get_pos())
        if event.type == pygame.MOUSEBUTTONUP:
            if self.board.clicked_in_board(cursor_location):
                cell_clicked = self.board.get_tile_pos(cursor_location)
                board_data_object_location = self.board.board[cell_clicked[0]][cell_clicked[1]]
                print(board_data_object_location)
                self.board.board[cell_clicked[0]][cell_clicked[1]] = "Clicked"
            # Determine which tile user has clicked onto
            if self.current_player.player_deck.clicked_in_deck(cursor_location):
                self.handle_hand_select(cursor_location)
            #     Determine which tile has been clicked in on the deck
            if swapbutton.isOver(cursor_location):
                self.handle_tile_swap()
            if endturn.isOver(cursor_location):
                self.handle_end_turn()
                
        

    def handle_board_removal(self, x, y):
        Board.board[x][y] = object()

    def handle_board_placement(self, x, y):
        Board.board[x][y] = Tile.letter

    def handle_hand_replacement(self, position):
        pass
    

    def handle_hand_select(self, position):
        tile_area_clicked = self.current_player.player_deck.get_tile_clicked(position)
        self.selected_tile = self.current_player.player_deck.deck_tiles[tile_area_clicked][0]
        print(self.selected_tile.letter)
        self.selected_tile.clicked = True
        self.selected_tile.player_assigned = self.current_player

        print(self.selected_tile.clicked)
        print(self.selected_tile.player_assigned)
    
    def handle_tile_swap(self): # This is the issue the button clicking works all fine but the object in the list if different to the ones in the players tile deck for some reason 
        if self.selected_tile.clicked == True:
            selected_tile = self.selected_tile
            selected_tile_position_in_list = self.current_player.player_deck.deck_tiles.index(selected_tile)
            self.current_player.player_deck.deck_tiles.pop(selected_tile_position_in_list)
            self.current_player.player_deck.deck_tiles.append(random.choice(self.tile_bag.tile_bag_items))
        else:
            print("click a tile to swap then press")
    
    def handle_end_turn(self):
        if self.turn_end == False:
            self.turn_end == True
        else:
            self.turn_end == False
                
        
    def draw(self):
        pass

    def update(self, delta):
        # We are currently using clock.tick but could use this to make it all managed in the same place
        pass


        
        