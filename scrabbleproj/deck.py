

from ast import Gt
import pygame
import random
from scrabbleproj.constants import *

class Deck:
    def __init__(self):
        self.tile_bag = Tilebag().tile_bag
        self.random_deck = self.create_random_tile_deck()
    #creating a random reck for the player
    def create_random_tile_deck(self):
        random_deck = []
        print(self.tile_bag)
        for i in range(7):
            random_tile_selected = random.choice(self.tile_bag)
            random_deck.append(random_tile_selected)
            self.tile_bag.remove(random_tile_selected)
            
        return random_deck    
    #drawing the deck 7 boxes long 
    def draw_deck(self, win):
        for x in range(7): 
            deckboxes = pygame.Rect(x*SQUARE_SIZE, DECK_Y_AXIS, 53, 53)
            pygame.draw.rect(win, ORANGE, deckboxes, 1)
        
        #tile 1
        if self.random_deck[0] == 'A':
            tile_one = ATILE
        if self.random_deck[0] == 'B':
            tile_one = BTILE
        if self.random_deck[0] == 'C':
            tile_one = CTILE   
        if self.random_deck[0] == 'D':
            tile_one = DTILE    
        if self.random_deck[0] == 'E':
            tile_one = ETILE    
        if self.random_deck[0] == 'F':
            tile_one = FTILE
        if self.random_deck[0] == 'G':
            tile_one = GTILE   
        if self.random_deck[0] == 'H':
            tile_one = HTILE    
        if self.random_deck[0] == 'I':
            tile_one = ITILE   
        if self.random_deck[0] == 'J':
            tile_one = JTILE    
        if self.random_deck[0] == 'K':
            tile_one = KTILE 
        if self.random_deck[0] == 'L':
            tile_one = LTILE    
        if self.random_deck[0] == 'M':
            tile_one = MTILE   
        if self.random_deck[0] == 'N':
            tile_one = NTILE 
        if self.random_deck[0] == 'O':
            tile_one = OTILE
        if self.random_deck[0] == 'P':
            tile_one = PTILE
        if self.random_deck[0] == 'Q':
            tile_one = QTILE
        if self.random_deck[0] == 'R':
            tile_one = RTILE
        if self.random_deck[0] == 'S':
            tile_one = STILE
        if self.random_deck[0] == 'T':
            tile_one = TTILE
        if self.random_deck[0] == 'U':
            tile_one = UTILE
        if self.random_deck[0] == 'V':
            tile_one = VTILE
        if self.random_deck[0] == 'W':
            tile_one = WTILE
        if self.random_deck[0] == 'X':
            tile_one = XTILE
        if self.random_deck[0] == 'Y':
            tile_one = YTILE
        if self.random_deck[0] == 'Z':
            tile_one = ZTILE
        if self.random_deck[0] == 'BLANK':
            tile_one = BLANK  
            
        
        win.blit(tile_one,(0,DECK_Y_AXIS))
        
        
        
        #tile 2
        if self.random_deck[1] == 'A':
            tile_two = ATILE
        if self.random_deck[1] == 'B':
            tile_two = BTILE
        if self.random_deck[1] == 'C':
            tile_two = CTILE   
        if self.random_deck[1] == 'D':
            tile_two = DTILE    
        if self.random_deck[1] == 'E':
            tile_two = ETILE    
        if self.random_deck[1] == 'F':
            tile_two = FTILE
        if self.random_deck[1] == 'G':
            tile_two = GTILE   
        if self.random_deck[1] == 'H':
            tile_two = HTILE    
        if self.random_deck[1] == 'I':
            tile_two = ITILE   
        if self.random_deck[1] == 'J':
            tile_two = JTILE    
        if self.random_deck[1] == 'K':
            tile_two = KTILE 
        if self.random_deck[1] == 'L':
            tile_two = LTILE    
        if self.random_deck[1] == 'M':
            tile_two = MTILE   
        if self.random_deck[1] == 'N':
            tile_two = NTILE 
        if self.random_deck[1] == 'O':
            tile_two = OTILE
        if self.random_deck[1] == 'P':
            tile_two = PTILE
        if self.random_deck[1] == 'Q':
            tile_two = QTILE
        if self.random_deck[1] == 'R':
            tile_two = RTILE
        if self.random_deck[1] == 'S':
            tile_two = STILE
        if self.random_deck[1] == 'T':
            tile_two = TTILE
        if self.random_deck[1] == 'U':
            tile_two = UTILE
        if self.random_deck[1] == 'V':
            tile_two = VTILE
        if self.random_deck[1] == 'W':
            tile_two = WTILE
        if self.random_deck[1] == 'X':
            tile_two = XTILE
        if self.random_deck[1] == 'Y':
            tile_two = YTILE
        if self.random_deck[1] == 'Z':
            tile_two = ZTILE
        if self.random_deck[1] == 'BLANK':
            tile_two = BLANK  
            
        
        win.blit(tile_two,(54,DECK_Y_AXIS))
        
        #3 tile
        
        if self.random_deck[2] == 'A':
            tile_three = ATILE
        if self.random_deck[2] == 'B':
            tile_three = BTILE
        if self.random_deck[2] == 'C':
            tile_three = CTILE   
        if self.random_deck[2] == 'D':
            tile_three = DTILE    
        if self.random_deck[2] == 'E':
            tile_three = ETILE    
        if self.random_deck[2] == 'F':
            tile_three = FTILE
        if self.random_deck[2] == 'G':
            tile_three = GTILE   
        if self.random_deck[2] == 'H':
            tile_three = HTILE    
        if self.random_deck[2] == 'I':
            tile_three = ITILE   
        if self.random_deck[2] == 'J':
            tile_three = JTILE    
        if self.random_deck[2] == 'K':
            tile_three = KTILE 
        if self.random_deck[2] == 'L':
            tile_three = LTILE    
        if self.random_deck[2] == 'M':
            tile_three = MTILE   
        if self.random_deck[2] == 'N':
            tile_three = NTILE 
        if self.random_deck[2] == 'O':
            tile_three = OTILE
        if self.random_deck[2] == 'P':
            tile_three = PTILE
        if self.random_deck[2] == 'Q':
            tile_three = QTILE
        if self.random_deck[2] == 'R':
            tile_three = RTILE
        if self.random_deck[2] == 'S':
            tile_three = STILE
        if self.random_deck[2] == 'T':
            tile_three = TTILE
        if self.random_deck[2] == 'U':
            tile_three = UTILE
        if self.random_deck[2] == 'V':
            tile_three = VTILE
        if self.random_deck[2] == 'W':
            tile_three = WTILE
        if self.random_deck[2] == 'X':
            tile_three = XTILE
        if self.random_deck[2] == 'Y':
            tile_three = YTILE
        if self.random_deck[2] == 'Z':
            tile_three = ZTILE
        if self.random_deck[2] == 'BLANK':
            tile_three = BLANK  
            
        
        win.blit(tile_three,(108,DECK_Y_AXIS))
        
       #tile 4
         
        if self.random_deck[3] == 'A':
            tile_four = ATILE
        if self.random_deck[3] == 'B':
            tile_four = BTILE
        if self.random_deck[3] == 'C':
            tile_four = CTILE   
        if self.random_deck[3] == 'D':
            tile_four = DTILE    
        if self.random_deck[3] == 'E':
            tile_four = ETILE    
        if self.random_deck[3] == 'F':
            tile_four = FTILE
        if self.random_deck[3] == 'G':
            tile_four = GTILE   
        if self.random_deck[3] == 'H':
            tile_four = HTILE    
        if self.random_deck[3] == 'I':
            tile_four = ITILE   
        if self.random_deck[3] == 'J':
            tile_four = JTILE    
        if self.random_deck[3] == 'K':
            tile_four = KTILE 
        if self.random_deck[3] == 'L':
            tile_four = LTILE    
        if self.random_deck[3] == 'M':
            tile_four = MTILE   
        if self.random_deck[3] == 'N':
            tile_four = NTILE 
        if self.random_deck[3] == 'O':
            tile_four = OTILE
        if self.random_deck[3] == 'P':
            tile_four = PTILE
        if self.random_deck[3] == 'Q':
            tile_four = QTILE
        if self.random_deck[3] == 'R':
            tile_four = RTILE
        if self.random_deck[3] == 'S':
            tile_four = STILE
        if self.random_deck[3] == 'T':
            tile_four = TTILE
        if self.random_deck[3] == 'U':
            tile_four = UTILE
        if self.random_deck[3] == 'V':
            tile_four = VTILE
        if self.random_deck[3] == 'W':
            tile_four = WTILE
        if self.random_deck[3] == 'X':
            tile_four = XTILE
        if self.random_deck[3] == 'Y':
            tile_four = YTILE
        if self.random_deck[3] == 'Z':
            tile_four = ZTILE
        if self.random_deck[3] == 'BLANK':
            tile_four = BLANK  
            
        
        win.blit(tile_four,(162,DECK_Y_AXIS)) 
        
        
    #tile 5
    
        if self.random_deck[4] == 'A':
            tile_five = ATILE
        if self.random_deck[4] == 'B':
            tile_five = BTILE
        if self.random_deck[4] == 'C':
            tile_five = CTILE   
        if self.random_deck[4] == 'D':
            tile_five = DTILE    
        if self.random_deck[4] == 'E':
            tile_five = ETILE    
        if self.random_deck[4] == 'F':
            tile_five = FTILE
        if self.random_deck[4] == 'G':
            tile_five = GTILE   
        if self.random_deck[4] == 'H':
            tile_five = HTILE    
        if self.random_deck[4] == 'I':
            tile_five = ITILE   
        if self.random_deck[4] == 'J':
            tile_five = JTILE    
        if self.random_deck[4] == 'K':
            tile_five = KTILE 
        if self.random_deck[4] == 'L':
            tile_five = LTILE    
        if self.random_deck[4] == 'M':
            tile_five = MTILE   
        if self.random_deck[4] == 'N':
            tile_five = NTILE 
        if self.random_deck[4] == 'O':
            tile_five = OTILE
        if self.random_deck[4] == 'P':
            tile_five = PTILE
        if self.random_deck[4] == 'Q':
            tile_five = QTILE
        if self.random_deck[4] == 'R':
            tile_five = RTILE
        if self.random_deck[4] == 'S':
            tile_five = STILE
        if self.random_deck[4] == 'T':
            tile_five = TTILE
        if self.random_deck[4] == 'U':
            tile_five = UTILE
        if self.random_deck[4] == 'V':
            tile_five = VTILE
        if self.random_deck[4] == 'W':
            tile_five = WTILE
        if self.random_deck[4] == 'X':
            tile_five = XTILE
        if self.random_deck[4] == 'Y':
            tile_five = YTILE
        if self.random_deck[4] == 'Z':
            tile_five = ZTILE
        if self.random_deck[4] == 'BLANK':
            tile_five = BLANK  
            
        
        win.blit(tile_five,(216,DECK_Y_AXIS)) 
        
        #6
        if self.random_deck[5] == 'A':
            tile_six = ATILE
        if self.random_deck[5] == 'B':
            tile_six = BTILE
        if self.random_deck[5] == 'C':
            tile_six = CTILE   
        if self.random_deck[5] == 'D':
            tile_six = DTILE    
        if self.random_deck[5] == 'E':
            tile_six = ETILE    
        if self.random_deck[5] == 'F':
            tile_six = FTILE
        if self.random_deck[5] == 'G':
            tile_six = GTILE   
        if self.random_deck[5] == 'H':
            tile_six = HTILE    
        if self.random_deck[5] == 'I':
            tile_six = ITILE   
        if self.random_deck[5] == 'J':
            tile_six = JTILE    
        if self.random_deck[5] == 'K':
            tile_six = KTILE 
        if self.random_deck[5] == 'L':
            tile_six = LTILE    
        if self.random_deck[5] == 'M':
            tile_six = MTILE   
        if self.random_deck[5] == 'N':
            tile_six = NTILE 
        if self.random_deck[5] == 'O':
            tile_six = OTILE
        if self.random_deck[5] == 'P':
            tile_six = PTILE
        if self.random_deck[5] == 'Q':
            tile_six = QTILE
        if self.random_deck[5] == 'R':
            tile_six = RTILE
        if self.random_deck[5] == 'S':
            tile_six = STILE
        if self.random_deck[5] == 'T':
            tile_six = TTILE
        if self.random_deck[5] == 'U':
            tile_six = UTILE
        if self.random_deck[5] == 'V':
            tile_six = VTILE
        if self.random_deck[5] == 'W':
            tile_six = WTILE
        if self.random_deck[5] == 'X':
            tile_six = XTILE
        if self.random_deck[5] == 'Y':
            tile_six = YTILE
        if self.random_deck[5] == 'Z':
            tile_six = ZTILE
        if self.random_deck[5] == 'BLANK':
            tile_six = BLANK 
             
        win.blit(tile_six,(270,DECK_Y_AXIS)) 
        
        
        if self.random_deck[6] == 'A':
            tile_seven = ATILE
        if self.random_deck[6] == 'B':
            tile_seven = BTILE
        if self.random_deck[6] == 'C':
            tile_seven = CTILE   
        if self.random_deck[6] == 'D':
            tile_seven = DTILE    
        if self.random_deck[6] == 'E':
            tile_seven = ETILE    
        if self.random_deck[6] == 'F':
            tile_seven = FTILE
        if self.random_deck[6] == 'G':
            tile_seven = GTILE   
        if self.random_deck[6] == 'H':
            tile_seven = HTILE    
        if self.random_deck[6] == 'I':
            tile_seven = ITILE   
        if self.random_deck[6] == 'J':
            tile_seven = JTILE    
        if self.random_deck[6] == 'K':
            tile_seven = KTILE 
        if self.random_deck[6] == 'L':
            tile_seven = LTILE    
        if self.random_deck[6] == 'M':
            tile_seven = MTILE   
        if self.random_deck[6] == 'N':
            tile_seven = NTILE 
        if self.random_deck[6] == 'O':
            tile_seven = OTILE
        if self.random_deck[6] == 'P':
            tile_seven = PTILE
        if self.random_deck[6] == 'Q':
            tile_seven = QTILE
        if self.random_deck[6] == 'R':
            tile_seven = RTILE
        if self.random_deck[6] == 'S':
            tile_seven = STILE
        if self.random_deck[6] == 'T':
            tile_seven = TTILE
        if self.random_deck[6] == 'U':
            tile_seven = UTILE
        if self.random_deck[6] == 'V':
            tile_seven = VTILE
        if self.random_deck[6] == 'W':
            tile_seven = WTILE
        if self.random_deck[6] == 'X':
            tile_seven = XTILE
        if self.random_deck[6] == 'Y':
            tile_seven = YTILE
        if self.random_deck[6] == 'Z':
            tile_seven = ZTILE
        if self.random_deck[6] == 'BLANK':
            tile_seven = BLANK 
        
        win.blit(tile_seven,(324,DECK_Y_AXIS))
        
        
        
        
        # win.blit(self.random_deck[1]),(54,DECK_Y_AXIS)
        # win.blit(self.random_deck[2]),(108,DECK_Y_AXIS)
        # win.blit(self.random_deck[3]),(162,DECK_Y_AXIS)
        # win.blit(self.random_deck[4]),(216,DECK_Y_AXIS)
        # win.blit(self.random_deck[5]),(270,DECK_Y_AXIS)
        # win.blit(self.random_deck[6]),(324,DECK_Y_AXIS)
        
    def append_to_deck(self):
        print(self.random_deck[0])
        
    

class Tilebag:
    def __init__(self):
        self.tile_bag_values = TILE_VALUES
        self.tile_bag = self.create_list_of_tile_bag()
        
    def create_list_of_tile_bag(self):
        tile_bag = []
           
        for tile, details in self.tile_bag_values.items():
            qty = details.get('qty')
            
            for qty_of_tile in range(0, qty):
                tile_bag.append(tile)
        
        return tile_bag
           
            
        
    
    
        


    
    