import pygame 
from .constants import BLACK, COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE, DECK_Y_AXIS, TRIPLEWORDIMG, TRIPLELETTERIMG, DOUBLEWORDIMG, DOUBLELETTERIMG, STARTTILE
from scrabbleproj.deck import Deck


class Board:
    def __init__(self, win):
        self.board = []
        self.win = win
        self.selected_tile = None
        
        self.draw_squares()
        self.draw_tile_boosters()
        self.draw_swap_button()
        self.draw_player1_score()
        self.draw_player2_score()
        
    #draself.wing the grid for scrabble
    def draw_squares(self):
        self.win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(self.win, ORANGE, rect, 1)
    
    
    #draself.wing player1 and 2 score
    def draw_player1_score(self):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Player 1 Score :", True, BLACK)
        self.win.blit(score,(871, 101))
        player1scorebox = pygame.Rect(870, 100, 100, 40)
        pygame.draw.rect(self.win, ORANGE, player1scorebox, 1)
          
    def draw_player2_score(self):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Player 2 Score :", True, BLACK)
        self.win.blit(score,(871, 401))
        player2scorebox = pygame.Rect(870, 400, 100, 40)
        pygame.draw.rect(self.win, ORANGE, player2scorebox, 1)
    
    
    #Swap Tile Button 
    def draw_swap_button(self):
        button_pressed = False
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Swap tile", True, BLACK)
        self.win.blit(score,(510, 880))
        swapbuttonbox = pygame.Rect(500, 870, 100, 40)
        pygame.draw.rect(self.win, ORANGE, swapbuttonbox, 1)
        pos = pygame.mouse.get_pos()
        if swapbuttonbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and button_pressed == False: #Making it so that only one click is registered as a positive output
                button_pressed = True
                print('Clicked')
                button_pressed = False
    
    
    
    #triple word placement
    def draw_tile_boosters(self):
        self.win.blit(TRIPLEWORDIMG,(0,0))
        self.win.blit(TRIPLEWORDIMG,(378,0))
        self.win.blit(TRIPLEWORDIMG,(756,0))
        self.win.blit(TRIPLEWORDIMG,(0,756))
        self.win.blit(TRIPLEWORDIMG,(378,756))
        self.win.blit(TRIPLEWORDIMG,(756,756))
        self.win.blit(TRIPLEWORDIMG,(0,378))
        self.win.blit(TRIPLEWORDIMG,(756,378))
        
        #triple letter placement
        self.win.blit(TRIPLELETTERIMG,(54,270))
        self.win.blit(TRIPLELETTERIMG,(54,486))
        self.win.blit(TRIPLELETTERIMG,(270,54))
        self.win.blit(TRIPLELETTERIMG,(270,270))
        self.win.blit(TRIPLELETTERIMG,(270,486))
        self.win.blit(TRIPLELETTERIMG,(270,702))
        self.win.blit(TRIPLELETTERIMG,(486,54))
        self.win.blit(TRIPLELETTERIMG,(486,270))
        self.win.blit(TRIPLELETTERIMG,(486,486))
        self.win.blit(TRIPLELETTERIMG,(486,702))
        self.win.blit(TRIPLELETTERIMG,(702,270))
        self.win.blit(TRIPLELETTERIMG,(702,486))
        
        #double letter placement
        self.win.blit(DOUBLELETTERIMG,(0,162))
        self.win.blit(DOUBLELETTERIMG,(0,594))
        self.win.blit(DOUBLELETTERIMG,(108,324))
        self.win.blit(DOUBLELETTERIMG,(108,432))
        self.win.blit(DOUBLELETTERIMG,(162,0))
        self.win.blit(DOUBLELETTERIMG,(162,378))
        self.win.blit(DOUBLELETTERIMG,(162,756))
        self.win.blit(DOUBLELETTERIMG,(324,108))
        self.win.blit(DOUBLELETTERIMG,(324,324))
        self.win.blit(DOUBLELETTERIMG,(324,432))
        self.win.blit(DOUBLELETTERIMG,(324,648))
        self.win.blit(DOUBLELETTERIMG,(378,162))
        self.win.blit(DOUBLELETTERIMG,(378,594))
        self.win.blit(DOUBLELETTERIMG,(432,108))
        self.win.blit(DOUBLELETTERIMG,(432,324))
        self.win.blit(DOUBLELETTERIMG,(432,432))
        self.win.blit(DOUBLELETTERIMG,(432,648))
        self.win.blit(DOUBLELETTERIMG,(594,0))
        self.win.blit(DOUBLELETTERIMG,(594,378))
        self.win.blit(DOUBLELETTERIMG,(594,756))
        self.win.blit(DOUBLELETTERIMG,(648,324))
        self.win.blit(DOUBLELETTERIMG,(648,432))
        self.win.blit(DOUBLELETTERIMG,(756,162))
        self.win.blit(DOUBLELETTERIMG,(756,594))
        
        #double word placement
        self.win.blit(DOUBLEWORDIMG,(54,54))
        self.win.blit(DOUBLEWORDIMG,(54,702))
        self.win.blit(DOUBLEWORDIMG,(108,108))
        self.win.blit(DOUBLEWORDIMG,(108,648))
        self.win.blit(DOUBLEWORDIMG,(162,162))
        self.win.blit(DOUBLEWORDIMG,(162,594))
        self.win.blit(DOUBLEWORDIMG,(216,216))
        self.win.blit(DOUBLEWORDIMG,(216,540))
        self.win.blit(DOUBLEWORDIMG,(540,216))
        self.win.blit(DOUBLEWORDIMG,(540,540))
        self.win.blit(DOUBLEWORDIMG,(594,162))
        self.win.blit(DOUBLEWORDIMG,(594,594))
        self.win.blit(DOUBLEWORDIMG,(648,108))
        self.win.blit(DOUBLEWORDIMG,(648,648))
        self.win.blit(DOUBLEWORDIMG,(702,54))
        self.win.blit(DOUBLEWORDIMG,(702,702))
        
        self.win.blit(STARTTILE,(378,378))