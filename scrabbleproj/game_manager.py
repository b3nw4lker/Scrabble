
from locale import currency
import random
import pygame

from scrabbleproj.board import Board
from scrabbleproj.buttons import Button, swapbutton, endturn, skipturn, whowon
from scrabbleproj.constants import BLACK, BLANKBOARDTILE, BONUS_TILE_LOCATIONS, DOUBLELETTERIMG, DOUBLEWORDIMG, HEIGHT, ORANGE, SQUARE_SIZE, STARTTILE, TRIPLELETTERIMG, TRIPLEWORDIMG, WHITE, DECK_Y_AXIS, WIDTH, BONUS_TILE_COORDS
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

        self.who_won = whowon
        self.swapbutton = swapbutton
        self.swap_ammount = 7
        self.end_turn_button = endturn
        self.skip_turn_button = skipturn
        self.tiles_have_been_placed = False
        

        self.board.draw_player_score(self.player_one)
        self.board.draw_player_score(self.player_two)
        self.swapbutton.draw_button(self.window)
        self.end_turn_button.draw_button(self.window)
        self.skip_turn_button.draw_button(self.window)
        
        
        

        print(f"Tile bag qty after player creation: {self.tile_bag.get_tile_bag_count()}")
        # self.ai_possibility()
        
        
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
                if event.type == pygame.MOUSEBUTTONUP and event.button == 3 and self.last_tile_placed != None:
                    print("Removing board tile")
                    print(f"Before removing tile {self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]].letter}")
                    self.handle_reactivation(self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]])
                    self.current_player.player_deck.draw_deck() #draw_deck_partially will be used 
                    self.handle_board_booster_replacement()
                    # self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]] = self.tile_prior_placement
                    # self.board.update_tile(self.tile_prior_placement, self.tile_prior_placement.tile_location)
                    # print(f"After removing tile {self.tile_prior_placement}")
                                           
                        
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
            if skipturn.isOver(cursor_location) and self.tiles_have_been_placed is False:
                self.handle_skip_turn()



    def handle_check_if_word(self):
        print("Running Word Check")
        word_score = self.words.check_if_word(self.board, self.last_tile_placed)
        print('player score')
        if type(word_score) == int:
            self.current_player.score += word_score
            self.is_a_word = True
        else:
            print("not a word bud")
            self.is_a_word = False
        
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
            print(self.current_player.player_deck.deck_tiles)
           
            
            self.selected_tile.disabled = True
            #the change i did which when a tile is placed removes it from the players deck on placement (interferes )
            # selected_tile_position_in_list = self.current_player.player_deck.get_location_in_deck(self.selected_tile)
            # self.current_player.player_deck.deck_tiles.pop(selected_tile_position_in_list)
            
            
            # self.word_being_played.append(self.selected_tile.letter)
            # self.tiles_to_replenish_at_turn_end.append(self.selected_tile)
            self.selected_tile = None
            self.tiles_have_been_placed = True
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
    
    def handle_board_booster_replacement(self):
        tile_pos_tuple = self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]].tile_location
        tile_pos_list = list(tile_pos_tuple)
        print(tile_pos_list)
        tile_pos_list[0] = tile_pos_list[0] * SQUARE_SIZE
        tile_pos_list[1] = tile_pos_list[1] * SQUARE_SIZE
        new_tuple_coords = tuple(tile_pos_list)
        print(new_tuple_coords)
        print('new img now')
        if new_tuple_coords in BONUS_TILE_LOCATIONS.get(TRIPLEWORDIMG):
            self.window.blit(TRIPLEWORDIMG,(new_tuple_coords))  
            print("done1")
        elif new_tuple_coords in BONUS_TILE_LOCATIONS.get(DOUBLEWORDIMG):
            self.window.blit(DOUBLEWORDIMG,(new_tuple_coords))
            print("2")  
        elif new_tuple_coords in BONUS_TILE_LOCATIONS.get(TRIPLELETTERIMG):
            self.window.blit(TRIPLELETTERIMG,(new_tuple_coords))  
            print("3") 
        elif new_tuple_coords in BONUS_TILE_LOCATIONS.get(DOUBLELETTERIMG):
            self.window.blit(DOUBLELETTERIMG,(new_tuple_coords))    
            print("4")
        elif new_tuple_coords in BONUS_TILE_LOCATIONS.get(STARTTILE):
            self.window.blit(STARTTILE,(new_tuple_coords))
            print("5")
        else:
            self.window.blit(BLANKBOARDTILE,(new_tuple_coords))
            print("6")
        self.board.board[self.last_tile_placed[0]][self.last_tile_placed[1]] = self.tile_prior_placement
        # self.board.update_tile(self.tile_prior_placement, self.tile_prior_placement.tile_location)        
        
     
                
    def handle_reactivation(self,word):
        print('the tile')
        print(word.letter)
        word.disabled = False
    
      
        
    # def ai_possibility(self):
    #     ai_letters = []
    #     for tile in range(len(self.player_two.player_deck.deck_tiles) + 1):
    #         tile_1 = self.player_two.player_deck.deck_tiles[tile-1]
    #         ai_letters.append(tile_1[0].letter)
    #     ai_letters_str = ''.join([str(item) for item in ai_letters])
    #     rest_of_word = ai_letters[0]
    #     ai_tail_str = ''.join([str(item) for item in rest_of_word]) 
    #     word_not_made = True
    #     true_word = []
        
    #     while word_not_made is True:
    #         list1 = [] 
    #         for tile in ai_letters:
    #             letter = random.choice(ai_letters)
    #             list1.append(letter)
    #             ai_letters.remove(letter)
    #         word_str =  ''.join([str(item) for item in list1])              
    #         if self.words.does_word_exist(word_str):
    #             true_word.append(word_str)
    #             word_not_made = False
    #     print(true_word)
                
        
        
        # pos1_in_word = str(ai_letters[1])
        # possible_words = [ai_letters_str.replace((pos1_in_word),letter) for letter in ai_tail_str]
        # for word in possible_words:
        #     if self.words.does_word_exist(word):
        #         use_word = word
        #         print(use_word)
        #     else: 
        #         print("no words")
              
        
                           
     
        
             
    def did_game_end(self):
        if self.player_one.score > 12:
            print('game is over')
            self.who_won = Button((ORANGE), 850, 650, 150, 40,  (f'Player 1 wins'))
            self.who_won.draw_button(self.window)
        elif self.player_two.score > 12:
            self.who_won = Button((ORANGE), 850, 650, 150, 40,  (f'Player 2 wins'))
            self.who_won.draw_button(self.window)
        else:
            pass
           
            
            
            
               
        

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
        if self.selected_tile and self.swap_ammount > 0:
            selected_tile_position_in_list = self.current_player.player_deck.get_location_in_deck(self.selected_tile)
            self.current_player.player_deck.deck_tiles.pop(selected_tile_position_in_list)
            new_tile = (random.choice(self.tile_bag.tile_bag_items), self.selected_tile_location)
            self.tile_bag.tile_bag_items.remove(new_tile[0])
            self.current_player.player_deck.deck_tiles.insert(self.tile_area_clicked, new_tile)
            self.current_player.player_deck.deck_tiles.append(new_tile)
            self.tile_bag.tile_bag_items.append(self.selected_tile)
            self.current_player.player_deck.update_tile_in_deck(new_tile)
            self.selected_tile = None
            self.swap_ammount -= 1
            swapbutton = Button((ORANGE) , 620, 870, 110, 40, (f"Swap [{self.swap_ammount}]"))
            swapbutton.draw_button(self.window)
        else:
            print("click a tile to swap then press")

    def handle_rules(self):
        WIN2 = pygame.display.set_mode((600, 600))
        pygame.display.set_caption('rules')
        WIN2.fill(BLACK)
       
            
    def handle_skip_turn(self): #if the player doesnt want to play a round -> skips 
        self.swap_ammount = 7
        self.swapbutton.draw_button(self.window)
        if self.current_player == self.player_two:
            self.current_player = self.player_one
        else:
            self.current_player = self.player_two
        self.update_player_turn()      
    
    
    
    def handle_end_turn(self): #ends the go changes to the other player 
        print(self.last_tile_placed)
        self.tiles_have_been_placed = False
        self.swap_ammount = 7
        self.handle_check_if_word()
        self.did_game_end()
        self.handle_hand_replacement()
        self.board.draw_tile_bag_count(self.tile_bag)
        swapbutton = Button((ORANGE) , 620, 870, 110, 40, (f"Swap [7]"))
        swapbutton.draw_button(self.window)
        if self.current_player == self.player_two:
            self.current_player = self.player_one
        else:
            self.current_player = self.player_two
            
        self.update_player_turn()

        

        #self.tiles_to_replenish_at_turn_end = []
        

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
