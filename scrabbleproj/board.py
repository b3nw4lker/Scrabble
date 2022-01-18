import pygame 
from .constants import BLACK, COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE, DECK_Y_AXIS, TRIPLEWORDIMG, TRIPLELETTERIMG, DOUBLEWORDIMG, DOUBLELETTERIMG, STARTTILE


class Board:
    def __init__(self):
        self.board = []
        self.deck = []
        self.selected_tile = None
        
    #drawing the grid for scrabble
    def draw_squares(self, win):
        win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, ORANGE, rect, 1)
    
    #drawing the deck 
    def draw_deck(self, win):
        for x in range(7): 
            deckboxes = pygame.Rect(x*SQUARE_SIZE, DECK_Y_AXIS, 53, 53)
            pygame.draw.rect(win, ORANGE, deckboxes, 1)
    
    #drawing player1 and 2 score
    def draw_player1_score(self, win):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Player 1 Score :", True, BLACK)
        win.blit(score,(871, 101))
        player1scorebox = pygame.Rect(870, 100, 100, 40)
        pygame.draw.rect(win, ORANGE, player1scorebox, 1)
          
    def draw_player2_score(self, win):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Player 2 Score :", True, BLACK)
        win.blit(score,(871, 401))
        player2scorebox = pygame.Rect(870, 400, 100, 40)
        pygame.draw.rect(win, ORANGE, player2scorebox, 1)
    
    
    #Swap Tile Button 
    def draw_swap_button(self,win):
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Swap tile", True, BLACK)
        win.blit(score,(505, 875))
        swapbuttonbox = pygame.Rect(500, 870, 100, 40)
        pygame.draw.rect(win, ORANGE, swapbuttonbox, 1)
    
    #triple word placement
    def draw_tile_boosters(self, win):
        win.blit(TRIPLEWORDIMG,(0,0))
        win.blit(TRIPLEWORDIMG,(378,0))
        win.blit(TRIPLEWORDIMG,(756,0))
        win.blit(TRIPLEWORDIMG,(0,756))
        win.blit(TRIPLEWORDIMG,(378,756))
        win.blit(TRIPLEWORDIMG,(756,756))
        win.blit(TRIPLEWORDIMG,(0,378))
        win.blit(TRIPLEWORDIMG,(756,378))
        
        #triple letter placement
        win.blit(TRIPLELETTERIMG,(54,270))
        win.blit(TRIPLELETTERIMG,(54,486))
        win.blit(TRIPLELETTERIMG,(270,54))
        win.blit(TRIPLELETTERIMG,(270,270))
        win.blit(TRIPLELETTERIMG,(270,486))
        win.blit(TRIPLELETTERIMG,(270,702))
        win.blit(TRIPLELETTERIMG,(486,54))
        win.blit(TRIPLELETTERIMG,(486,270))
        win.blit(TRIPLELETTERIMG,(486,486))
        win.blit(TRIPLELETTERIMG,(486,702))
        win.blit(TRIPLELETTERIMG,(702,270))
        win.blit(TRIPLELETTERIMG,(702,486))
        
        #double letter placement
        win.blit(DOUBLELETTERIMG,(0,162))
        win.blit(DOUBLELETTERIMG,(0,594))
        win.blit(DOUBLELETTERIMG,(108,324))
        win.blit(DOUBLELETTERIMG,(108,432))
        win.blit(DOUBLELETTERIMG,(162,0))
        win.blit(DOUBLELETTERIMG,(162,378))
        win.blit(DOUBLELETTERIMG,(162,756))
        win.blit(DOUBLELETTERIMG,(324,108))
        win.blit(DOUBLELETTERIMG,(324,324))
        win.blit(DOUBLELETTERIMG,(324,432))
        win.blit(DOUBLELETTERIMG,(324,648))
        win.blit(DOUBLELETTERIMG,(378,162))
        win.blit(DOUBLELETTERIMG,(378,594))
        win.blit(DOUBLELETTERIMG,(432,108))
        win.blit(DOUBLELETTERIMG,(432,324))
        win.blit(DOUBLELETTERIMG,(432,432))
        win.blit(DOUBLELETTERIMG,(432,648))
        win.blit(DOUBLELETTERIMG,(594,0))
        win.blit(DOUBLELETTERIMG,(594,378))
        win.blit(DOUBLELETTERIMG,(594,756))
        win.blit(DOUBLELETTERIMG,(648,324))
        win.blit(DOUBLELETTERIMG,(648,432))
        win.blit(DOUBLELETTERIMG,(756,162))
        win.blit(DOUBLELETTERIMG,(756,594))
        
        #double word placement
        win.blit(DOUBLEWORDIMG,(54,54))
        win.blit(DOUBLEWORDIMG,(54,702))
        win.blit(DOUBLEWORDIMG,(108,108))
        win.blit(DOUBLEWORDIMG,(108,648))
        win.blit(DOUBLEWORDIMG,(162,162))
        win.blit(DOUBLEWORDIMG,(162,594))
        win.blit(DOUBLEWORDIMG,(216,216))
        win.blit(DOUBLEWORDIMG,(216,540))
        win.blit(DOUBLEWORDIMG,(540,216))
        win.blit(DOUBLEWORDIMG,(540,540))
        win.blit(DOUBLEWORDIMG,(594,162))
        win.blit(DOUBLEWORDIMG,(594,594))
        win.blit(DOUBLEWORDIMG,(648,108))
        win.blit(DOUBLEWORDIMG,(648,648))
        win.blit(DOUBLEWORDIMG,(702,54))
        win.blit(DOUBLEWORDIMG,(702,702))
        
        win.blit(STARTTILE,(378,378))

    # def calc_pos(self):   still idea
    #     x_coord = self.pos_on_board[0]
    #     y_coord = self.pos_on_board[1]
    #     print(x_coord)
    #     print(y_coord)
    #     # center_x_pos = x_coord
    #     # self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2    #this is making sure that the position (coords)
    #     # self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2    #that i get will be from the centre of the square    
        