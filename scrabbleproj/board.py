import pygame 
from .constants import BLACK, COLS, ROWS, WHITE, ORANGE, SQUARE_SIZE, DECK_Y_AXIS, TRIPLEWORDIMG, TRIPLELETTERIMG, DOUBLEWORDIMG, DOUBLELETTERIMG, STARTTILE
from scrabbleproj.deck import Deck

class Board:
    def __init__(self):
        self.board = []
        self.deck = Deck()
        self.selected_tile = None
        
    #drawing the grid for scrabble
    def draw_squares(self, win):
        win.fill(WHITE)
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*SQUARE_SIZE, y*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(win, ORANGE, rect, 1)
    
    
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
        button_pressed = False
        pygame.font.init()
        font = pygame.font.Font('freesansbold.ttf',12)
        score = font.render("Swap tile", True, BLACK)
        win.blit(score,(510, 880))
        swapbuttonbox = pygame.Rect(500, 870, 100, 40)
        pygame.draw.rect(win, ORANGE, swapbuttonbox, 1)
        pos = pygame.mouse.get_pos()
        if swapbuttonbox.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and button_pressed == False: #Making it so that only one click is registered as a positive output
                button_pressed = True
                print('Clicked')
                button_pressed = False
    
    
    
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

    
#button class 
# class Button():
#     def __init__(self, x ,y, image):
#         self.image = image
#         self.rect = self.image.get_rect()
#         self.rect.topleft = (x, y)
#         self.clicked = False
    
#     def draw(self,win):
        
#         pos = pygame.mouse.get_pos()
#         if self.rect.collidepoint(pos):
#             if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False: #Making it so that only one click is registered as a positive output
#                 self.clicked = True
#                 print('Clicked')
                
#         if pygame.mouse.get_pressed()[0] == 0: #Making it so that you can click again after and that the button isnt just locked 
#             self.clicked = False
            
#         #draw button on screen
#         win.blit(self.image, (self.rect.x, self.rect.y))
        
# swap_button = Button(400, 870)



        
# def calc_pos(self):   still idea
#     x_coord = self.pos_on_board[0]
#     y_coord = self.pos_on_board[1]
#     print(x_coord)
#     print(y_coord)
#     # center_x_pos = x_coord
#     # self.x = SQUARE_SIZE * self.col + SQUARE_SIZE//2    #this is making sure that the position (coords)
#     # self.y = SQUARE_SIZE * self.row + SQUARE_SIZE//2    #that i get will be from the centre of the square    
        