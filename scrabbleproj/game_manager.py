import random
from turtle import width


import pygame

from scrabbleproj.board import Board
from scrabbleproj.buttons import Button, swapbutton, endturn
from scrabbleproj.constants import BLACK, HEIGHT, WHITE, DECK_Y_AXIS, WIDTH, BONUS_TILE_COORDS
from scrabbleproj.player import Player
from scrabbleproj.tile import Tile
from scrabbleproj.tile_bag import TileBag
from scrabbleproj.words import Words


class GameManager:

    def __init__(self, window):
        self.tile_prior_placement = None
        self.last_tile_selected_in_hand = None
        self.last_tile_placed = None
        self.window = window
        self.board = Board(self.window)
        self.tile_bag = TileBag()
        self.words = Words()
        self.tile = Tile(self)
        # self.word_being_played = []
        # self.tile = Tile()

        
        self.player_one = Player("Player One", self.tile_bag, self.window, (101, 100))
        self.player_two = Player("Player Two", self.tile_bag, self.window, (401, 400))

        print(f"Initial tile bag qty: {self.tile_bag.get_tile_bag_count()}")
        
        self.turn_end = False
        self.current_player = self.player_one
        self.update_player_turn()

        self.swapbutton = swapbutton
        self.end_turn_button = endturn

        self.board.draw_player_score(self.player_one)
        self.board.draw_player_score(self.player_two)
        self.swapbutton.draw_button(self.window)
        self.end_turn_button.draw_button(self.window)
        
        
        

        print(f"Tile bag qty after player creation: {self.tile_bag.get_tile_bag_count()}")
        
        
        self.board.draw_tile_bag_count(self.tile_bag)
        self.selected_tile = None
        self.selected_tile_location = None
        self.tile_area_clicked = None
        self.tiles_to_replenish_at_turn_end = []
        print(self.current_player.player_deck.deck_tiles)

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
                print(f"EVENT BUTTON {event.button}")
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                    print("Removing board tile")
                    print(f"Before removing tile {self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]].letter}")
                    self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]] = self.tile_prior_placement
                    self.board.update_tile(self.tile_prior_placement, self.tile_prior_placement.tile_location)
                    print(f"After removing tile {self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]].letter}")
                    self.handle_reactivation()
                    # if self.last_tile_placed.tile_location in BONUS_TILE_COORDS.get("TRIPPLE_WORD_COORDS"):
                    #     pass
                    # elif self.last_tile_placed.tile_location in BONUS_TILE_COORDS.get("TRIPPLE_LETTER_COORDS"):
                    #     pass
                    # elif self.last_tile_placed.tile_location in BONUS_TILE_COORDS.get("DOUBLE_WORD_COORDS"):
                    #     pass
                    # elif self.last_tile_placed.tile_location in BONUS_TILE_COORDS.get("DOUBLE_LETTER_COORDS"):
                    #     pass
                    # else: #for normal tiles 
                    #     pass
                        
                        
                else:
                    self.handle_board_placement(cursor_location)
            # Determine which tile user has clicked onto
            if self.current_player.player_deck.clicked_in_deck(cursor_location):
                self.handle_hand_select(cursor_location)
            #     Determine which tile has been clicked in on the deck
            if swapbutton.isOver(cursor_location):
                self.handle_tile_swap()
            if endturn.isOver(cursor_location):
                self.handle_end_turn()



    def handle_check_if_word(self):
        print("Running Word Check")
        word_score = self.words.check_if_word(self.board, self.last_tile_placed)
        print('player score')
        if type(word_score) == int:
            self.current_player.score += word_score
        else:
            print("not a word bud")
        
        print(f"player 1 score = {self.player_one.score}")
        print(f"player 2 score = {self.player_two.score}")

        self.board.draw_player_score(self.current_player)
        

    def handle_board_placement(self, cursor_location):
        cell_clicked = self.board.get_tile_pos(cursor_location)
        board_data_object_location = self.board.board[cell_clicked[0]][cell_clicked[1]]
        self.tile_prior_placement = self.board.board[cell_clicked[0]][cell_clicked[1]]

        print("board_data_object")
        print(board_data_object_location)
        print(cell_clicked)

        if self.selected_tile and self.selected_tile.disabled is False:
            self.board.board[cell_clicked[0]][cell_clicked[1]] = self.selected_tile
            place_holder_tile = Tile(None)
            place_holder_tile.disabled = True
            blank_tile_placeholder = (place_holder_tile, self.selected_tile_location)
            self.current_player.player_deck.update_tile_in_deck(blank_tile_placeholder)
            print("Selected tile location")
            print(cell_clicked)
            self.selected_tile.tile_location = cell_clicked
            print(f"Bens edited tile location {self.selected_tile.tile_location}")
            print(self.last_tile_selected_in_hand)
            self.current_player.player_deck.disable_tile(self.last_tile_selected_in_hand)
            self.board.update_tile(self.selected_tile, board_data_object_location.tile_location)
            self.last_tile_placed = cell_clicked
            
            self.selected_tile.disabled = True
            #the change i did which when a tile is placed removes it from the players deck on placement (interferes )
            # selected_tile_position_in_list = self.current_player.player_deck.get_location_in_deck(self.selected_tile)
            # self.current_player.player_deck.deck_tiles.pop(selected_tile_position_in_list)
            
            
            # self.word_being_played.append(self.selected_tile.letter)
            # self.tiles_to_replenish_at_turn_end.append(self.selected_tile)
            self.selected_tile = None
        #     We need to add new tiles at end of turn and re-draw deck
        else:
            print("Tile not selected from deck")

        self.board.display_board()

    def handle_hand_replacement(self):
        copy_of_player_deck = self.current_player.player_deck.deck_tiles.copy() #copying the player deck so that it doesnt point to the same object
        for index, tile in enumerate(copy_of_player_deck):
            print(tile)
            if tile[0].disabled:
                self.current_player.player_deck.deck_tiles.pop(index)
                new_tile = random.choice(self.tile_bag.tile_bag_items)
                self.current_player.player_deck.deck_tiles.insert(index, (new_tile, tile[1]))
                self.tile_bag.tile_bag_items.remove(new_tile)
                print("disabled tile")
                
    def handle_reactivation(self):
        print('the tile')
        print(self.last_tile_placed)
        self.last_tile_placed[1].disabled = False
        self.board.update_tile(self.last_tile_placed)

        
             
                
        

    def handle_hand_select(self, position):
        self.tile_area_clicked = self.current_player.player_deck.get_tile_clicked(position)
        print("tile bug")
        print(self.tile_area_clicked)
        self.selected_tile = self.current_player.player_deck.deck_tiles[self.tile_area_clicked][0]
        print(self.selected_tile)
        print(self.selected_tile.letter)

        print("running letters")

        for letter in self.current_player.player_deck.deck_tiles:
            print(letter[0].disabled)

        #if self.selected_tile.disabled:
           # print("This is a placeholder tile")
            #return

        self.selected_tile_location = self.current_player.player_deck.deck_tiles[self.tile_area_clicked][1]
        self.last_tile_selected_in_hand = self.selected_tile_location
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

    def handle_rules(self):
        WIN2 = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('rules')
        WIN2.fill(BLACK)
       
            
        
        
    
    def handle_end_turn(self):
        print(self.last_tile_placed)
        self.handle_check_if_word()
        self.handle_hand_replacement()
        self.board.draw_tile_bag_count(self.tile_bag)
        

        if self.current_player == self.player_two:
            self.current_player = self.player_one
        else:
            self.current_player = self.player_two

        #self.tiles_to_replenish_at_turn_end = []
        self.update_player_turn()

        print(f"It is player: {self.current_player.player_name} turn")

    def update_player_turn(self):
        player_turn = Button((WHITE), 50, 815, 100, 40, (f'Its {self.current_player.player_name}s turn !'))
        players_go_button = player_turn
        players_go_button.draw_button(self.window)
        self.current_player.player_deck.draw_deck()
    
    def add_to_player_score(self):
        print(self.current_player.score)
        self.current_player.score += self.calc_score_to_add()
        
    def draw(self):
        pass

    def update(self, delta):
        pass
