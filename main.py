import pygame
from scrabbleproj.constants import WIDTH, HEIGHT
from scrabbleproj.board import Board
from scrabbleproj.deck import Deck, Tilebag

#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble
FPS = 60

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Scrabble')

# swap_button = Button(400, 870)

def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    deck = Deck()
    tilebag = Tilebag()

    
    deck.create_random_tile_deck()
    deck.append_to_deck()
    
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
               

        # swap_button.draw(WIN)     
        board.draw_squares(WIN)
        board.draw_player1_score(WIN)
        board.draw_player2_score(WIN)
        board.draw_tile_boosters(WIN)
        board.draw_swap_button(WIN)
        deck.draw_deck(WIN)
        
        
        pygame.display.update()

    pygame.quit()


main()