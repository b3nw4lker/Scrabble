import pygame
from scrabbleproj.constants import WIDTH, HEIGHT
from scrabbleproj.board import Board
#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble
FPS = 244

WIN = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Scrabble')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
               

                

        board.draw_squares(WIN)
        board.draw_deck(WIN)
        board.draw_player1_score(WIN)
        board.draw_player2_score(WIN)
        board.draw_tile_boosters(WIN)
        board.draw_swap_button(WIN)
        
        pygame.display.update()

    pygame.quit()


main()