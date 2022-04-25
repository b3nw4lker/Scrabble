from shutil import move
from tkinter import BOTH
from assets.allwords import worddict
from scrabbleproj.constants import BONUS_TILE_COORDS, POINTS
from scrabbleproj.tileboosters import TileBoost


class Words:

    def __init__(self):
        self.word_to_calc = ''
        self.points_per_letter = POINTS
        self.tileboost = TileBoost()
        self.word_score = 0 

    def check_if_word(self, board, last_tile_placed):
        horizontal_word = []
        vertical_word = []
        print(f"Last Tile Placed {board.board[last_tile_placed[0]][last_tile_placed[1]].letter}")

        # FIXME: If we place the horizontal tile last we need to use _create_row_representation to generate row

        row_representation = self._create_row_representation(board, last_tile_placed)

        # Check if words are right
        for index, tile in enumerate(row_representation, start=last_tile_placed[0]):
            if row_representation[index].letter:
                horizontal_word.append(row_representation[index])
                vertical_word = self._vertical_word_check(board, index, last_tile_placed, vertical_word)
                continue
            break

        # Check if words are left
        negative_count = 1
        for index, tile in enumerate(row_representation, start=last_tile_placed[0]):
            adjusted_index = index - negative_count

            if row_representation[adjusted_index].letter:
                horizontal_word.insert(0, row_representation[adjusted_index])
                negative_count += 2
                vertical_word = self._vertical_word_check(board, index, last_tile_placed, vertical_word)
                continue
            break

        if len(horizontal_word) == 1 and len(vertical_word) > 1:
            horizontal_word.clear()
        elif len(vertical_word) == 1 and len(horizontal_word) > 1:
            vertical_word.clear()

        print(f"Horizontal Words: {[word.letter for word in horizontal_word]}")
        print(f"Vertical Words: {[word.letter for word in vertical_word]}")
        
        
        print(''.join([word.letter.lower() for word in vertical_word]))
        print(''.join([word.letter.lower() for word in horizontal_word]))
        
        print("Before word check")
        
        vertical_word_check = ''
        horizontal_word_check = ''
        
        if len(horizontal_word) < 1:
            print('not a  hori word')
            horizontal_word_check = True #make it true as the word has no size
        else:
            horizontal_word_check = self.does_word_exist(''.join([word.letter.lower() for word in horizontal_word])) #List comprehension
            
            
    
    #verticle word getting boolean for if its true     
        if len(vertical_word) < 1:
            print('not a vert word') 
            vertical_word_check = True
            
        else:
            vertical_word_check = self.does_word_exist(''.join([word.letter.lower() for word in vertical_word]))#used so that it doesnt recognise the rutrned word as an object

        
        if horizontal_word_check == True and vertical_word_check == True:
            
            if len(vertical_word) != 0:
                return self.score_word(vertical_word)
                 
            else:
                pass
            
            if len(horizontal_word) != 0:
                return self.score_word(horizontal_word)
            else:
                pass
        
        elif horizontal_word_check == False or vertical_word_check == False:
            print('we cant score as isnt word')


            
        
        
        
        
        

        
        
    @staticmethod #doesn't need to have context of class (static method)
    def does_word_exist(word):
        # print(worddict.get(word))
        word_evaluation = worddict.get(word) == 1
        print(f"word {word} is {word_evaluation}")
        return word_evaluation
    
        
    

    @staticmethod #doesnt need to have context of class (static method) i can call without instantiating this will mean my code run quicker
    def _vertical_word_check(board, index, last_tile_placed, vertical_word):
        cell_above = board.board[index][last_tile_placed[1] - 1]
        cell_below = board.board[index][last_tile_placed[1] + 1]

        if cell_above.letter:
            for cell in board.board[index]:
                if cell.letter:
                    vertical_word.append(cell)

        if cell_below.letter:
            for cell in board.board[index]:
                if cell.letter:
                    vertical_word.append(cell)

        return vertical_word

    @staticmethod #doesnt need to have context of class (static method) i can call without instantiating - this will mean my code run quicker
    def _create_row_representation(board, last_tile_placed):
        board_representation = []
        for row in board.board:
            new_row = []
            for letter in row:
                new_row.append(letter.letter)

            board_representation.append(new_row)
        # Create row based on start location (the list is all flipped)

        row_representation = []
        for cell in range(15):
            row_representation.append(board.board[cell][last_tile_placed[1]])

        return row_representation

    #     return message showing which words are fake.

    # To return tiles to deck - we store all tiles placed in turn in a list, if turn can't be scored we run function to
    # move all tiles form list back to deck

    def score_word(self, word):
        self.word_score = 0
        tripple_letter_locations = BONUS_TILE_COORDS.get("TRIPPLE_LETTER_COORDS")
        double_letter_locations = BONUS_TILE_COORDS.get("DOUBLE_LETTER_CORDS") 
    
        for letter in word:
           # if letter.tile_location in BONUS_TILE_COORDS.get("TRIPPLE_LETTER_COORDS").values():
            if letter.tile_location in BONUS_TILE_COORDS.get("TRIPPLE_LETTER_COORDS"):
                booster_points = POINTS.get(letter.letter.upper())
                booster_points *= 3 #triple letter
                self.word_score += booster_points
                
            elif letter.tile_location in BONUS_TILE_COORDS.get("DOUBLE_LETTER_COORDS"):
                booster_points = POINTS.get(letter.letter.upper())
                booster_points *= 2 #double letter 
                self.word_score += booster_points
                
            else:
                self.word_score += POINTS.get(letter.letter.upper())


        for letter in word:
            if letter.tile_location in BONUS_TILE_COORDS.get("TRIPPLE_WORD_COORDS"):
                print("tripl the word score")
                self.word_score *= 3 #if tripple word
            if letter.tile_location in BONUS_TILE_COORDS.get("DOUBLE_WORD_COORDS"):
                self.word_score *= 2 #if double word    
            #word can be in both double word or triple letter so would need if statements rather than elif 
            
            
        print(self.word_score)
        
        
        #PSUEDO CODE FOR SCORE 
        
#       for tile.tileposition in word made:
#           if tile position is in BONUSTILECOORDS(triplewordecoordselection):
#               score x 3
        return self.word_score
            
            
            

   





