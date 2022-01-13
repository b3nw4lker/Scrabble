import pygame
from scrabbleproj.constants import WIDTH, HEIGHT
from scrabbleproj.board import Board
#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble
FPS = 60

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
                pass

        board.draw_squares(WIN)
        pygame.display.update()

    pygame.quit()


main()