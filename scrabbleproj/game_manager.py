import random
from tkinter import Button

import pygame

from scrabbleproj.board import Board
from scrabbleproj.buttons import Button, swapbutton, endturn
from scrabbleproj.constants import WHITE, DECK_Y_AXIS
from scrabbleproj.player import Player
from scrabbleproj.tile import Tile
from scrabbleproj.tile_bag import TileBag
from scrabbleproj.words import Words


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
        self.current_player = self.player_one
        self.update_player_turn()

        self.swapbutton = swapbutton
        self.end_turn_button = endturn

        self.board.draw_player_score(self.player_one.player_name, (101, 100))
        self.board.draw_player_score(self.player_two.player_name, (401, 400))
        self.swapbutton.draw_button(self.window)
        self.end_turn_button.draw_button(self.window)

        print(f"Tile bag qty after player one creation: {self.tile_bag.get_tile_bag_count()}")

        self.selected_tile = None
        self.selected_tile_location = None
        self.tile_area_clicked = None
        self.tiles_to_replenish_at_turn_end = []

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
                print("Cursor location")
                print(cursor_location)
                self.handle_board_placement(cursor_location)
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

    def handle_board_placement(self, cursor_location):
        cell_clicked = self.board.get_tile_pos(cursor_location)
        board_data_object_location = self.board.board[cell_clicked[0]][cell_clicked[1]]

        if self.selected_tile and not self.selected_tile.disabled:
            self.board.board[cell_clicked[0]][cell_clicked[1]] = self.selected_tile
            place_holder_tile = Tile(None)
            place_holder_tile.disabled = True
            blank_tile_placeholder = (place_holder_tile, self.selected_tile_location)
            self.current_player.player_deck.deck_tiles[self.current_player.player_deck.get_tile_clicked(cursor_location)] = blank_tile_placeholder
            self.current_player.player_deck.update_tile_in_deck(blank_tile_placeholder)
            self.board.update_tile(self.selected_tile, board_data_object_location.tile_location)
            self.tiles_to_replenish_at_turn_end.append(self.selected_tile)
            self.selected_tile = None
        #     We need to add new tiles at end of turn and re-draw deck
        else:
            print("Tile not selected from deck")

    def handle_hand_replacement(self, position):
        pass

    def handle_hand_select(self, position):
        self.tile_area_clicked = self.current_player.player_deck.get_tile_clicked(position)
        self.selected_tile = self.current_player.player_deck.deck_tiles[self.tile_area_clicked][0]

        if self.selected_tile.disabled:
            print("This is a placeholder tile")
            return

        self.selected_tile_location = self.current_player.player_deck.deck_tiles[self.tile_area_clicked][1]
        self.selected_tile.clicked = True
        self.selected_tile.player_assigned = self.current_player

    def handle_tile_swap(self):
        if self.selected_tile:
            selected_tile_position_in_list = self.current_player.player_deck.get_location_in_deck(self.selected_tile)
            self.current_player.player_deck.deck_tiles.pop(selected_tile_position_in_list)
            new_tile = (random.choice(self.tile_bag.tile_bag_items), self.selected_tile_location)
            self.current_player.player_deck.deck_tiles.insert(self.tile_area_clicked, new_tile)
            self.current_player.player_deck.deck_tiles.append(new_tile)
            self.tile_bag.tile_bag_items.append(self.selected_tile)
            self.current_player.player_deck.update_tile_in_deck(new_tile)
            self.selected_tile = None
        else:
            print("click a tile to swap then press")

    def handle_end_turn(self):
        print(f"Tiles needing to be replaced {self.tiles_to_replenish_at_turn_end}")
        self.current_player.player_deck.replenish_tiles(self.tiles_to_replenish_at_turn_end)

        if self.current_player == self.player_two:
            self.current_player = self.player_one
        else:
            self.current_player = self.player_two


        self.tiles_to_replenish_at_turn_end = []
        self.update_player_turn()

        print(f"It is player: {self.current_player.player_name} turn")

    def update_player_turn(self):
        player_turn = Button((WHITE), 50, 815, 100, 40, (f'Its {self.current_player.player_name}s turn !'))
        players_go_button = player_turn
        players_go_button.draw_button(self.window)
        self.current_player.player_deck.draw_deck()

    def draw(self):
        pass

    def update(self, delta):
        # We are currently using clock.tick but could use this to make it all managed in the same place
        pass
