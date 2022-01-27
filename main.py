import pygame
from scrabbleproj.constants import WIDTH, HEIGHT
from scrabbleproj.board import Board
from scrabbleproj.deck import Deck

#Ben Walker 
#Scrabble Project for NEA

# Example Link - https://github.com/cheukyin699/py-scrabble
from scrabbleproj.game_manager import GameManager

FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Scrabble')

# swap_button = Button(400, 870)


def main():
    run = True
    clock = pygame.time.Clock()
    game_manager = GameManager(WIN)
    # board = Board(WIN)
    # deck = Deck(WIN)

    # Move all this into a player state class and then instantiate that class in the while True Loop
    while run:
        clock.tick(FPS)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print(mouse_position)
                game_manager.deck.over_ride_tile_image()

        print(game_manager.deck.tile_bag.get_tile_bag_count())
        pygame.display.update()

    pygame.quit()

main()